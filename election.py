from tkinter import messagebox
import sqlite3
from tkinter import *
from tkinter import filedialog
import shutil
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3

conn=sqlite3.connect('election_system.db')
c=conn.cursor()

'''The following four comments needs to be executed before starting the first time implementation of the project
   because they are needed to create the tables once'''


#c.execute("CREATE TABLE vote_result(sl_no int primary key,party_name text,colour text,total_vote_given int)")
#c.execute("CREATE TABLE student_register(voter_id int primary key,stuname text,usn text,image blob,email text,year_of_passing int,dept text,voting character)")

'''The following is the code for voting'''
def voted1():
    cursor10 = conn.execute("SELECT total_vote_given from vote_result where sl_no=1")
    for row in cursor10:
        number = str(row[0])
    getnumber = int(number)
    totalnumber = getnumber
    totalnumber=totalnumber+1
    con=str(totalnumber)

    conn.execute("UPDATE vote_result SET total_vote_given = ? WHERE sl_no=1",(con))

    conn.commit()
    messagebox.showinfo('Message title', 'voting successful')
    voted.destroy()

def voted2():
    cursor10 = conn.execute("SELECT total_vote_given from vote_result where sl_no=2")
    for row in cursor10:
        number = str(row[0])
    getnumber = int(number)
    totalnumber = getnumber
    totalnumber = totalnumber + 1
    con = str(totalnumber)


    conn.execute(
        "UPDATE vote_result SET total_vote_given= ? WHERE sl_no=2",
        (con))
    conn.commit()
    messagebox.showinfo('Message title', 'voting successful')
    voted.destroy()

def voted3():
    cursor10 = conn.execute("SELECT total_vote_given from vote_result where sl_no=3")
    for row in cursor10:
        number = str(row[0])
    getnumber = int(number)
    totalnumber = getnumber
    totalnumber = totalnumber + 1
    con = str(totalnumber)

    conn.execute(
        "UPDATE vote_result SET total_vote_given= ? WHERE sl_no=3",
        (con))
    conn.commit()
    messagebox.showinfo('Message title', 'voting successful')


def voted4():
    cursor10 = conn.execute("SELECT total_vote_given from vote_result where sl_no=4")
    for row in cursor10:
        number = str(row[0])
    getnumber = int(number)
    totalnumber = getnumber
    totalnumber = totalnumber + 1
    con = str(totalnumber)

    conn.execute(
        "UPDATE vote_result SET total_vote_given= ? WHERE sl_no=4",
        (con))
    conn.commit()

    messagebox.showinfo('Message title', 'voting successful')

def test():
    cursor10 = conn.execute("SELECT total_vote_given from vote_result where sl_no=1")
    for row in cursor10:
        number = str(row[0])
    getnumber = int(number)

    conn.commit()
    cursor11 = conn.execute("SELECT total_vote_given from vote_result where sl_no=2")
    for row in cursor11:
        number1 = str(row[0])
    getnumber1 = int(number1)
    conn.commit()
    cursor12 = conn.execute("SELECT total_vote_given from vote_result where sl_no=3")
    for row in cursor12:
        number2 = str(row[0])
    getnumber2 = int(number2)
    conn.commit()
    cursor13 = conn.execute("SELECT total_vote_given from vote_result where sl_no=4")
    for row in cursor13:
        number3 = str(row[0])
    getnumber3 = int(number3)
    conn.commit()

    totalnumber1 = getnumber + getnumber1 + getnumber2 + getnumber3

    return totalnumber1

def voted():


    voter=Tk()

    totalnumber2=test()

    voter.title("COLLEGE VOTING MANAGEMENT SYSTEM")


    #labelfont = ('times', 20, 'bold')
    #label_a = Label(window, text="VOTING PANEL")
    #label_a.config(font=labelfont)
    #label_a.grid(column=0, row=0)

    labelfont1 = ('times', 14, 'bold')
    label1 = Label(voter, text="NSUP", bg="green")
    label1.config(font=labelfont1)
    label1.grid(column=0, row=2, sticky=NSEW)

    label2 = Label(voter, text="YOUTH TRENDS", bg="red")
    label2.config(font=labelfont1)
    label2.grid(column=0, row=5, sticky=NSEW)

    label3 = Label(voter, text="COOL NERDIES", bg="blue")
    label3.config(font=labelfont1)
    label3.grid(column=0, row=6, sticky=NSEW)

    label3 = Label(voter, text="COMMMONER'S GROUP", bg="yellow")
    label3.config(font=labelfont1)
    label3.grid(column=0, row=8, sticky=NSEW)

    btn = Button(voter, text='vote', relief="raised",command=voted1)
    btn.grid(column=4, row=2)

    btn1 = Button(voter, text='vote', relief="raised",command=voted2)
    btn1.grid(column=4, row=5)

    btn2 = Button(voter, text='vote', relief="raised",command=voted3)
    btn2.grid(column=4, row=6)

    btn3 = Button(voter, text='vote', relief="raised",command=voted4)
    btn3.grid(column=4, row=8)

    label3 = Label(voter, text="No.of voted")
    label3.config(font=labelfont1)
    label3.grid(column=8, row=5, sticky=NSEW)

    label3 = Label(voter, text=totalnumber2)
    label3.config(font=labelfont1)
    label3.grid(column=8, row=6, sticky=NSEW)
    voter.mainloop()




