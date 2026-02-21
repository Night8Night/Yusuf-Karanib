from flask import Flask
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')

@app.route("/")
def home():
    try:
        response = s3.get_object(Bucket='yusuf-babystore-data-2026', Key='test.txt')
        content = response['Body'].read().decode('utf-8')
        return f"<h1>Babystore Analytics</h1><p>Data from S3: {content}</p>"
    except Exception as e:
        return f"<h1>S3 Connection Error</h1><p>{str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
