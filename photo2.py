from PIL import Image
import numpy as np
import os
import matplotlib.pyplot as plt
import sys
import random
import tkinter
import cv2
import pandas as pd

def ButtonEvent(event):
    #get photo list
    path=os.path.dirname(os.path.abspath(__file__))
    #print(path)
    #path2 = input("type directory name:")
    path2 = EditBox1.get()
    path2 = "/" + path2 + "/"
    path = path + path2
    #print(path)
    #input()
    #exit()
    dir0 = os.listdir(path)
    len0=len(dir0)
    #print(dir0, dir0[0], len0)
    dir1=[]
    for i in range(0, len0):
        name = dir0[i]
        if name.count(".jpg") + name.count(".png") != 0:
            dir1.append(name)
        else:
            pass
    #print(dir1)
    len1=len(dir1)
    n0 = random.randrange(0, len1)
    photo=dir1[n0]
    #print(photo)

    #sys.exit()

    #path=input("Input file name: ")
    path=os.path.dirname(os.path.abspath(__file__))
    #print(path)
    path = path + path2 + photo
    #print(path)
    a=os.path.exists(path)
    if a==True :
            #img = Image.open(path)
            #img.show()
            #img_list = np.asarray(img)
            #img_list = np.array(img)
            #print(img_lis)
            #plt.imshow(img_list)
            #plt.show()
            imgread = cv2.imread(path)
            #img = cv2.resize(imgread, (200,200))# サイズ変更
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
            with open('history.csv', 'a') as f:
                f.write(path+"\n")
            EditBox2.delete(0,tkinter.END)
            EditBox2.insert(tkinter.END,"0")
    else :
        print("error")

def ButtonEvent2(event):
    k=int(EditBox2.get())
    k=k+1
    #print(k)
    list = pd.read_csv("history.csv", header=None)
    #print(list)
    n = len(list)
    #print(n)
    #print(list.loc[[n-1-k],[0]])
    path = list.iat[n-1-k,0]
    #print(path)
    #input()
    imgread = cv2.imread(path)
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
