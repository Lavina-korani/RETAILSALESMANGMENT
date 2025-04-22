# detection.py
from PIL import Image
import numpy as np
import os

def detect_product(input_data):
    """
    Accepts either a file path (str) or a PIL Image.
    """
    if isinstance(input_data, str) and os.path.isfile(input_data):
        # From tkinter: file path
        image = Image.open(input_data)
    elif isinstance(input_data, Image.Image):
        # From Streamlit: PIL Image
        image = input_data
    else:
        raise ValueError("Unsupported input format for detect_product")

    # Convert image to array for model (if needed)
    image_array = np.array(image)

    # TODO: Run your real model here
    return {"name": "Detected Product", "price": 120}


def detect_customer(input_data):
    # Same as above (optional)
    return {"name": "John Doe"}
