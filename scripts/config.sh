#!/usr/bin/env bash
# shellcheck disable=SC2034

APP_NAME=vlim-co-sam-python-mongo-boilerplate
STAGE_NAME=dev
S3_BUCKET=$APP_NAME-$STAGE_NAME-bucket
STACK_NAME=$APP_NAME-$STAGE_NAME-stack
PROFILE=private.vlim
REGION=us-east-1
INPUT_FILE=template.yaml
OUTPUT_FILE=packaged.yaml
DB_PASSWORD="bLgOTWoUvI4kaUtN"
DB_NAME="vlim-co-sam-python-boilerplate"
DATABASE_URI="mongodb+srv://vlim:${DB_PASSWORD}@vlim-sam-python-mongodb.qzg3k.mongodb.net/${DB_NAME}?retryWrites=true&w=majority"

