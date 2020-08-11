from tkinter import *
import tkinter.ttk as ttk 
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image , ImageDraw ,ImageGrab , ImageTk 
from tkinter import messagebox

root = Tk()
root.title("Paint Clone")
root.geometry("800x800")

brush_color = "black"

def Paint(e):
    
    Brush_width = '%0.0f' % float(my_slider.get())
    brush_type2 = brush_type.get() #ROUND,PROJECTING
    
    x1 = e.x - 3
    y1 = e.y - 3 

    x2 = e.x + 3
    y2 = e.y + 3

    my_canvas.create_line(x1,y1,x2,y2,fill = brush_color,width = Brush_width,capstyle = brush_type2,smooth = True)

def chage_brush_size(thing):
    sliderLabel.config(text ='%0.0f' % float(my_slider.get()))

def change_brush_color():
    global brush_color 
    brush_color = colorchooser.askcolor(color=brush_color)[1]

def change_canvas_color():
    global bg_color 
    bg_color = "white"
    bg_color = colorchooser.askcolor(color=bg_color)[1]
    my_canvas.config(bg = bg_color)

def clear_screen():
    my_canvas.delete(ALL)
    my_canvas.config(bg = "white")

def clear_cancvas():
    my_canvas.delete(ALL)

def save():
    result = filedialog.asksaveasfilename(initialdir = "c:",filetypes = (("png files","*.png"),("all files","*.*")))

    if result.endswith(".png"):
        pass
    else :
        result += ".png"

    x = root.winfo_rootx()+my_canvas.winfo_x()
    y = root.winfo_rooty()+my_canvas.winfo_y()
    x1 = x + my_canvas.winfo_width()
    y1 = y + my_canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(result)

    messagebox.showinfo("image saved","Your image has been suscessfully saved!")

w = 600
h = 400
my_canvas = Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=20) 

my_canvas.bind("<B1-Motion>" , Paint)

brush_option_frame = Frame(root)#bg = "red"
brush_option_frame.pack(pady=20)

brush_size_frame = LabelFrame(brush_option_frame,text = "Brush Size")
brush_size_frame.grid(row = 0,column = 0,padx = 50)

my_slider = ttk.Scale(brush_size_frame,from_ = 1,to = 100,orient = VERTICAL,value = 10, command = chage_brush_size)
my_slider.pack(pady = 10,padx = 10)

sliderLabel = Label(brush_size_frame,text = my_slider.get())
sliderLabel.pack(pady = 5)

brush_type_frame = LabelFrame(brush_option_frame,text = "Brush type")
brush_type_frame.grid(row = 0,column = 1,padx = 50)

brush_type = StringVar()
brush_type.set("round")

Radiobutton1 = Radiobutton(brush_type_frame,text = "Round",value = "round",variable = brush_type)
Radiobutton2 = Radiobutton(brush_type_frame,text = "Slash",value = "butt",variable = brush_type)
Radiobutton3 = Radiobutton(brush_type_frame,text = "Dimaond",value = "projecting",variable = brush_type)

Radiobutton1.pack(anchor = W)
Radiobutton2.pack(anchor = W)
Radiobutton3.pack(anchor = W)

change_color_frame = LabelFrame(brush_option_frame,text = "Change Color")
change_color_frame.grid(row = 0,column = 2)

brush_color_button = Button(change_color_frame,text = "Change Brush Color",command = change_brush_color)
brush_color_button.pack(pady = 10,padx = 10)

canvas_color_button = Button(change_color_frame,text = "Change canvas Color",command = change_canvas_color)
canvas_color_button.pack(pady = 10,padx = 10)

options_menu = LabelFrame(brush_option_frame,text = "Preferances")
options_menu.grid(row = 0,column =3, padx = 50)

clear_button = Button(options_menu,text = "clear screen",command = clear_screen)
clear_button.pack(padx = 10, pady = 10)

canvas_button = Button(options_menu,text = "clear canvas",command = clear_cancvas)
canvas_button.pack(padx = 10, pady = 10)

save_image = Button(options_menu,text = "save as png",command = save)
save_image.pack(padx = 10, pady = 10)

root.mainloop()