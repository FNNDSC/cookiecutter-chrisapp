#!/bin/bash -ex
# Use the template to create an example FS app, then run it locally.
#
# Preconditions:
# - install cookiecutter, curl, jq-1.6
# - CUBE and ChRIS_store are running on :8000 and :8010 respectively
#   with default user "chris:chris1234"
# - CUBE's container has the name "chris"
#
# To meet the ChRIS backend preconditions, see
# https://github.com/FNNDSC/minimake
# 
# The example app is customized by appending text to the source code,
# overriding define_parameters and run.
# It should be run as
#
#     docker run --rm -v $PWD/out:/outgoing local/pl-cctest appname --give present /outgoing
#
# If successful, a file ./out/goodbye will be created containing the string
#
#     it works :o
#
# The example plugin is registered into CUBE with a random name.
# Then we run it. Finally, we assert that it has "finishedSuccessfully"
# and that it creates an output file as described above.
#
# The resulting example app is created in a temporary directory which
# is removed if this script succeeds. Otherwise, check stdout.
# Since naming is randomized, collisions should not be a problem
# and this script can be run over and over again (or even in parallel)
# against the same CUBE instance without needing to wipe it.

repo="${1:-https://github.com/FNNDSC/cookiecutter-chrisapp.git}"

folder=$(mktemp -dt cookiecutter-test-XXXX)

cookiecutter -o "$folder" "$repo" << EOF
AuthorName
dne@babyMRI.org
pl-cctest
appname
AppClassName
2
A cool title for a cool test
Utility
To describe pl-cctest, it does literally nothing
https://github.com/FNNDSC/cookiecutter-chrisapp#readme
1.0.0
2
2
3
EOF

# add functionality

cat >> $folder/pl-cctest/appname/appname.py << EOF
    def define_parameters(self):
        self.add_argument('-g', '--give', 
                          dest         = 'give', 
                          type         = str, 
                          optional     = False,
                          help         = 'give me a "present"')
        self.add_argument('-t', '--take', 
                          dest         = 'take', 
                          type         = str, 
                          optional     = True,
                          help         = 'please do not take anything',
                          default      = 'nothing')

    def run(self, options):
        if options.give != 'present':
            raise ValueError('please give me a "present" with --give present')
        from os import path
        with open(path.join(options.outputdir, 'goodbye'), 'w') as f:
            f.write('it works :o')
EOF


# upload to ChRIS_store

name="pl-cctest-$RANDOM"
docker build -q -t local/pl-cctest $folder/pl-cctest

mkdir $folder/json
docker run --rm -u "$(id -u)" -v $folder/json:/out local/pl-cctest appname --savejson /out
curl -u chris:chris1234 -s 'http://localhost:8010/api/v1/plugins/' \
  -F 'dock_image=local/pl-cctest' \
  -F "descriptor_file=@$folder/json/AppClassName.json" \
  -F 'public_repo=https://github.com/FNNDSC/dne' \
  -F "name=$name"

docker exec chris python plugins/services/manager.py register host --pluginname $name

# run the created plugin

inst_url=$(
  curl -s "http://localhost:8000/api/v1/plugins/search/?name=$name" \
    -u 'chris:chris1234' \
    -H 'Accept: application/json' | jq -r '.results[0].instances'
)
feed=$(
  curl -s "$inst_url" \
    -u 'chris:chris1234' \
    -H 'Content-Type: application/vnd.collection+json' \
    -H 'Accept: application/json' \
    --data '{"template":{"data":[{"name": "give", "value": "present"}]}}'
)
job_url=$(echo $feed | jq -r .url)

# wait for job to finish, timeout after 2 minutes
{ set +x; } 2> /dev/null
for i in {0..60}; do
  sleep 2
  job=$(
    curl -s "$job_url" \
      -u 'chris:chris1234' \
      -H 'Accept: application/json'
  )
  run_status=$(echo $job | jq -r .status)
  if [[ "$run_status" == "finished"* ]]; then
    break
  fi
  printf .
done
echo

# check that it was successful

set -x
if [ "$run_status" != "finishedSuccessfully" ]; then
  exit 1
fi

files_url=$(echo $job | jq -r .files)
files_data=$(curl -s "$files_url" -u 'chris:chris1234')

# this is some dark magic to parse the cumbersome JSON response
# and wrangle it into { fname, file_resource } mappings,
# then choose the hard-coded filename created by our test plugin.

file_resource=$(
  echo "$files_data" | jq -r '.collection.items[] |
    {fname: (.data | from_entries | .fname),
    file_resource: (.links | map({key: .rel, value: .href}) | from_entries | .file_resource)}
    | select(.fname | endswith("goodbye")) | .file_resource'
)

curl -s "$file_resource" -u 'chris:chris1234' | grep -Fq 'it works'

# clean up

set +e
cleanup_success=0
rm -rf $folder                 || cleanup_success=2
docker rmi -f local/pl-cctest  || cleanup_success=2
exit $cleanup_success
