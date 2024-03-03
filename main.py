from keras.models import load_model

model = load_model('Model\Model10Epochs30batch.h5')
FilePathTest = ""
ImageToAnalys = ""

def OpenFilePathTest():
    global FilePathTest 
    FilePathTest = filedialog.askopenfilename()
    print(FilePathTest)
    if FilePathTest != "":
        UpdateImage(FilePathTest)
