import io
import cv2
import requests
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
import argparse

MODEL = 'hold-detection'
VERSION = '1'
API_KEY = '3cZO2UYZLwtFu4j2STv0'

def get_parser():
    parser = argparse.ArgumentParser(description='Command line utility for hold detection')
    parser.add_argument('-i', '--image_path', type=str, required=True, help='Path to image for hold detection')
    return parser

def predict_holds(rgb_img):
    pil_image = Image.fromarray(rgb_img)
    buffered = io.BytesIO()
    pil_image.save(buffered, format="JPEG", quality=100)
    multipart_data = MultipartEncoder(
        fields={'file': ("imageToUpload", buffered.getvalue(), "image/jpeg")}
    )
    url = f"https://detect.roboflow.com/{MODEL}/{VERSION}?api_key={API_KEY}"
    response = requests.post(url, data=multipart_data, headers={'Content-Type': multipart_data.content_type})
    return response.status_code, response.json()