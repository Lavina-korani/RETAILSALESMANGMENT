import cv2
import os

def detect_product(image_path):
    known_products = {
        'chips': "data/chips.png",
        'soap': "data/soap.png",
        'cold_drink': "data/cold_drink.png",
        'shampoo': "data/shampoo.png"
    }

    img_input = cv2.imread(image_path)

    if img_input is None:
        return "Input Image Not Found!"

    img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)

    for product, path in known_products.items():
        if not os.path.exists(path):
            continue

        img_product = cv2.imread(path)

        if img_product is None:
            continue

        img_product = cv2.cvtColor(img_product, cv2.COLOR_BGR2GRAY)

        res = cv2.matchTemplate(img_input, img_product, cv2.TM_CCOEFF_NORMED)
        threshold = 0.7
        loc = cv2.minMaxLoc(res)

        if loc[1] >= threshold:
            return product

    return "Unknown Product"


def detect_customer(image_path):
    if not os.path.exists(image_path):
        return "Unknown Customer"

    customer_name = os.path.splitext(os.path.basename(image_path))[0]
    return customer_name.capitalize()


