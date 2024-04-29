
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

window = Tk()
window.title('Login System of Student Management System')


def login():
    if username_entry.get() == '' or password_entry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif username_entry.get() == 'Arya' and password_entry.get() == '1234':
        messagebox.showinfo('Welcome', 'Login successful!')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error', 'Please enter correct data')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

imgTemp = Image.open("BG7.jpg")
img2 = imgTemp.resize((width, height))
background_img = ImageTk.PhotoImage(img2)

background_label = Label(window, image=background_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

loginFrame = Frame(window, bg='white', bd=2, relief=SOLID)
loginFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

original_logo_image = Image.open('logo.png')
resized_logo_image = original_logo_image.resize((200, 200))
logo_img = ImageTk.PhotoImage(resized_logo_image)

logo_label = Label(loginFrame, image=logo_img, bg='white')
logo_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

original_username_image = Image.open('user.png')
resized_username_image = original_username_image.resize((30, 30))
username_img = ImageTk.PhotoImage(resized_username_image)

username_label = Label(loginFrame, image=username_img, text='Username:', compound='left', font=('Arial', 14), bg='white')
username_label.grid(row=1, column=0, padx=10, pady=5, sticky='w')

username_entry = Entry(loginFrame, font=('Arial', 14), bd=2)
username_entry.grid(row=1, column=1, padx=10, pady=5, sticky='e')

original_pass_image = Image.open('eye.png')
resized_pass_image = original_pass_image.resize((30, 30))
pass_img = ImageTk.PhotoImage(resized_pass_image)

password_label = Label(loginFrame, image=pass_img, text='Password:', compound='left', font=('Arial', 14), bg='white')
password_label.grid(row=2, column=0, padx=10, pady=5, sticky='w')

password_entry = Entry(loginFrame, font=('Arial', 14), bd=2, show='*')
password_entry.grid(row=2, column=1, padx=10, pady=5, sticky='e')

login_button = Button(loginFrame, text='Login', font=('Arial', 14, 'bold'), bg='#4CAF50', fg='white', bd=2, relief=RAISED, width=15, pady=8, command=login)
login_button.grid(row=3, columnspan=2, pady=(20, 10))

forgot_password_button = Button(loginFrame, text='Forgot Password?', font=('Arial', 12), bg='#2196F3', fg='white', bd=2, relief=RAISED, width=15)
forgot_password_button.grid(row=4, columnspan=2, pady=(0, 20))

window.mainloop()