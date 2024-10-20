import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

#READ!!!!
# make sure python environment is 3.11 or higher
# please make sure to run the following commands in terminal before: 
# pip install opencv-python
# pip install numpy
# pip install Pillow
# if that doesnt work still, then run these commands in terminal ...
# python3 -m pip install opencv-python
# python3 -m pip install numpy 
# python3 -m pip install Pillow

def imageLoader():
    global sketch, reference
    sketch_path = filedialog.askopenfilename(title="Select first image")
    reference_path = filedialog.askopenfilename(title="Select second image")
    sketch = cv2.imread(sketch_path)
    reference = cv2.imread(reference_path)
    sketch = cv2.resize(sketch, (500, 500))
    reference = cv2.resize(reference, (500, 500))
    showComparison()

def showComparison():
    global photo
    slider_pos = slider.get()
    combined = np.zeros((500, 500, 3), dtype=np.uint8)
    combined[:, :int(slider_pos * 5)] = sketch[:, :int(slider_pos * 5)]
    combined[:, int(slider_pos * 5):] = reference[:, int(slider_pos * 5):]
    
    cv2.line(combined, (int(slider_pos * 5), 0), (int(slider_pos * 5), 500), (0, 255, 0), 2)
    
    combined = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB)
    photo = ImageTk.PhotoImage(image=Image.fromarray(combined))
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

root = tk.Tk() #window popup & canvas
root.title("Image Comparison Slider")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=500, command=lambda x: showComparison())
slider.set(50)
slider.pack()

load_button = tk.Button(root, text="Load Images", command=imageLoader)
load_button.pack()

root.mainloop()
