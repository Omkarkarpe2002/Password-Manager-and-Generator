from tkinter import *
import random
from PIL import Image, ImageTk
import tkinter.messageboxpip

window = Tk()
window.geometry("550x700")
window.minsize(500,460)
window.title("Random Password Generator")
window.configure(bg="slategray")   

image=Image.open("pass1.jpg")
photo= ImageTk.PhotoImage(image)

pass1_label=Label(image=photo)
pass1_label.pack(pady=20)

cond1 = IntVar()
cond2 = IntVar()
cond3 = IntVar()
cond4 = IntVar()
length = IntVar()

# charecter lists
list_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']
list_2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
          'W', 'X', 'Y', 'Z']
list_3 = ['!', '@', '#', '$', '%', '^', '&', '*']
list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# function to generate password
def password():
    
    final_list = []
    ln = length.get()
    if (cond3.get()):
        final_list.append(list_1)
    if (cond4.get()):
        final_list.append(list_2)
    if (cond2.get()):
        final_list.append(list_3)
    if (cond1.get()):
        final_list.append(list_4)
    bound = cond1.get() + cond2.get() + cond3.get() + cond4.get()
    if not (bound):
        return ("Nothing selected")
    password = []
    for i in range(ln):
        if (i == 0):
            a = 1
        else:
            a = random.randint(1, bound)
        k = final_list[a - 1]
        b = random.randint(0, len(k) - 1)
        password.append(str(k[b]))
    return (''.join(password))
    
# gloabal password variable
pswrd = StringVar()
pswrd.set(password())
txt_1 = Entry(window, textvariable=pswrd, font=("ComicSansMS", 14),bd=5,bg="red")

# function to display generated password
def display_password():
    global txt_1
    txt_1.pack_forget()
    pswrd.set(password())
    txt_1 = Entry(window, textvariable=pswrd, font=("ComicSansMS", 14),bd=5,bg="gray")
    txt_1.pack()
    
def clipper():
    window.clipboard_clear()
    window.clipboard_append(txt_1.get())
    tkinter.messagebox.showinfo( "Successful", "Your password is successfully copied to clipboard..!")


slider_1 = tkinter.Scale(window, variable=length, orient=HORIZONTAL, label="Set length of password", 
                         font="Helvetica 10 bold",bg="gray",length=200,
                         from_=6, to=30)
slider_1.pack(pady=10,padx=60)


label_2 = tkinter.Label(window, 
                text="Select the type of password you want\n(For strong password select atleast 2 options)\n",
                        font="ComicSansMS 10 bold",bg="slategray")
label_2.pack(pady=10)


# creating gui components
chkbutton_1 = tkinter.Checkbutton(window, text='Numbers', variable=cond1, onvalue=1, offvalue=0,font="helvetica 10 bold",bg="ivory")
chkbutton_2 = tkinter.Checkbutton(window, text='Special Characters', variable=cond2, onvalue=1, offvalue=0,font="helvetica 10 bold",bg="ivory")
chkbutton_3 = tkinter.Checkbutton(window, text='Small Letters', variable=cond3, onvalue=1, offvalue=0,font="helvetica 10 bold",bg="ivory")
chkbutton_4 = tkinter.Checkbutton(window, text='Capital Letters', variable=cond4, onvalue=1, offvalue=0,font="helvetica 10 bold",bg="ivory")

# run created components
chkbutton_1.pack(pady=10)
chkbutton_2.pack(pady=10)
chkbutton_3.pack(pady=10)
chkbutton_4.pack(pady=10)

# Create a frame for our Buttons
my_frame = Frame(window, borderwidth=2,bg="slategray")
my_frame.pack(pady=20)

# Create our Buttons
my_button = Button(my_frame, text="Generate Password", command=display_password, bg="light yellow", fg="red")
my_button.grid(row=0, column=0, padx=10)

clip_button = Button(my_frame, text="Copy To Clipboard", command=clipper, bg="light yellow", fg="red")
clip_button.grid(row=0, column=1, padx=10)

window.mainloop()