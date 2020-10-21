#!/usr/bin/env bash

source scripts/config.sh
rm -rf .aws-sam
sh scripts/layer-preparation.sh

aws s3api 	--profile "$PROFILE" create-bucket \
			--bucket "$S3_BUCKET" \
			--region "$REGION"

sam package --profile "$PROFILE" \
			--template-file "$INPUT_FILE" \
			--output-template-file "$OUTPUT_FILE" \
			--s3-bucket "$S3_BUCKET"

sam deploy 	--profile "$PROFILE" \
			--region "$REGION" \
			--template-file "$OUTPUT_FILE" \
			--stack-name "$STACK_NAME" \
			--parameter-overrides \
				StageName="$STAGE_NAME" \
				DeploymentS3BucketName="$S3_BUCKET" \
				AppName="$APP_NAME" \
			--capabilities CAPABILITY_IAM

# shellcheck disable=SC2155
export API_GATEWAY_URL=$( \
aws cloudformation describe-stacks \
					--profile "$PROFILE" \
					--region "$REGION" \
					--stack-name "$STACK_NAME" \
					--query 'Stacks[0].Outputs[0].OutputValue' \
					--output text \
)

echo "API Gateway URL: $API_GATEWAY_URL"
