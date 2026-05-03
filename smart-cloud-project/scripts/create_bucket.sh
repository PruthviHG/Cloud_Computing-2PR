#!/bin/bash

gcloud config set project YOUR_PROJECT_ID

gcloud storage buckets create gs://my-project-bucket --location=us-central1