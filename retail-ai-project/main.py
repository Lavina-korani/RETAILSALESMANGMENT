# main.py
import tkinter as tk
from tkinter import filedialog, messagebox
from detection import detect_product, detect_customer
from billing import generate_bill
from database import connect_db

connect_db()

app = tk.Tk()
app.title("Retail Sales Management AI")
app.geometry("400x400")

def select_product_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        product = detect_product(file_path)
        customer = detect_customer(file_path)  # assuming customer image same for demo
        bill = generate_bill(product, customer)
        messagebox.showinfo("Bill Generated", bill)

title = tk.Label(app, text="Retail Sales Management", font=("Arial", 16))
title.pack(pady=20)

btn = tk.Button(app, text="Upload Product Image", command=select_product_image, font=("Arial", 14), bg="lightblue")
btn.pack(pady=40)

app.mainloop()
