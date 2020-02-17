#!/bin/bash -x

set -e

rm -rf layer/python_libs
docker build -t requests-lambda-layer/python_libs .
CONTAINER=$(docker run -d requests-lambda-layer/python_libs false)
docker cp $CONTAINER:/opt layer/python_libs
docker rm $CONTAINER
touch layer/python_libs/.slsignore
cat > layer/python_libs/.slsignore << EOF
**/*.a
**/*.la
share/**
include/**
bin/**
EOF
