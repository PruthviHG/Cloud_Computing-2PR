# Smart Cloud File Upload System

## Description
This project demonstrates a cloud-based file upload system using Google Cloud.

## Features
- Upload file via web interface
- File stored in Cloud Storage
- Cloud Function triggered automatically
- Logs file activity

## Technologies
- Google Cloud Storage
- Cloud Functions
- App Engine (Flask)
- gcloud CLI

## Steps to Run

1. Create bucket
   ./scripts/create_bucket.sh

2. Deploy Cloud Function
   ./scripts/deploy_function.sh

3. Deploy App Engine
   ./scripts/deploy_app.sh

4. Open web app and upload file

5. Check logs
   gcloud functions logs read file_upload_trigger --region=us-central1
