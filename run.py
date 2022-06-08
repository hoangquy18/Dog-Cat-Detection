import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import ctypes
import os
from PIL import ImageTk, Image
from tkinter import messagebox  


ctypes.windll.shcore.SetProcessDpiAwareness(1)

# create the root window
root = tk.Tk()
root.geometry("720x720")
root.title("Khoanh vùng ảnh chó mèo")
panel = tk.Label(root, image='')

def openfile():
    filetypes = (
        ('images files', '*.png'),
        ('images files', '*.jpg'),
        ('images files', '*.jpeg'),
    )

    filename = fd.askopenfilename(title='open',filetypes=filetypes)
    if len(filename) == 0:
        messagebox.showwarning("warning","Vui lòng chọn file")
        filename = fd.askopenfilename(title='open')
        return

    exe = "python ./yolov5/detect.py --weights ./yolov5/runs/train/exp31/weights/best.pt --img 640 --conf 0.25 --source {}".format(filename)	
    os.system(exe)	
    os.system('quit()')
    
    return filename

def open_img():
    base_name = os.path.basename(openfile())
    x = "./yolov5/predicted/{}".format(base_name)
    img = Image.open(x)
    img = img.resize((640, 640), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    # panel = tk.Label(root, image=img)
    panel.image = img
    panel.config(image = img)
    panel.pack(side = "bottom", fill = "both", expand = "no")


if __name__ == "__main__":
    btn = tk.Button(root, text='open image', height = 2, 
            width = 20,command=open_img).pack()

    root.mainloop()
