#!/bin/bash

gcloud config set project gen-lang-client-0597944803

gcloud storage buckets create gs://my-project-bucket --location=us-central1
