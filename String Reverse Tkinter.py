from tkinter import *

def reverseText(event):
    inVar = entry1.get()
    revVar = inVar[::-1]
    sum = 0
    for i in inVar:
        sum += int(i)

    if (inVar==revVar and int(inVar)==sum):
        p.set("Palindrom and Perfect")
    elif (inVar==revVar and int(inVar)!=sum):
        p.set("Palindrom not Perfect")
    elif (int(inVar)==sum and inVar!=revVar):
        p.set("Perfect not Palindrom")
    else:
        p.set("Nothing")
    v.set(revVar)

root = Tk()
frame1 = Frame()
frame1.pack(side=TOP, fill=X)
label1 = Label(frame1, text="Click the button to reverse", bg="white", fg="black", font=("Arial", 16))
button1 = Button(frame1, text="Reverse", bg="white", fg="black", font=("Arial", 16))
label1.grid(row=0)
button1.grid(row=2)
button1.bind("<Button-1>", reverseText)

entry1 = Entry(frame1)
entry1.grid(row=1)
v = StringVar()
p = StringVar()

label2 = Label(frame1, textvariable=v, fg="black", font=("Arial", 16))
label2.grid(row=3)

label3 = Label(frame1, textvariable=p, fg="black", font=("Arial", 16))
label3.grid(row=4)

root.mainloop()
