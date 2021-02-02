# Docker file for {{ cookiecutter.app_name }} ChRIS plugin app
#
# Build with
#
#   docker build -t <name> .
#
# For example if building a local version, you could do:
#
#   docker build -t local/{{ cookiecutter.app_repo_name }} .
#
# In the case of a proxy (located at 192.168.13.14:3128), do:
#
#    docker build --build-arg http_proxy=http://192.168.13.14:3128 --build-arg UID=$UID -t local/{{ cookiecutter.app_repo_name }} .
#
# To run an interactive shell inside this container, do:
#
#   docker run -ti --entrypoint /bin/bash local/{{ cookiecutter.app_repo_name }}
#
# To pass an env var HOST_IP to container, do:
#
#   docker run -ti -e HOST_IP=$(ip route | grep -v docker | awk '{if(NF==11) print $9}') --entrypoint /bin/bash local/{{ cookiecutter.app_repo_name }}
#

FROM python:3.9.1-buster
LABEL maintainer="{{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>"

WORKDIR /usr/local/src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install .

WORKDIR /usr/local/bin
CMD ["{{ cookiecutter.app_name }}", "--help"]
