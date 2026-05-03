import functions_framework

@functions_framework.cloud_event
def file_upload_trigger(cloud_event):
    data = cloud_event.data

    file_name = data.get("name", "Unknown")
    bucket = data.get("bucket", "Unknown")

    print(f"✅ File '{file_name}' uploaded to bucket '{bucket}'")