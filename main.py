import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import cv2

from add_images import add_image_and_copy
from inverse import inverse

def load_image(image_path, size):
    try:
        img = Image.open(image_path)
        img = img.resize(size, Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

image_path = None
def load_image_button_click():
    global image_path
    # Ask the user to select an image file
    image_path = filedialog.askopenfilename(title="Select an Image")
    if image_path:
        # Load the image and resize it for both the original and result
        original_image = load_image(image_path, (400, 225))
        if original_image:
            # Display the image in the original image label
            label_original_image.config(image=original_image)
            label_original_image.image = original_image  # Keep a reference
            
            # Initially, set the result image to be the same as the original image
            label_result_image.config(image=original_image)
            label_result_image.image = original_image  # Keep a reference

def save_result_image_button_click():
    if label_result_image.image:
        result_img = label_result_image.image._PhotoImage__photo  # Get the underlying PhotoImage object
        result_img.write(filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]), format="png")
    else:
        print("No result image to save!")

# Create the main application window
root = tk.Tk()
root.title("Image Processing")
root.geometry("1000x800")
root.resizable(False, False)  # Disable resizing

# Frame for buttons
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

# Function for button clicks
def on_button_click(btn_number):
    print(f"Button {btn_number} clicked!")
    
def update_result_image(function):
    result_image = function(image_path)
    if result_image is not None:
        # Resize the result image to 400x225
        result_image_resized = cv2.resize(result_image, (400, 225))
        # Convert and load the resized image for tkinter
        result_image_rgb = cv2.cvtColor(result_image_resized, cv2.COLOR_BGR2RGB)
        result_image_pil = Image.fromarray(result_image_rgb)
        result_image_tk = ImageTk.PhotoImage(result_image_pil)
        # Update the label with the resized result image
        label_result_image.config(image=result_image_tk)
        label_result_image.image = result_image_tk


# List of functions for buttons
functions = [
    {"title": "Image Operations", "name": "Invert Image", "function": lambda: update_result_image(inverse)},
    {"title": "Image Operations", "name": "Add Image", "function": lambda: update_result_image(add_image_and_copy)},
    {"title": "Image Operations", "name": "Subtract Image", "function": lambda: on_button_click(3)},
    {"title": "Basic Operations", "name": "Grayscale", "function": lambda: on_button_click(4)},
    {"title": "Basic Operations", "name": "Threshold", "function": lambda: on_button_click(5)},
    {"title": "Basic Operations", "name": "Halftone", "function": lambda: on_button_click(6)},
    {"title": "Histogram", "name": "Apply Histogram", "function": lambda: on_button_click(7)},
    {"title": "Histogram", "name": "Histogram Equalization", "function": lambda: on_button_click(8)},
    {"title": "Histogram", "name": "Manual Segmentation", "function": lambda: on_button_click(9)},
    {"title": "Histogram", "name": "Histogram Peak", "function": lambda: on_button_click(10)},
    {"title": "Histogram", "name": "Histogram Valley", "function": lambda: on_button_click(11)},
    {"title": "Histogram", "name": "Adaptive Histogram", "function": lambda: on_button_click(12)},
    {"title": "Filters", "name": "High-Pass", "function": lambda: on_button_click(13)},
    {"title": "Filters", "name": "Low-Pass", "function": lambda: on_button_click(14)},
    {"title": "Filters", "name": "Median", "function": lambda: on_button_click(15)},
    {"title": "Edge Detection", "name": "Sobel", "function": lambda: on_button_click(16)},
    {"title": "Edge Detection", "name": "Prewitt", "function": lambda: on_button_click(17)},
    {"title": "Edge Detection", "name": "Kirsch", "function": lambda: on_button_click(18)},
    {"title": "Advanced Edge Detection", "name": "Homogeneity", "function": lambda: on_button_click(19)},
    {"title": "Advanced Edge Detection", "name": "Difference op", "function": lambda: on_button_click(20)},
    {"title": "Advanced Edge Detection", "name": "Difference of Gaussian", "function": lambda: on_button_click(21)},
    {"title": "Advanced Edge Detection", "name": "AST based", "function": lambda: on_button_click(22)},
    {"title": "Advanced Edge Detection", "name": "Variance", "function": lambda: on_button_click(23)},
    {"title": "Advanced Edge Detection", "name": "Range op", "function": lambda: on_button_click(24)},
]

# Group buttons by title
grouped_buttons = {}
for func in functions:
    title = func["title"]
    if title not in grouped_buttons:
        grouped_buttons[title] = []
    grouped_buttons[title].append(func)

# Variables to track layout
current_column = 0
current_row = 0
filters_completed = False

# Create buttons dynamically under their titles
for title, buttons in grouped_buttons.items():
    # Create a label for the group title
    if title == "Edge Detection" and not filters_completed:
        filters_completed = True
        current_column += 1
        current_row = 0

    title_label = ttk.Label(button_frame, text=title, font=("Arial", 12, "bold"))
    title_label.grid(row=current_row, column=current_column, pady=(10, 5), sticky="w")
    current_row += 1

    # Add buttons for the group
    for btn_info in buttons:
        btn = ttk.Button(button_frame, text=btn_info["name"], command=btn_info["function"])
        btn.grid(row=current_row, column=current_column, padx=5, pady=2, sticky="w")
        current_row += 1

# Frame for images
image_frame = ttk.Frame(root)
image_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Add titles for the images
label_original_title = ttk.Label(image_frame, text="Original Image", font=("Arial", 14, "bold"))
label_original_title.pack(pady=5)

# Label for original image
label_original_image = tk.Label(image_frame)
label_original_image.pack(pady=10)

# Add title for result image
label_result_title = ttk.Label(image_frame, text="Result", font=("Arial", 14, "bold"))
label_result_title.pack(pady=5)

# Label for result image
label_result_image = tk.Label(image_frame)
label_result_image.pack(pady=10)

# Buttons to load and save images
load_button = ttk.Button(image_frame, text="Load Image", command=load_image_button_click)
load_button.pack(pady=5)

save_button = ttk.Button(image_frame, text="Save Image", command=save_result_image_button_click)
save_button.pack(pady=5)

# Run the application
root.mainloop()
