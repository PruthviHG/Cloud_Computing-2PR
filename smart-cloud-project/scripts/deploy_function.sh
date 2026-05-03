#!/bin/bash

cd cloud-function

gcloud functions deploy file_upload_trigger \
 --gen2 \
 --runtime=python311 \
 --region=us-central1 \
 --source=. \
 --entry-point=file_upload_trigger \
 --trigger-event-filters="type=google.cloud.storage.object.v1.finalized" \
 --trigger-event-filters="bucket=my-project-bucket" \
 --allow-unauthenticated