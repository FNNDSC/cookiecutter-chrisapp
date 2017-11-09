# Docker file for the {{ cookiecutter.app_name }} plugin app

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/{{ cookiecutter.app_name }}"  VERSION="0.1"
COPY ["{{ cookiecutter.app_name }}", "${APPROOT}"]
COPY ["requirements.txt", "${APPROOT}"]

WORKDIR $APPROOT

RUN pip install -r requirements.txt

CMD ["{{ cookiecutter.app_name }}.py", "--json"]