from PIL import Image
import numpy as np
import os
import sys
import random
import tkinter
import cv2
import pandas as pd

def scale_to_siza(img, height):
    scale = height / img.shape[0]
    return cv2.size(img, dsize=None, fx=scale, fy=scale)

def ButtonEvent(event):
    #get photo list
    path=os.path.dirname(os.path.abspath(__file__))
    path2 = EditBox1.get()
    path2 = "/" + path2 + "/"
    path = path + path2
    dir0 = os.listdir(path)
    len0=len(dir0)
    dir1=[]
    for i in range(0, len0):
        name = dir0[i]
        if name.count(".jpg") + name.count(".png") + name.count(".jpg") + name.count(".png") != 0:
            dir1.append(name)
        else:
            pass
    #random choice of photo
    len1=len(dir1)
    n0 = random.randrange(0, len1)
    photo=dir1[n0]
    #open with OpenCV
    path=os.path.dirname(os.path.abspath(__file__))
    path = path + path2 + photo
    a=os.path.exists(path)
    if a==True :
            imgread = cv2.imread(path)
            #imgread = cv2.resize(imgread, (200,200))# サイズ変更
            if imgread.shape[0] > 1000:
                imgread = scale_to_height(imgread, 1000)
            elif imgread.shape[0] < 750:
                imgread = scale_to_height(imgread, 1000)
            #ウィンドウの表示形式の設定
            #第一引数：ウィンドウを識別するための名前
            #第二引数：ウィンドウの表示形式
            #cv2.WINDOW_AUTOSIZE：デフォルト。ウィンドウ固定表示
            #cv2.WINDOW_NORMAL：ウィンドウのサイズを変更可能にする
            #cv2.namedWindow("image", cv2.WINDOW_NORMAL)
            cv2.imshow("image",imgread)
            cv2.moveWindow("image",500,0)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            #log opened photo
            with open('history.csv', 'a') as f:
                f.write(path+"\n")
            EditBox2.delete(0,tkinter.END)
            EditBox2.insert(tkinter.END,"0")
    else :
        print("error")

def ButtonEvent2(event):
    #view backward using the log
    k=int(EditBox2.get())
    k=k+1
    list = pd.read_csv("history.csv", header=None)
    n = len(list)
    path = list.iat[n-1-k,0]
    if n > 10000000:
        with open("history.csv", "w") as f:
            f.write(path)
    imgread = cv2.imread(path)
    if imgread.shape[0] > 1000:
        imgread = scale_to_height(imgread, 1000)
    elif imgread.shape[0] < 750:
        imgread = scale_to_height(imgread, 1000)
    cv2.imshow("image",imgread)
    cv2.moveWindow("image",500,0)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    kstr=str(k)
    EditBox2.delete(0,tkinter.END)
    EditBox2.insert(tkinter.END,kstr)


root = tkinter.Tk()
root.title("Random photo")
root.geometry("200x320")

Static1 = tkinter.Label(text='folder name')
Static1.pack()
Static1.place(x=40, y=25)

EditBox1 = tkinter.Entry(width=20)
#EditBox1.insert(tkinter.END,"photo_test")
EditBox1.insert(tkinter.END,"2d")
EditBox1.place(x=40, y=50)

Static2 = tkinter.Label(text='back #')
Static2.pack()
Static2.place(x=40, y=75)

EditBox2 = tkinter.Entry(width=10)
EditBox2.insert(tkinter.END,"0")
EditBox2.place(x=40, y=100)

#左クリック（<Button-1>）されると，ButtonEvent関数を呼び出すようにバインド
Button1 = tkinter.Button(text='view', width=15)
Button1.bind("<Button-1>",ButtonEvent)
Button1.place(x=40, y=150)

Button3 = tkinter.Button(text='back', width=15)
Button3.bind("<Button-1>",ButtonEvent2)
Button3.place(x=40, y=200)

Button2 = tkinter.Button(text='exit',command=root.quit, width=15)
Button2.place(x=40, y=250)

root.mainloop()
