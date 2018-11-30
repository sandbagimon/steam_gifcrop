# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:41:56 2018

@author: sandb
"""

import tkinter as tk
from tkinter.filedialog import askopenfilename
from gif_crop import steamgif_crop

window = tk.Tk()  # 创建一个窗口
window.title('Steam创意工坊动态GIF分割器')
window.geometry('360x120+120+300')  # 窗口的位置以及大小
path = tk.StringVar()
filename =str()
def selectPath():
    global filename
    filename = askopenfilename(initialdir = "/",title = "选择你想切割的GIF图",filetypes = (("GIF图","*.gif"),("全部文件","*.*")))
    print(filename)
    path.set(filename)
    return 
def run():
    if filename == '':
        path.set('尚未选择图片')
    else:
        steamgif_crop(filename)
button_var = "选择图片路径"
entry = tk.Entry(window, textvariable =path,width=55)
button = tk.Button(window, text=button_var, width=10,
                   height=1, command=selectPath)

button2 = tk.Button(window, text='开始', width=10,
                   height=1, command=run)
button2.place(x=220, y=60)
entry.place(x=10,y=30)
button.place(x=40, y=60)



window.mainloop()
window.destroy()