'''This is the code for result section'''

def result():

    cursor1 = conn.execute("SELECT total_vote_given from vote_result where sl_no=1")
    for row in cursor1:
        totalvote1=str(row[0])
        o1=int(totalvote1)
        per1=o1


    cursor2 = conn.execute("SELECT total_vote_given from vote_result where sl_no=2")
    for row in cursor2:
        totalvote2 = str(row[0])
        o2 = int(totalvote2)
        per2 = o2

    cursor3 = conn.execute("SELECT total_vote_given from vote_result where sl_no=3")
    for row in cursor3:
        totalvote3 = str(row[0])
        o3 = int(totalvote3)
        per3 = o3

    cursor4 = conn.execute("SELECT total_vote_given from vote_result where sl_no=4")
    for row in cursor4:
        totalvote4 = str(row[0])
        o4 = int(totalvote4)
        per4 = o4

    cursor5= conn.execute("SELECT count(voter_id) from student_register")
    for row in cursor5:
        total1 = str(row[0])
        o5 = int(total1)
        t = o5

    totalper1=(per1*100)/t
    totalper2=(per2*100)/t
    totalper3=(per3*100)/t
    totalper4=(per4*100)/t

    status=Tk()
    titleno = Label(status, text="Number of votes\nreceived:")
    titleno.grid(row=0, column=0)

    nsuipvoter = Label(status, text=totalvote1, bg="white")
    nsuipvoter.grid(row=1, column=0, sticky=E)

    nsuip = Label(status, text="National student union party", bg="green")
    nsuip.grid(row=1, column=1, sticky=E)

    nsuipper = Label(status, text=totalper1, bg="white")
    nsuipper.grid(row=1, column=2, sticky=E)

    ytvoter = Label(status, text=totalvote2, bg="white")
    ytvoter.grid(row=2, column=0, sticky=E)

    yt = Label(status, text="        YOUTH TRENDS         ", bg="red")
    yt.grid(row=2, column=1, sticky=E)

    ytper = Label(status, text=totalper2, bg="white")
    ytper.grid(row=2, column=2, sticky=E)

    cnvoter = Label(status, text=totalvote3, bg="white")
    cnvoter.grid(row=3, column=0, sticky=E)

    cn = Label(status, text="       COOL NERDIES           ", bg="blue")
    cn.grid(row=3, column=1, sticky=E)

    cnper = Label(status, text=totalper3, bg="white")
    cnper.grid(row=3, column=2, sticky=E)

    cgvoter = Label(status, text=totalvote4, bg="white")
    cgvoter.grid(row=4, column=0, sticky=E)

    cg = Label(status, text="      COMMONER'S GROUP    ", bg="yellow")
    cg.grid(row=4, column=1, sticky=E)

    cgper = Label(status, text=totalper4, bg="white")
    cgper.grid(row=4, column=2, sticky=E)

    per = Label(status, text="% of votes\nreceived")
    per.grid(row=0, column=2)

    total = Label(status, text="Total no.of \nvoters ")
    total.grid(row=3, column=8)

    totalvoter = Label(status, text=t, bg="white")
    totalvoter.grid(row=4, column=8)


    status.mainloop()

'''This is code for register section'''

