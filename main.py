import numpy as np
import cv2
import os
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk 
import shutil

prototxt = r'model/colorization_deploy_v2.prototxt'
model = r'model/colorization_release_v2.caffemodel'
points = r'model/pts_in_hull.npy'
points = os.path.join(os.path.dirname(__file__), points)
prototxt = os.path.join(os.path.dirname(__file__), prototxt)
model = os.path.join(os.path.dirname(__file__), model)

def check_model_file():
    if not os.path.isfile(model):
        messagebox.showerror('Missing model file', 'You are missing the file "colorization_release_v2.caffemodel"\n'
                             'Download it and place it into your "model" folder.\n'
                             'You can download this file from this location:\n'
                             'https://www.dropbox.com/s/dx0qvhhp5hbcx7z/colorization_release_v2.caffemodel?dl=1')
        exit()

check_model_file()
folder_path = "temp"
if os.path.exists(folder_path) and os.path.isdir(folder_path):
    shutil.rmtree(folder_path)
    print("removed")
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f'Folder {folder_path} has been created.')
    else:
        print(f'Folder {folder_path} already exists.')
prototxt = os.path.join(os.path.dirname(__file__), prototxt)
model = os.path.join(os.path.dirname(__file__), model)
points = os.path.join(os.path.dirname(__file__), points)

net = cv2.dnn.readNetFromCaffe(prototxt, model)
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")

pts = np.load(points)
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]
cv2_frame = 0
def colorize(l, image, lab):
    net.setInput(cv2.dnn.blobFromImage(l))
    ab = net.forward()[0].transpose((1, 2, 0))
    ab = cv2.resize(ab, (image.shape[1], image.shape[0]))
    L = cv2.split(lab)[0]
    colorized = np.concatenate((L[:, :, np.newaxis], ab), axis=2)
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    return colorized


def colorize_photo():
    # print(in_file_entry)
    if in_file_entry.get():
        filename = in_file_entry.get()
        print(filename)
        image = cv2.imread(filename) if filename else cv2_frame
        scaled = image.astype("float32") / 255.0
        lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
        resized = cv2.resize(lab, (224, 224))
        L = cv2.split(resized)[0]
        li = [50, 49, 48, 51, 52, 53] #[50, 48, 45, 55, 53, 58]
        # L -= 50
        'print("[INFO] colorizing image...")'
        for i in li:
            L -= i
            coloriz = colorize(L, image, lab)
            cv2.imwrite(f'temp/output{li.index(i)+1}.png', coloriz)
        for i in range(1,7):
            img = cv2.imread(f'temp/output{i}.png')
            resiz = cv2.resize(img, (349, 243))
            cv2.imwrite(f'temp/outputr{i}.png', resiz)
            if i==1:
                outputi = PhotoImage(file="temp/outputr1.png")
                output1.config(image=outputi)
                output1.image = outputi
            elif i==2:
                outputi = PhotoImage(file="temp/outputr2.png")
                output2.config(image=outputi)
                output2.image = outputi
            elif i==3:
                outputi = PhotoImage(file="temp/outputr3.png")
                output3.config(image=outputi)
                output3.image = outputi
            elif i==4:
                outputi = PhotoImage(file="temp/outputr4.png")
                output4.config(image=outputi)
                output4.image = outputi
            elif i==5:
                outputi = PhotoImage(file="temp/outputr5.png")
                output5.config(image=outputi)
                output5.image = outputi
            else:
                outputi = PhotoImage(file="temp/outputr6.png")
                output6.config(image=outputi)
                output6.image = outputi

def browse_file():
    file =  filedialog.askopenfilename()
    print(file)
    in_file_entry.delete(0, 'end')
    in_file_entry.insert(0, file)
    img = cv2.imread(file)
    resiz = cv2.resize(img, (349, 243))
    cv2.imwrite('temp/input.png', resiz)
    inputi = PhotoImage(file="temp/input.png")
    inputt.config(image=inputi)
    inputt.image = inputi
save=0
def image1():
    global save
    print(1)
    save=1
    print(save)
def image2():
    global save
    save=2
    print(2)
    print(save) 
def image3():
    global save
    save=3
    print(save)
    print(3)
def image4():
    global save
    save=4
    print(save)
    print(4)
def image5():
    global save
    save=5
    print(save)
    print(5)
def image6():
    global save
    save=6
    print(6)
    print(save)

def save_file():
    file_extension = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    print(save)
    if file_extension:
        print(save)
        if save==2:
        # cv2.imwrite(file_extension, cv2.cvtColor(output_image_label.cget("image"), cv2.COLOR_RGB2BGR))
            img = cv2.imread("temp/output2.png")
            cv2.imwrite(file_extension, img)
            messagebox.showinfo('Image Saved', 'Image save complete')
        elif save==3:
            img = cv2.imread("temp/output3.png")
            cv2.imwrite(file_extension, img)
            messagebox.showinfo('Image Saved', 'Image save complete')
        elif save==4:
            img = cv2.imread("temp/output4.png")
            cv2.imwrite(file_extension, img)
            messagebox.showinfo('Image Saved', 'Image save complete')
        elif save==5:
            img = cv2.imread("temp/output5.png")
            cv2.imwrite(file_extension, img)
            messagebox.showinfo('Image Saved', 'Image save complete')
        elif save==6:
            img = cv2.imread("temp/output6.png")
            cv2.imwrite(file_extension, img)
            messagebox.showinfo('Image Saved', 'Image save complete')
        else:
            img = cv2.imread("temp/output1.png")
            cv2.imwrite(file_extension, img)
            messagebox.showinfo('Image Saved', 'Image save complete')

