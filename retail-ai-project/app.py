import streamlit as st
from PIL import Image
from detection import detect_product, detect_customer
from billing import generate_bill
from database import connect_db

# Connect to database
connect_db()

# App title
st.set_page_config(page_title="Retail Sales Management AI", layout="wide")
st.title("🛍️ ONLINE CASHEIR (YOUR BILL)")

# Upload multiple images
uploaded_files = st.file_uploader("Upload Product Images", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

# Process images
total_price = 0
all_items = []
columns = st.columns(len(uploaded_files)) if uploaded_files else []

for idx, uploaded_file in enumerate(uploaded_files):
    try:
        img = Image.open(uploaded_file)

        # Detect product and customer (same image for demo)
        product = detect_product(img)
        customer = detect_customer(img)

        # Generate bill for this item
        bill = generate_bill(product, customer)
        price = product.get("price", 0)
        total_price += price
        all_items.append((product, price))

        # Show image + details
        with columns[idx]:
            st.image(img, use_column_width=True)
            st.caption(f"{product['name']} - ${price}")

    except Exception as e:
        st.error(f"Error processing image: {str(e)}")

# Show total
if uploaded_files:
    st.markdown("---")
    st.subheader(f"🧾 Total Bill: ${total_price}")
