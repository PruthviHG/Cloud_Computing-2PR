from flask import Flask, request, render_template_string
from google.cloud import storage
import os

app = Flask(__name__)

BUCKET_NAME = "my-project-bucket"   # ⚠️ CHANGE THIS

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Upload System</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">
    <h1>📁 Smart Cloud Upload</h1>

    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <br><br>
        <button type="submit">Upload</button>
    </form>

    {% if message %}
        <p style="color:green; font-size:18px;">{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def upload():
    message = ""

    if request.method == "POST":
        file = request.files.get("file")

        if file:
            client = storage.Client()
            bucket = client.bucket(BUCKET_NAME)
            blob = bucket.blob(file.filename)

            blob.upload_from_file(file)

            message = f"✅ File '{file.filename}' uploaded successfully!"

    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)