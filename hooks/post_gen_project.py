# Attempt to generate the projct title ASCII-art using figlet from a web service.
# You know, the
#                  _    _                 _   _                       _          _                       
#                 | |  (_)               | | | |                     | |        (_)                      
#   ___ ___   ___ | | ___  ___  ___ _   _| |_| |_ ___ _ __ ______ ___| |__  _ __ _ ___  __ _ _ __  _ __  
#  / __/ _ \ / _ \| |/ / |/ _ \/ __| | | | __| __/ _ \ '__|______/ __| '_ \| '__| / __|/ _` | '_ \| '_ \ 
# | (_| (_) | (_) |   <| |  __/ (__| |_| | |_| ||  __/ |        | (__| | | | |  | \__ \ (_| | |_) | |_) |
#  \___\___/ \___/|_|\_\_|\___|\___|\__,_|\__|\__\___|_|         \___|_| |_|_|  |_|___/\__,_| .__/| .__/ 
#                                                                                           | |   | |    
#                                                                                           |_|   |_|    
# thing

from subprocess import check_output, CalledProcessError

service_url = 'http://route-figlet-faas.k-apps.osh.massopen.cloud/'


class FigletPatchException(Exception):
    pass

try:
    # it's more likely that a user has curl installed on their system
    # (default on most Linux, Mac, apparently Windows too)
    # than something like requests
    try:
        pretty_title = check_output(
            [
                'curl', '-s',
                f'{service_url}?message=' + '{{ cookiecutter.app_name }}'
            ],
            timeout=5, encoding='utf8'
        )
    except CalledProcessError as e:
        raise FigletPatchException('curl unsuccessful')

    # chop off leading empty lines
    for i in range(10):
        empty_position = pretty_title.index('\n') + 1
        if not pretty_title[:empty_position].lstrip():
            pretty_title = pretty_title[empty_position:]
        else:
            break

    print(pretty_title)

    filename = '{{ cookiecutter.app_name }}/{{ cookiecutter.app_name }}.py'

    with open(filename, 'r') as f:
        original_lines = f.readlines()
    
    # find location in file where Gstr_title is defined
    start_index = -1
    end_index = -1
    for i, line in enumerate(original_lines):
        if line.startswith('Gstr_title = """'):
            start_index = i
            break
    if start_index < 0:
        raise FigletPatchException('Could not find location to insert title')

    for i, line in enumerate(original_lines[start_index+1:]):
        if line.startswith('"""'):
            end_index = i + start_index + 1
            break
    if end_index < 0:
        raise FigletPatchException('Could not find ending """')

    # overwrite the file with patched content
    with open(filename, 'w') as f:
        f.write(''.join(original_lines[:start_index + 1]))
        f.write(pretty_title + '\n')
        f.write(''.join(original_lines[end_index:]))

except FigletPatchException as e:
    print('Could not automatically generate figlet title from web service.')
