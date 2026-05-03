#!/bin/bash

echo "Test file" > test.txt

gcloud storage cp test.txt gs://my-project-bucket