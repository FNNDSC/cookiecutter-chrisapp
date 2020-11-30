#!/bin/bash -ex
# use the template to create an example FS app, then run it locally

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
1.0
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
    --data '{"template":{"data":[]}}'
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

# clean up

rm -rf $folder
