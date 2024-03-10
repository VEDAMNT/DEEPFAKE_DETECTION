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


root = tk.Tk()
root.title("DeepFakeDetector Version")
root.geometry("1440x920")
root.resizable(False, False)


background = tk.Frame(root, width=1440, height=920, bg="lightgrey")
background.grid(row=0, column=0)

Bg = Image.open("ImageRessource\Background.jpg")
Bg = Bg.resize((1440, 920)) 
Bg = ImageTk.PhotoImage(Bg)

LabelImageFrame = tk.Label(background, image=Bg)
LabelImageFrame.place(x=0, y=0)


menu = tk.Frame(background, width=1320, height=800, bg='white')
menu.grid(row=0, column=0)
menu.place(x=60, y=60)

TestLabelTitle = tk.Label(menu, text="! DeepfakeDetector !", font=("Arial", 20), bg="white")
TestLabelTitle.place(x = 50, y = 50)

Notice = tk.Label(menu, text="STEPS TO FOLLOW : ", font=("Arial", 15), bg="white")
Notice.place(x = 50, y = 150)

Instruction1 = tk.Label(menu, text="1. Select an image with the button < UPLOAD YOUR IMAGE >.", font=("Arial", 11), bg="white", fg="grey")
Instruction1.place(x = 50, y = 200)

Instruction2 = tk.Label(menu, text="2. Start the analysis with the button < START THE ANALYSIS >.", font=("Arial", 11), bg="white", fg="grey")
Instruction2.place(x = 50, y = 230)

Instruction3 = tk.Label(menu, text="3. The Model will tell you the interpretation of the image.", font=("Arial", 11), bg="white", fg="grey")
Instruction3.place(x = 50, y = 260)


ButtonPathTest = tk.Button(menu, text = "UPLOAD YOUR IMAGE", width=70, command = OpenFilePathTest, bg="#1E90FF", fg="white")
ButtonPathTest.place(x = 50, y = 680)

ButtonAnalyseTest = tk.Button(menu, text="START THE ANALYSIS", width = 70, command = lambda : Analyze(FilePathTest), bg="#1E90FF", fg="white")
ButtonAnalyseTest.place(x = 50, y = 726)

LabelReturn=tk.Label(menu,text ="",font=("Arial",31), bg="white")
LabelReturn.place(x = 50,y = 600)
ImageFrame = Image.open("ImageRessource\ImageCadre.jpg")
ImageFrame = ImageFrame.resize((600, 600)) 
tk_ImageFrame = ImageTk.PhotoImage(ImageFrame)
LabelImageFrame = tk.Label(menu, image=tk_ImageFrame)

LabelImageFrame.place(x=640, y= 100)


