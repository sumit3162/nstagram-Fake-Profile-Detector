# detector_app/model_functions.py
from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np
from mtcnn.mtcnn import MTCNN

def check_if_real_profile_pic(profile_pic_url):
    try:
        response = requests.get(profile_pic_url)
        img = Image.open(BytesIO(response.content))

        # Convert PIL Image to OpenCV format
        open_cv_image = np.array(img)
        
        # Create an MTCNN detector
        detector = MTCNN()

        # Detect faces in the image using MTCNN
        faces_mtcnn = detector.detect_faces(open_cv_image)

        # If faces are detected by MTCNN, consider it a real profile picture
        if faces_mtcnn:
            return True

        # If MTCNN does not detect faces, fallback to the original OpenCV-based logic
        is_real_human = actual_image_processing_logic(img)
        return is_real_human
    except Exception as e:
        print(f"Error checking profile picture: {e}")
        return False

def analyze_content(username, access_token):
    try:
        # Placeholder for media data, replace with actual Instagram API call
        media_data = [{'media_type': 'IMAGE'}, {'media_type': 'VIDEO'}, {'media_type': 'IMAGE'}]
        content_types = [actual_content_analysis_logic(media) for media in media_data]
        most_frequent_content_type = max(set(content_types), key=content_types.count)
        return most_frequent_content_type
    except Exception as e:
      print(f"Error processing image: {e}")
    return False


def actual_image_processing_logic(image):
    # Example image processing logic (original OpenCV-based face detection)
    try:
        # Convert PIL Image to OpenCV format
        open_cv_image = np.array(image)
        gray_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2GRAY)

        # Load a pre-trained face detector
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Detect faces in the image using OpenCV
        faces_opencv = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

        # If faces are detected, consider it a real profile picture
        return len(faces_opencv) > 0
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

def actual_content_analysis_logic(media):
    # Example content analysis logic
    # Analyze the media type and return a category
    try:
        if media['media_type'] == 'IMAGE':
            # Example: Check if the image is real
            return 'real'
        elif media['media_type'] == 'VIDEO':
            # Example: Check if the video is animated
            return 'animated'
        else:
            return 'unknown'
    except Exception as e:
        print(f"Error analyzing content: {e}")
        return 'unknown'
