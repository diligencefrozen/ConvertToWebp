import tkinter as tk
from tkinter import filedialog, messagebox, Menu
from PIL import Image
import os
import webbrowser

def convert_to_webp(image_path):
    # Open the image and split the file name and extension
    img = Image.open(image_path)
    file_name, file_extension = os.path.splitext(image_path)

    # Allow the user to select the storage location
    save_path = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WebP files", "*.webp")])
    if save_path:
        # Save the image in WebP format
        img.save(save_path, "WEBP")
        label_result.config(text=f"Conversion complete: {os.path.basename(save_path)}")
    else:
        label_result.config(text="Conversion cancelled")

def open_file_dialog():
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        convert_to_webp(file_path)

def show_about():
    # Show information about the program and open the GitHub link
    messagebox.showinfo("About ChangeToWebp", "ChangeToWebp Version 20240110.2\n"
                                              "Convert your images to WebP format easily.\n\n"
                                              "GitHub: https://github.com/diligencefrozen/ChangeToWebp")
    webbrowser.open("https://github.com/diligencefrozen/ChangeToWebp")

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

# Create a menu
menu = Menu(root)
root.config(menu=menu)

# Add a "File" menu
file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="About", command=show_about)

# Run Event Loop
root.mainloop()
