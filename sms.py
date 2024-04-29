from tkinter import*
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

def iexit():
    result=messagebox.askyesno('confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        #one by one all rows will be printed
        content=studentTable.item(index)
        datalist=content['values']
        print(datalist)
        newlist.append(datalist)
        #dataframe from pandas will help to convert it into tabular form
        #and it ll store values into table
    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')


def toplevel_data(title, button_text, command):
    global idEntry, mobileEntry, nameEntry, emailEntry, addressEntry, genderEntry, dobEntry, screen
    screen = Toplevel()
    screen.grab_set()
    screen.resizable(False, False)
    screen.title(title)

    # Entry fields for search criteria...
    screen_button = ttk.Button(screen, text='Update STUDENT', command=command)
    screen_button.grid(row=7, columnspan=2, pady=15)

    # ID
    idLabel = Label(screen, text='ID', font=('new times roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, stick=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    # Name
    nameLabel = Label(screen, text='Name', font=('new times roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, stick=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    # Mobile Number
    mobileLabel = Label(screen, text='Mobile Number', font=('new times roman', 20, 'bold'))
    mobileLabel.grid(row=2, column=0, padx=30, pady=15, stick=W)
    mobileEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, pady=15, padx=10)

    # Email
    emailLabel = Label(screen, text='Email', font=('new times roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, stick=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    # Address
    addressLabel = Label(screen, text='Address', font=('new times roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, stick=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    # Gender
    genderLabel = Label(screen, text='Gender', font=('new times roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, stick=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    # Date of Birth
    dobLabel = Label(screen, text='Date of Birth', font=('new times roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, stick=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=7, columnspan=2, pady=15)

    if title == 'Update Student':
        indexing = studentTable.focus()
        content = studentTable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        mobileEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])

        # Assuming date and currenttime are defined elsewhere in your code



'''def update_data():
    query = 'update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query, (
    nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(),
    date, currenttime, idEntry.get()))
    con.commit()
    messagebox.showinfo('Success', f'Id{idEntry.get()}is modified successfully', parent=screen)
    screen.destroy()
    show_student()'''


def show_student():
    query = 'select * from student'
    mycursor.execute(query)  # Pass the query to execute
    fetch_data = mycursor.fetchall()
    for data in fetch_data:
        studentTable.insert('', END, values=data)
'''def update_data():
    global currentdate, currenttime  # Ensure these variables are global
    currentdate = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')  # Corrected format
    
    query = 'update student set id=%s, name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
    mycursor.execute(query, (
        idEntry.get(),nameEntry.get(), mobileEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(),
        dobEntry.get(), currentdate, currenttime, idEntry.get()))
    con.commit()
    messagebox.showinfo('Success', f'Id {idEntry.get()} is modified successfully', parent=screen)
    screen.destroy()
    show_student()
'''





def delete_student():
    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM student WHERE id=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')

    # Clear the studentTable before inserting new data
    studentTable.delete(*studentTable.get_children())

    # Fetch and insert updated data into the table
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetch_data = mycursor.fetchall()
    for data in fetch_data:
        studentTable.insert('', END, values=data)

'''def delete_student():
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    # print(content)
    content_id = content['values'][0]
    query = 'delete from student where id=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')

    mycursor.execute(query='select * from student')
    fetch_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)'''


def search_data():
    query = 'select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query, (idEntry.get(), nameEntry.get(), emailEntry.get(), mobileEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.grab_set()
    search_window.resizable(False, False)
    search_window.destroy()

'''def search_data():
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),mobileEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get() ))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('',END,values=data)


    search_window = Toplevel()
    # to first i need only to graab only add student window and non other
    search_window.grab_set()
    search_window.resizable(False, False)'''





def add_data():
    try:
        if idEntry.get() == '' or nameEntry.get() == '' or mobileEntry.get() == '' or emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('error', 'All fields should be filled', parent=add_window)
    finally:
        currentdate = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%H:%H:%S')
        query = 'INSERT INTO student VALUES (%s, %s, %s , %s, %s, %s, %s, %s, %s)'

        mycursor.execute(query, (idEntry.get(), nameEntry.get(), mobileEntry.get(), emailEntry.get(),
                                 addressEntry.get(), genderEntry.get(), dobEntry.get(), currentdate, currenttime))
        # if i manipulate the data i have to use commit
        con.commit()

        result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?')
        if result:
            idEntry.delete(0, 'end')
            nameEntry.delete(0, 'end')
            mobileEntry.delete(0, 'end')
            emailEntry.delete(0, 'end')
            addressEntry.delete(0, 'end')
            genderEntry.delete(0, 'end')
            dobEntry.delete(0, 'end')
        else:
            pass

    add_window = Toplevel()
    # to first i need only to graab only add student window and non other
    add_window.grab_set()
    add_window.resizable(False, False)

    add_window.title("Add Student")
    add_window.destroy()



def connect_database():
    def connect():
        non_comment_string = "#0910Em@!"
        #making con variable global if i want to change some data externally
        global mycursor, con
        try:
            con = pymysql.connect(host='localhost', user='root', password=non_comment_string)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Data', parent=connectWindow)
            return

        try:
            query='create database SMS'
            mycursor.execute(query)
            query='use SMS'
            mycursor.execute(query)
            query = ('CREATE TABLE student ('
                     'id INT NOT NULL PRIMARY KEY,'
                     'name VARCHAR(30),'
                     'mobile INT(10),'
                     'email VARCHAR(30),'
                     'address VARCHAR(100),'
                     'gender VARCHAR(20),'
                     'DOB VARCHAR(20),'
                     'date VARCHAR(50),'
                     'time VARCHAR(50)'
                     ')')
            #(#0910Em@!)
            mycursor.execute(query)
        except:
            query = 'use SMS'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
      #enabling buttons after connection is successful
        connectWindow.destroy()
        #code to enable button after database is connected
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        exportDataButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)



    connectWindow = Tk()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnameLabel = ttk.Label(connectWindow, text='Host Name', font=('Arial', 20, 'bold'))
    hostnameLabel.grid(row=0, column=0)

    hostEntry = ttk.Entry(connectWindow, font=('roman', 15, 'bold'))
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    usernameLabel = ttk.Label(connectWindow, text='Username', font=('Arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0)

    usernameEntry = ttk.Entry(connectWindow, font=('roman', 15, 'bold'))
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = ttk.Label(connectWindow, text='Password', font=('Arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0)

    passwordEntry = ttk.Entry(connectWindow, font=('roman', 15, 'bold'))
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)



#defining fu
# nction
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]#S
    sliderLabel.config(text=text)
    count+=1
    #every time 0.3sec slider function gets called
    sliderLabel.after(300,slider)
def clock():
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    #fstring method used to concatenete two string
    datetimeLabel.config(text=f'Date:{date}\nTime:{currenttime}')
    #after every 1000ms the second is getting updated
    datetimeLabel.after(1000,clock)

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry(('1600x800'))
root.title('student management system')

datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
#calling function
clock()

s='Student Management System'
#s[count]=t when count is 1
sliderLabel=Label(root,font=('times new roman',30,'italic bold'),width=30)
sliderLabel.place(x=500,y=20)
slider()

connectButton=ttk.Button(root,text='Connect Database',command=connect_database)
connectButton.place(x=1350, y=15)

#lets create leftframe

leftFrame=Frame(root)
leftFrame.place(x=50,y=100,width=300,height=600)

logo_Image=PhotoImage(file='logo1.png')
#i am making logoimage as a label of left frame
logo_Label=Label(leftFrame,image=logo_Image)
logo_Label.grid(row=0,column=0,pady=12)

addstudentButton=ttk.Button(leftFrame,text='Add student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add ',add_data))
addstudentButton.grid(row=1,column=0,pady=12)

searchstudentButton=ttk.Button(leftFrame,text='Search for Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=12)
# Delete student button
deleteStudentButton = ttk.Button(leftFrame, text='Delete Student',width=25,state=DISABLED,command=delete_student)
deleteStudentButton.grid(row=3, column=0, pady=12)

# Update student button
updateStudentButton = ttk.Button(leftFrame, text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updateStudentButton.grid(row=4, column=0, pady=12)

# Show student button
showStudentButton = ttk.Button(leftFrame, text='Show Student',width=25,state=DISABLED,command=show_student)
showStudentButton.grid(row=5, column=0, pady=12)

# Export data button
exportDataButton = ttk.Button(leftFrame, text='Export Data',width=25,state=DISABLED,command=export_data)
exportDataButton.grid(row=6, column=0, pady=12)

# Exit button
exitButton = ttk.Button(leftFrame, text='Exit',width=25,state=DISABLED,command=iexit)
exitButton.grid(row=7, column=0, pady=12)

rightFrame=Frame(root)
rightFrame.place(x=350,y=100,width=1100,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
studentTable = ttk.Treeview(rightFrame, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address',
                                                 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)

# Configure scrollbars to control the view of the studentTable
scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

# Pack the scrollbars into the rightFrame
scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

# Add headings to the studentTable
studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')



style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',15,'bold'),foreground='red4')


# Show the table headings
studentTable['show'] = 'headings'

studentTable.pack(fill=BOTH, expand=True)

root.mainloop()
