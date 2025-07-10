# Test
just to test codex

## Image Compression App

This repository includes a small Flask application that lets you select multiple images and specify a folder name. Each image is compressed to JPEG format with reduced quality before being packaged into a ZIP archive. The UI is a simple HTML form.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python image_compressor/app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser and upload images to receive a ZIP archive containing the compressed JPEGs.
