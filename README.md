# Contentor Video Processor Demo

This repository demonstrates the implementation and usage of the Contentor Video Processing API. The demo shows how to upload, process, and retrieve video content using the Contentor service.

[package's repository](https://github.com/tahayusufkomur/django-contentor-video-processor)

## Preview

Below are screenshots that demonstrate the key features and interfaces of the Contentor Video Processor Demo:

*The video uploaded with chunks to prevent timeout or memory leak*
![Video Upload Interface](/docs/upload.gif)

*Contentor dashboard for realtime monitoring*
![Results Dashboard](/docs/contentor-dashboard.png)

*Status Table in the beginning admin panel*
![Status Table](/docs/status-table-1.png)

*Status Table after complete in the admin panel*
![Status Table](/docs/status-table-2.png)

*Built-in player with resolution settings*
![Video Player](/docs/video_player.gif)

## Prerequisites

- Contentor API credentials (key and secret)
- S3-compatible storage (AWS S3, Hetzner Storage Box, or self-hosted S3)
- Storage access credentials (access key and secret key)
- Ngrok account (for webhook testing)
- Python 3.8+
- Django 3.2+

## Setup Instructions

### 1. Get Contentor API Credentials

Register for a free account at [process.contentor.app](https://process.contentor.app) to obtain your API key and secret.

### 2. Configure S3 Storage

Ensure you have access to an S3-compatible storage service with:
- Bucket name
- Access key
- Secret key
- Endpoint URL (for non-AWS S3 services)

### 3. Clone the Repository

```bash
git clone https://github.com/tahayusufkomur/django-contentor-processor-demo.git
cd contentor-contentor-processor-demo
```

### 4. Environment Setup

Copy the environment template to create your `.env` file:

```bash
cp env-template .env
```

Edit the `.env` file with your credentials and configuration:

```
CONTENTOR_API_KEY=your_api_key
CONTENTOR_API_SECRET=your_api_secret
S3_ACCESS_KEY=your_s3_access_key
S3_SECRET_KEY=your_s3_secret_key
S3_BUCKET_NAME=your_bucket_name
S3_ENDPOINT_URL=your_endpoint_url  # Only needed for non-AWS S3
```

### 5. Install Dependencies

**Note:** The requirements versions are strict. Please use the exact versions specified.

```bash
pip install -r requirements.txt
```

### 6. Database Setup

Run migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

### 9. Set Up Webhook Testing with ngrok

Install ngrok if you haven't already, then start it:

```bash
ngrok http 8000
```

Note the HTTPS URL provided by ngrok (e.g., `https://abcd1234.ngrok.app`).

### 10. Update Webhook URL in Settings

Update the `BASE_URL` in your `settings.py` file with the ngrok URL:

```python
BASE_URL = "https://abcd1234.ngrok.app"
```

### 11. Create Admin User and Add a Video

Create a superuser to access the Django admin panel:

```bash
python manage.py createsuperuser
```

Then:
1. Go to `http://localhost:8000/admin`
2. Log in with your superuser credentials
3. Navigate to the Videos section
4. Click "Add Video" to create a new video entry
5. Fill in the required details and upload a video file
6. Save the entry to trigger the Contentor processing

## How It Works

1. When a video is created through the admin interface, the application uploads it to your S3 bucket
2. The application then sends the video details to Contentor for processing
3. Contentor processes the video and sends a webhook notification to your application when complete
4. The application receives the webhook and updates the video status

## Webhook Information

The webhook endpoint at `/contentor/webhook/` receives processing status updates from Contentor. Make sure your ngrok URL is correctly set in the `WEBHOOK_URL` setting for this to work properly.

## Troubleshooting

- Ensure your S3 bucket has the correct permissions set
- Verify your Contentor API credentials are correct
- Check the Django server logs for any error messages
- Ensure ngrok is running and the URL is correctly set in your settings

## License

MIT License.
```