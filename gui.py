# -*- coding = utf-8 -*-
# @Time :2020/8/27 10:13
# @Author :LiBai
# @File : gui.py
from tkinter import *
from tkinter import messagebox

i = 0
while True:
    root = Tk()
    root.title('我的第一个gui')
    root.geometry("300x200+100+200")

    btn01 = Button(root)
    btn01['text'] = '等我'
    btn01.pack()

nihao
    def dj(e):
        messagebox.showinfo('Message', '很好，你等了')


    btn01.bind('<Button-1>', dj)

    root.mainloop()
    i += 1
    if i == 20:
        exit(0)
