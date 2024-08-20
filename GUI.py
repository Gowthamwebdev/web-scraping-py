from tkinter import *   
import tkinter as tk  
from tkinter import ttk  
import pytesseract
import glob
import os
import cv2
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
 
  

    img = cv2.imread(filename)
    
    cv2.imshow("Input image",img)
    pytesseract.pytesseract.tesseract_cmd = r'D:\webscraping\Tesseract-OCR'
    s=pytesseract.image_to_string(filename)
    
    f=open("Text.doc","w")
    f.write(s)
    print("\n\nThese contents are saved to Text.doc in current working directory...!")
    f.close()
    # Insert The Fact.
    T.insert(tk.END, s)





root = Tk()

# specify size of window.
root.geometry("500x500")
root.config(background = "black")
# Create text widget and specify size.
T = Text(root, height = 20, width = 52)

# Create label
l = Label(root, text = "Text Predictor")
l.config(font =("Courier", 14))



# Create button for next text.
b1 = Button(root, text = "Browse", command = browseFiles)


# Create an Exit button.
b2 = Button(root, text = "Exit",
			command = root.destroy)


l.pack()
T.pack()
b1.pack()
b2.pack()




tk.mainloop()

