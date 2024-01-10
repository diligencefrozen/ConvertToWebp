import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def convert_to_webp(image_path):
    img = Image.open(image_path)
    file_name, file_extension = os.path.splitext(image_path)

    # Allow the user to select the storage location
    save_path = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WebP files", "*.webp")])
    if save_path:
        img.save(save_path, "WEBP")
        label_result.config(text=f"Conversion complete: {os.path.basename(save_path)}")
    else:
        label_result.config(text="Conversion cancelled")

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    if file_path:
        convert_to_webp(file_path)

# Tkinter Window Settings
root = tk.Tk()
root.title("ChangeToWebp")

# Title icon settings: Automatically load the icon from the same directory as the script
script_dir = os.path.dirname(os.path.realpath(__file__))
icon_path = os.path.join(script_dir, "ChangeToWebp.ico")
root.iconbitmap(icon_path)

# Window size settings
root.geometry("300x200")

# Layout Settings
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

# Welcome message
label_welcome = tk.Label(frame, text="Hello, User!\nUpload a file and I will convert it for you.", pady=10)
label_welcome.pack()

# Button to select an image
button_select = tk.Button(frame, text="Select an image", command=open_file_dialog)
button_select.pack()

# Label to show the result
label_result = tk.Label(frame, text="")
label_result.pack()

# Run Event Loop
root.mainloop()
