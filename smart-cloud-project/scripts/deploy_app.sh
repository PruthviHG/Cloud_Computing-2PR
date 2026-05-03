#!/bin/bash

cd app-engine

gcloud app create --region=us-central1

gcloud app deploy

gcloud app browse