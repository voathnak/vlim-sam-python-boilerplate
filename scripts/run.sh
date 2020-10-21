#!/usr/bin/env bash

source scripts/config.sh
rm -rf .aws-sam
sh scripts/layer-preparation.sh
#sam build && \
sam local start-api --region "$REGION" --profile "$PROFILE"  --skip-pull-image --debug-port 5890
