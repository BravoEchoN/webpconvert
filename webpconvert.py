import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def convert_image(input_path, output_format):
    try:
        image = Image.open(input_path)
        output_path = os.path.splitext(input_path)[0] + '.' + output_format
        image.save(output_path, output_format.upper())
        return output_path
    except Exception as e:
        return str(e)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("WEBP files", "*.webp")])
    if file_path:
        input_path_var.set(file_path)

def convert_and_save():
    input_path = input_path_var.get()
    output_format = output_format_var.get().lower()
    
    if not input_path or not output_format:
        messagebox.showerror("Error", "Please select a file and output format.")
        return
    
    result = convert_image(input_path, output_format)
    
    if result.endswith(output_format):
        messagebox.showinfo("Success", f"File converted successfully: {result}")
    else:
        messagebox.showerror("Error", f"Conversion failed: {result}")

# GUI setup
root = tk.Tk()
root.title("WEBP to PNG/JPEG Converter")

input_path_var = tk.StringVar()
output_format_var = tk.StringVar()

tk.Label(root, text="Select WEBP file:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=open_file_dialog).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select output format:").grid(row=1, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="PNG", variable=output_format_var, value="png").grid(row=1, column=1, padx=10, pady=10, sticky="w")
tk.Radiobutton(root, text="JPEG", variable=output_format_var, value="jpeg").grid(row=1, column=1, padx=10, pady=10, sticky="e")

tk.Button(root, text="Convert", command=convert_and_save).grid(row=2, column=0, columnspan=3, padx=10, pady=20)

root.mainloop()