def web_cam():
    os.system('python webcam.py')

root = tk.Tk()
root.title("E3 Colorizer") 
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


root.geometry(f"{screen_width}x{screen_height}")
# root.geometry("1440x1024")
background_image = PhotoImage(file="source/color.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
texti = PhotoImage(file="source/text.png")
textf = tk.Label(root, image=texti ,width=391, height=40, borderwidth=0)
textf.place(x=191, y=258)
# textbi = PhotoImage(file="textb.png")
in_file_entry = tk.Entry(textf, width=391, bg = "#1E80FF")#, bg="#FFFFFF00"#36475A
in_file_entry.place(x=0, y=0,relwidth=1, relheight=1)


browi = PhotoImage(file="source/brow.png")
browf = tk.Frame(root, width=124, height=40)
browf.place(x=673, y=258)
# brow=tk.Button(browf, image=browi, command=lambda: in_file_entry.insert(0, filedialog.askopenfilename()), borderwidth=0, bg="#8ACEFF") #012136
brow=tk.Button(browf, image=browi, command=browse_file, borderwidth=0, bg="#8ACEFF") 
brow.place(x=0, y=0, relwidth=1, relheight=1)

# in_file_entry = tk.Entry(root, width=25)


colori = PhotoImage(file="source/colori.png")
colorf = tk.Frame(root, width=185, height=40)
colorf.place(x=892, y=258)
color=tk.Button(colorf, image=colori, command=colorize_photo, borderwidth=0, bg="#8ACEFF") #012136
color.place(x=0, y=0, relwidth=1, relheight=1)

cami = PhotoImage(file="source/cam.png")
camf = tk.Frame(root, width=185, height=40)
camf.place(x=1163, y=258)
cam=tk.Button(camf, image=cami, command=web_cam, borderwidth=0, bg="#8ACEFF") #012136
cam.place(x=0, y=0, relwidth=1, relheight=1)

savei = PhotoImage(file="source/save.png")
savef = tk.Frame(root, width=185, height=40)
savef.place(x=1423, y=258)
saveg=tk.Button(savef, image=savei, command=save_file, borderwidth=0, bg="#8ACEFF") #012136
saveg.place(x=0, y=0, relwidth=1, relheight=1)

inputi = PhotoImage(file="source/input.png")
inputf = tk.Frame(root, width=349, height=233)
inputf.place(x=126, y=537)
inputt=tk.Button(inputf, image=inputi, command=image1, borderwidth=0, bg="#8ACEFF") 
inputt.place(x=0, y=0, relwidth=1, relheight=1)

output1i = PhotoImage(file="source/img1.png")
output1f = tk.Frame(root, width=349, height=233)
output1f.place(x=531, y=404)
output1=tk.Button(output1f, image=output1i, command=image1, borderwidth=0, bg="#8ACEFF") 
output1.place(x=0, y=0, relwidth=1, relheight=1)

output2i = PhotoImage(file="source/img2.png")
output2f = tk.Frame(root, width=349, height=233)
output2f.place(x=963, y=404)
output2=tk.Button(output2f, image=output2i, command=image2, borderwidth=0, bg="#8ACEFF") 
output2.place(x=0, y=0, relwidth=1, relheight=1)

output3i = PhotoImage(file="source/img3.png")
output3f = tk.Frame(root, width=349, height=233)
output3f.place(x=1398, y=404)
output3=tk.Button(output3f, image=output3i, command=image3, borderwidth=0, bg="#8ACEFF") 
output3.place(x=0, y=0, relwidth=1, relheight=1)

output4i = PhotoImage(file="source/img4.png")
output4f = tk.Frame(root, width=349, height=233)
output4f.place(x=531, y=685)
output4=tk.Button(output4f, image=output4i, command=image4, borderwidth=0, bg="#8ACEFF") 
output4.place(x=0, y=0, relwidth=1, relheight=1)

output5i = PhotoImage(file="source/img5.png")
output5f = tk.Frame(root, width=349, height=233)
output5f.place(x=963, y=685)
output5=tk.Button(output5f, image=output5i, command=image5, borderwidth=0, bg="#8ACEFF") 
output5.place(x=0, y=0, relwidth=1, relheight=1)

output6i = PhotoImage(file="source/img6.png")
output6f = tk.Frame(root, width=349, height=233)
output6f.place(x=1398, y=685)
output6=tk.Button(output6f, image=output6i, command=image6, borderwidth=0, bg="#8ACEFF") 
output6.place(x=0, y=0, relwidth=1, relheight=1)


root.attributes('-fullscreen', True)
icon = PhotoImage(file="source/save.png")
root.iconphoto(True, icon)
# front_page = mainpage(root)
root.mainloop()
