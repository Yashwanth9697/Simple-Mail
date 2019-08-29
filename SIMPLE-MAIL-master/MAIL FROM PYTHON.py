from tkinter import *
from smtplib import SMTP
myapp=Tk()
myapp.resizable(0,0)
myapp.iconbitmap("pyt.ico")
def send_mail():
	try:
		user_mail=mail_text.get()
		user_psw=password_text.get()
		message=message_text.get()
		sender_mail=receivemail_text.get()
		mail=SMTP("SMTP.gmail.com",587)
		mail.ehlo()
		mail.starttls()
		mail.login(user_mail,user_psw)
		mail.sendmail(user_mail,sender_mail,message)
		mail.close()
		emyapp=Tk()
		emyapp.iconbitmap("pyt.ico")
		emyapp.resizable(0,0)
		emyapp.geometry("398x177+490+225")
		emyapp.title("Mail Sent")
		Label(emyapp,text="Success",font=30,relief=GROOVE).place(relx=0.13, rely=0.17, height=41, width=304)
		Label(emyapp,text="Message Sent Successfully",font=30,relief=GROOVE).place(relx=0.13, rely=0.56, height=41, width=304)
		emyapp.mainloop()
	except:
		emyapp=Tk()
		emyapp.iconbitmap("pyt.ico")
		emyapp.resizable(0,0)
		emyapp.geometry("398x177+490+225")
		emyapp.title("Invalid Details")
		Label(emyapp,text="Please Provide Valid Detail's",font=30,relief=GROOVE).place(relx=0.13, rely=0.17, height=41, width=304)
		Label(emyapp,text="Message Sending Failed",font=30,relief=GROOVE).place(relx=0.13, rely=0.56, height=41, width=304)
		emyapp.mainloop()
myapp.geometry("634x480+410+68")
myapp.title("G-Mail Python-APP")
myapp.configure(background="#2daad8")
mail_text=StringVar()
mail_entry=Entry(myapp,textvariable=mail_text,background="#c4efff",relief=GROOVE,font=18).place(relx=0.47, rely=0.17,height=30,width=264)
mail_label=Label(myapp,text='E-Mail ID',background="#2daad8",font=18,foreground="#dddddd").place(relx=0.22, rely=0.17 ,height=30, width=100)
password_text=StringVar()
password_entry=Entry(myapp,background="#c4efff",textvariable=password_text,relief=GROOVE,font=18,show='X').place(relx=0.47, rely=0.27,height=30, relwidth=0.42)
password_label=Label(myapp,text='Password',background="#2daad8",font=18,foreground="#dddddd").place(relx=0.22, rely=0.27, height=30, width=100)
message_label=Label(myapp,text="Enter the message",background="#2daad8",font=18,foreground="#dddddd").place(relx=0.36, rely=0.4, height=30, width=190)
message_text=StringVar()
message_entry=Entry(myapp,font=23,background="#ffff36",textvariable=message_text,foreground="#000000").place(relx=0.25, rely=0.48,height=40, relwidth=0.51)
receivemail_text=StringVar()
receivemail_entry=Entry(myapp,textvariable=receivemail_text,background="#c4efff",relief=GROOVE,font=18).place(relx=0.47, rely=0.63, height=30, relwidth=0.42)
receivemail_label=Label(myapp,text='Destination Mail ID',background="#2daad8",font=18,foreground="#dddddd").place(relx=0.08, rely=0.63, height=30, width=200)
send_button=Button(myapp,text='Send Mail',command=send_mail,relief=GROOVE,background="#39d820",foreground="#ffffff",font=18).place(relx=0.3, rely=0.75, height=34, width=247)
Label(myapp,text="Created by : Yashwanth",width=194).place(relx=0.68, rely=0.95, height=21, width=194)
myapp.mainloop()
