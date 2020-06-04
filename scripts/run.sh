#!/usr/bin/env bash

source scripts/config.sh
rm -rf .aws-sam
sam build && \
sam local start-api --region "$REGION" --profile "$PROFILE"  --skip-pull-image --debug-port 5890