def register_class():

    def register_now():
        global getname, getaddress,getdept,getyear,getmail


        getname = entername.get()
        getusn = enterusn.get()
        getdept = enterdept.get()
        getyear = enteryear.get()
        getmail = enteremail.get()
        if (getname == "" or getmail == "" or getusn == "" or getdept == "" or getyear == "" ):
            messagebox.showinfo("Empty Field", "No Field should be EMPTY")


        else:
            cursor4 = conn.execute("SELECT voter_id from student_register")
            rows = cursor4.fetchall()
            for row in rows:
                totale = str(row[0])
            os1 = int(totale)
            pe = os1

            conn.commit()

            #conn.execute("INSERT INTO student_register(voter_id,name,usn,email,year_of_passing,dept,voting) VALUES(?,?,?,?,?,?,?)",
                         #(pe,))
            conn.execute("UPDATE student_register SET stuname = ?, usn = ?, email = ?,year_of_passing = ?,dept= ?,voting= ? WHERE voter_id=?",
                         (getname, getusn, getmail, getyear, getdept, 0,pe))

            email_user = 'upchar.pythonproject.com@gmail'
            email_password = 'pycharm.python3'
            email_send = str(getmail)

            subject = 'college voter id'

            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['To'] = email_send
            msg['Subject'] = subject
            body = 'Hi there, sending this email to tell your voter id = ' + str(pe)
            msg.attach(MIMEText(body, 'plain'))

            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)

            server.sendmail(email_user, email_send, text)
            server.quit()

            messagebox.showinfo("voter id","check your email id")
            conn.commit()
            register.destroy()




    register=Tk()

    def browsefunc():
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        path1 = os.path.abspath(filename)
        path=shutil.copy(path1, 'C:\\Users\\mkbon\\PycharmProjects\\online_election _system')
        cursor4 = conn.execute("SELECT voter_id from student_register")
        rows = cursor4.fetchall()
        for row in rows:
            totale = str(row[0])
        os1 = int(totale)
        pe = os1
        pe = pe + 1
        conn.commit()

        conn.execute(
            "INSERT INTO student_register(voter_id,image) VALUES(?,?)",(pe,path))
        conn.commit()
    name1= Label(register, text="NAME:")
    name1.grid(row=0, column=0, sticky=E)

    entername = Entry(register, bd=3)
    entername.grid(row=0, column=2)

    usn = Label(register, text="USN:")
    usn.grid(row=1, column=0, sticky=E)


    enterusn = Entry(register)
    enterusn.grid(row=1, column=2)

    uploadid = Label(register, text="UPLOAD YOUR COLLEGE ID:")
    uploadid.grid(row=2, column=0, sticky=E)

    button_id = Button(register, text="upload", bg="light green", relief="raised",command= browsefunc)
    button_id.grid(row=2, column=2)

    #filepath = Label(register)
    #filepath.grid(row=3,column=2)

    email = Label(register, text="EMAIL:")
    email.grid(row=4, column=0, sticky=E)

    enteremail = Entry(register, bd=3)
    enteremail.grid(row=4, column=2)

    year = Label(register, text="YEAR OF PASSING:")
    year.grid(row=5, column=0, sticky=E)

    enteryear = Entry(register, bd=3)
    enteryear.grid(row=5, column=2)

    dept = Label(register, text="DEPARTMENT:")
    dept.grid(row=6, column=0, sticky=E)

    enterdept = Entry(register, bd=3)
    enterdept.grid(row=6, column=2)

    button_id = Button(register, text="submit", bg="light green", relief="raised",command=register_now)
    button_id.grid(row=8, column=2)

    register.mainloop()


'''THIS IS CODE FOR VOTER WHO HAS GIVEN THE VOTE'''

def checking():


    if (enterid.get() == ""):
        messagebox.showinfo("Empty Field", "Any Field can't be EMPTY")

    else:
        y = [int(enterid.get())]

        conn = sqlite3.connect('election_system.db')
        c = conn.cursor()
        flag = 0
        for row in c.execute("Select voter_id from student_register"):
            if str(row) == str(tuple(y)):
                flag = 1
                break
        y = int(str(y[0]))
        l = []
        l.append(y)
        ver=0
        try:
            for row1 in c.execute("select voting from student_register where voter_id=?",l):
                r=str(row1[0])
                o=int(r)
        except :
            messagebox.showerror('ERROR','HELP ENTER VALID VOTER ID')
        if(o==0):
            ver=1

        if (flag == 1 & ver==1):


            conn.execute(
                "UPDATE student_register SET voting= 1 WHERE voter_id=?",
                (l))
            conn.commit()

            voted()

        else:
            messagebox.showinfo("you have already vote", "Sorry!only once you can vote")

        conn.commit()


''' MAIN PAGE OF ONLINE ELECTION SYSTEM'''

window=Tk()

labelfont=('times',30,'bold')
label_a=Label(window,text="ONSTREAM PLEBISCITE SETUP")
label_a.config(font=labelfont)
label_a.grid(column=0)

voterid=Label(window,text="enter your voter Id:  ")
voterid.grid(row=2,column=0)

enterid=Entry(window,bd=3)
enterid.grid(row=3,column=0)

button_m1=Button(window,text=" login ",bg="light green",relief="raised",command=checking)
button_m1.grid(row=4,column=0)


button_m2=Button(window,text=" register ",bg="light green",relief="raised",command=register_class)
button_m2.grid(row=5,column=0)

button_m3=Button(window,text=" result ",bg="light green",height="2",width="15",relief="raised",command=result)
button_m3.grid(row=6,column=0)

label_a=Label(window,text="   ")
label_a.grid(column=1)

window.mainloop()















