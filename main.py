from keras.models import load_model
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

model = load_model('Model\Model10Epochs30batch.h5')
FilePathTest = ""
ImageToAnalys = ""

def OpenFilePathTest():
    global FilePathTest 
    FilePathTest = filedialog.askopenfilename()
    print(FilePathTest)
    if FilePathTest != "":
        UpdateImage(FilePathTest)
