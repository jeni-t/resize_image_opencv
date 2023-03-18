import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from functools import partial
import random
import array
root = tk.Tk()
root.title("image resize")
root.geometry('320x150')

def call_result(label_result, n1, label_result1, n2):

    width = number1.get()
    print(width,"width")
    height = number2.get()
    print(height,"height")
    img = cv2.imread('jeni.jpg')
    #, w, c = img.shape
    #print(f"Height and width of original image: {h}, {w}" )

    # resize the image
    #new_size = (200, 250) #
    new_size=(width, height)
    print(f"New height and width: {new_size[1]}, {new_size[0]}" )
    resize_img = cv2.resize(img, new_size)

    # Convert the images from BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resize_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)
    cv2.imwrite("resize_image.jpg", resize_img)

    plt.subplot(121),plt.imshow(img), plt.title("Original Image")
    plt.subplot(122), plt.imshow(resize_img), plt.title("Resized Image")
    plt.show()
    
number1 = tk.IntVar()   
number2 = tk.IntVar()
#number2 = tk.IntVar()

labelNum1 = tk.Label(root, font=('arial',12,'bold'),text="width").grid(row=1, column=0)  
labelResult = tk.Label(root)  
labelResult.grid(row=1, column=3)

labelNum2 = tk.Label(root, font=('arial',12,'bold'),text="height").grid(row=2, column=0)  
labelResult1 = tk.Label(root)  
labelResult1.grid(row=2, column=3)

entryNum1 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number1,width=15,bg="#eee",bd=5).grid(row=1, column=2)  
call_result = partial(call_result, labelResult, number1)

entryNum2 = tk.Entry(root, font=('arial',14,'bold'), textvariable=number2,width=15,bg="#eee",bd=5).grid(row=2, column=2)  
call_result = partial(call_result, labelResult1, number2)

buttonCal = tk.Button(root, text="Result", width=10,command=call_result).grid(row=3, column=0)
