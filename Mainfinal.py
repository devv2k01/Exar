#____________________IMPORT FILES__________________________
from tkinter import *
from tkinter import ttk
import os.path
from os import path
import pandas as pd
import matplotlib.pyplot as plt
import webbrowser
import time
from datetime import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from PIL import Image, ImageTk
from tkdocviewer import *
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
from sklearn.linear_model import LinearRegression

#____________________MAIN WINDOW___________________________

root = Tk()
root.geometry("720x800")
root.rowconfigure(0,weight = 1)
root.columnconfigure(0,weight = 1)
root.minsize(650,750)
root.title("EXARR")
#____________________CREATE FRAMES_________________________

#LOGIN_____________
login = Frame(root,bg = '#8080b6')
login.grid(row=0,column=0,sticky='nsew')

#REGISTER__________
register = Frame(root, bg = '#8080b6')
register.grid(row=0,column=0,sticky='nsew')

#SELECTION_________
selection = Frame(root, bg = '#8080b6')
selection.grid(row=0,column=0,sticky='nsew')

#ANALYZER__________
Analyzer = Frame(root, bg = '#8080b6')
Analyzer.grid(row=0,column=0,sticky='nsew')

#PAPERS____________
papers = Frame(root, bg = '#8080b6')
papers.grid(row=0,column=0,sticky='nsew')

#FEEDBACK__________
Feedback = Frame(root,bg = '#8080b6')
Feedback.grid(row=0,column=0,sticky='nsew')

#ABOUT US__________
AboutUs = Frame(root,bg = '#8080b6')
AboutUs.grid(row=0,column=0,sticky='nsew')

#FORGOT PASSWORD___
forgot = Frame(root,bg = '#8080b6')
forgot.grid(row=0,column=0,sticky='nsew')

#____________________VARIABLES_____________________________
#currentName = StringVar()
#currentUname = StringVar()
#currentPass = StringVar()
loginFlag = 0
global curName
curName = ""
global currentName
global currentUname
global currentPass

#LOGIN VARIABLES

logLabel = Label(login,text = '',bg = '#8080b6')
lUname = StringVar()
lPass = StringVar()

#REGISTER VARIABLES

regLabel = Label(register,text = '',bg = '#8080b6')
rName = StringVar()
rUname = StringVar()    
rPass = StringVar()
rConfirmPass = StringVar()

#SELECTION VARIABLES
selectionLabel = Label(selection, text = curName, fg = 'green', bg = "#8080b6")

r =IntVar()

#____________________FUNCTIONS_____________________________
def showframe(frame):
    frame.tkraise()

def logout():
    curName = ""
    currentName = ""
    currentPass = ""
    currentUname = ""
    showframe(login)

#____________________LOGIN FRAME___________________________
#background
bglogin = PhotoImage(file="background.png")
label_1=Label(login, image=bglogin)
label_1.place(x=0,y=0,relwidth=1,relheight=1)

#_Variables

logLabel = Label(login,text = '',bg = '#8080b6')
lUname = StringVar()
lPass = StringVar()

#_LOGIN FUNCTION
def logSubmit():
    logLabel.place_forget()
    selectionLabel.place_forget()
    logUname = lUname.get()
    logPass = lPass.get()

    logNameEntry.delete(0,END)
    logPassEntry.delete(0,END) 

    if(path.exists(logUname)):
        file1 = open(logUname,'r')
        lines = file1.readlines()
        global curName
        currentName = lines[0]
        currentUname = lines[1]
        currentPass = lines[2]
        currentName = currentName.strip()
        currentPass = currentPass.strip()
        curName = currentName
        selectionLabel["text"] = "Welcome "+curName
        selectionLabel["font"] = ("arial,15")
        if(currentPass == logPass):
            showframe(selection)
            logLabel["text"] ='Login Successful !!'
            logLabel["fg"] = 'green'
            logLabel["font"] = ("arial,15")
            logLabel["padx"] = 37

        else:
            logLabel["text"] ='Wrong Password !!'
            logLabel["fg"] = 'red'
            logLabel["font"] = ("arial,15")
            logLabel["padx"] = 37

    else: 
        logLabel["text"] ='User Not Found !!'
        logLabel["fg"] = 'red'
        logLabel["font"] = ("arial,15")
        logLabel["padx"] = 37

    logLabel.place(relx=0.33,rely=0.65)
    selectionLabel.place(relx = 0.2,rely = 0.2)



#_WIDGETS
logNameLabel= Label(login,text='Username:',width=20,height=2,bg = '#696969',font = ('arial',15)).place(relx=0.35,rely=0.3)
logNameEntry = Entry(login,width=25,textvariable = lUname, font = (10))
logNameEntry.place(relx=0.35,rely=0.35,relheight = 0.035)

logPassLabel= Label(login,text='Password:',width=20,height=2,bg = '#696969',font = ('arial',15)).place(relx=0.35,rely=0.45)
logPassEntry = Entry(login,width=25,show = '*',textvariable = lPass, font = (10))
logPassEntry.place(relx=0.35,rely=0.501,relheight = 0.035)

loginButton = Button(login,text = 'LOGIN', padx=40,pady=12, bg='#d0d0ff',
    command=lambda: logSubmit())
loginButton.place(relx=0.18,rely=0.7)

login2register = Button(login,text = 'REGISTER',
    padx=40,pady=12, bg='#d0d0ff',
    activeforeground="white",
    activebackground="blue",
    command=lambda: showframe(register))
login2register.place(relx=0.39,rely=0.7)

forgotButton = Button(login,text = 'Forgot password', padx=30,pady=12, bg='#d0d0ff',command = lambda: showframe(forgot))
forgotButton.place(relx=0.62,rely=0.7)

login2About = Button(login, text = "About Us", bg = '#d0d0ff', command = lambda: showframe(AboutUs))
login2About.place(relx = 0.02,rely = 0.02)

#____________________REGISTER FRAME________________________
#background
#bgregister = PhotoImage(file="background.png")
#label_2=Label(register, image=bgregister)
#label_2.place(x=0,y=0,relwidth=1,relheight=1)

#_REGISTER FUNCTION
def RegSubmit():
    regLabel.place_forget()
    regName = rName.get()
    regUname = rUname.get()
    regPass = rPass.get()
    regConfirmPass = rConfirmPass.get()
    RegNameEntry.delete(0,END)
    RegUnameEntry.delete(0,END)
    RegPassEntry.delete(0,END)
    ConfirmPassEntry.delete(0,END)
    if(path.exists(regUname)):
        regLabel["text"] ='Username Already Exists !'
        regLabel["fg"] = 'red'
        regLabel["font"] = ("arial,15")
        regLabel["padx"] = 37

    elif(len(regName)<1):
        regLabel["text"] ='Name Cannot be empty!'
        regLabel["fg"] = 'red'
        regLabel["font"] = ("arial,15")
        regLabel["padx"] = 20
    
    elif(len(regUname)<4):
        regLabel["text"] ='Username Should be atleast 4 characters'
        regLabel["fg"] = 'red'
        regLabel["font"] = ("arial,15")
        regLabel["padx"] = 15

    elif(len(regPass)<8):
        regLabel["text"] ='Password must be 8-16 characters !'
        regLabel["fg"] = 'red'
        regLabel["font"] = ("arial,15")
        regLabel["padx"] = 20

    elif(regPass != regConfirmPass):
        regLabel["text"] ='Passwords Do Not Match!'
        regLabel["fg"] = 'red'
        regLabel["font"] = ("arial,15")
        regLabel["padx"] = 20

    else:
        file = open(regUname,"w")
        file.write(regName+"\n")
        file.write(regUname+"\n")
        file.write(regPass+"\n")
        
        regLabel["text"] ='Account Created Successfully!'
        regLabel["fg"] = 'green'
        regLabel["font"] = ("arial,15")
        regLabel["padx"] = 27
        file.close()
    regLabel.place(relx=0.33,rely=0.65)



#_WIDGETS

RegNameLabel = Label(register,text='Name :',width=30,height=2).place(relx=0.35,rely=0.15)
RegNameEntry = Entry(register,textvariable = rName,width=35)
RegNameEntry.place(relx=0.35,rely=0.2)

RegUnameLabel = Label(register,text='Username:',width=30,height=2).place(relx=0.35,rely=0.25)
RegUnameEntry = Entry(register,textvariable = rUname,width=35)
RegUnameEntry.place(relx=0.35,rely=0.3)

RegPassLabel = Label(register,text='Password:',width=30,height=2).place(relx=0.35,rely=0.35)
RegPassEntry = Entry(register,show = '*',textvariable = rPass,width=35)
RegPassEntry.place(relx=0.35,rely=0.4)

ConfirmPassLabel = Label(register,text='Confirm Password:',width=30,height=2).place(relx=0.35,rely=0.45)
ConfirmPassEntry = Entry(register,show = '*',textvariable = rConfirmPass,width=35)
ConfirmPassEntry.place(relx=0.35,rely=0.5)

register2login = Button(register,text = 'LOGIN PAGE', 
    padx=40,pady=12, bg='#d0d0ff',
    command=lambda: showframe(login))
register2login.place(relx=0.18,rely=0.7)

registerSubmitBt = Button(register,text = 'SUBMIT', padx=40,pady=12, bg='#d0d0ff', command = RegSubmit)
registerSubmitBt.place(relx=0.6,rely = 0.7)


#_____________________OPTION SELECT PAGE___________________

def selectionRadio():
    x = r.get()
    if(x==1):
        showframe(Analyzer)
    elif(x==2):
        showframe(papers)

#background
bgselect = PhotoImage(file="background.png")
label_3=Label(selection, image=bgselect)
label_3.place(x=0,y=0,relwidth=1,relheight=1)

radioAn = Radiobutton(selection, text = 'Analyzer', variable = r, value =1,
    bg = 'Slategray4',
    font=("arial,30"))
radioAn.place(relx=0.2,rely=0.4)

radioPre = Radiobutton(selection, text = 'Previous papers', variable = r, value =2,
    bg = 'Slategray4',
    font=("arial,30"))
radioPre.place(relx=0.5,rely=0.4)

selectionSubmit = Button(selection, text = 'Submit',
    bg = 'LightSteelBlue4',
    font=('arial',20),
    command = selectionRadio)
selectionSubmit.place(relx=0.4,rely=0.6)

selectionLogout = Button(selection, text = 'Logout',
    bg = '#8080b6',
    font=('arial',10),
    command = logout)
selectionLogout.place(relx=0.9,rely=0.95)


#_____________________ANALYZER_____________________________
#Variables
activeSub = []
activeSubList = []
#Function
def viewGraph():
    activeSub.clear()
    activeSubList.clear()
    for i in range(0,len(subList)):
        activeSub.append(0)

    for i in range(0,len(enable)):
        activeSub[i] = int(enable[i].get())
    
    for i in range(0,len(subList)):
        if(activeSub[i]==1):
            activeSubList.append(subList[i])

 
    k=0
    for i in subList:
        if(activeSub[k]==1):
            plotFrame = subGroups.get_group(i)
            markList = plotFrame["Total"].tolist()
            plt.plot(yearList,markList)
        k+=1
    plt.legend(activeSubList)
    plt.ylim(0,35)
    plt.savefig('graph.png')
    #plt.show()
    
    path = "graph.png"
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(Analyzer,image = img)
    panel.photo = img
    panel.place(relx =0.1,rely = 0.38, relheight = 0.6,relwidth = 0.8)

    #panel.place(relx =0.1,rely = 0.45, relheight = 0.5,relwidth = 0.8)

    plt.close()
    

#DATAFRAME
df = pd.read_csv("Visualization_dataset.csv")

data = df.groupby(['Subject']).sum()
data.drop(['Year'],inplace = True, axis = 1)

yearList = df["Year"].tolist()
yearList = list(dict.fromkeys(yearList))

subList = df["Subject"].tolist()
subList = list(dict.fromkeys(subList))

subGroups = df.groupby(['Subject'])
yearGroups = df.groupby(['Year'])
x = len(subList)
enable = list(range(0,x))

#GUI_cont.
#background
bganalyse = PhotoImage(file="background.png")
label_4=Label(Analyzer, image=bganalyse)
label_4.place(x=0,y=0,relwidth=1,relheight=1)


xvar = 0.05
yvar = 0.03
for sub in enable:
    activeSub.append(0)
    enable[sub] = IntVar(value = 0)
    l = Checkbutton(Analyzer, text=subList[sub], variable=enable[sub],bg = 'LightSteelBlue4',font = ('arial',18))
    l.place(relx=xvar,rely=yvar)
    yvar+=0.05

analyzerSubmit = Button(Analyzer,text = "Submit", bg = '#8080b6',padx=18,pady=10,command=viewGraph).place(relx = xvar, rely = yvar+0.03)
analyzerLogout = Button(Analyzer, text = 'Logout',
    bg = '#8080b6',
    font=('arial',10),
    command = logout)
analyzerLogout.place(relx=0.91,rely=0.95,relwidth = 0.1)

analyzerBack = Button(Analyzer, text = 'Back',
    bg = '#8080b6',
    font=('arial',10),
    command = lambda: showframe(selection))
analyzerBack.place(relx=0.91,rely=0.9,relwidth = 0.1)

analyzerFeedback = Button(Analyzer, text = 'Feedback',
    bg = '#8080b6',
    font=('arial',10),
    command = lambda: showframe(Feedback))
analyzerFeedback.place(relx=0.91,rely=0.85,relwidth = 0.1)

AnalyzerPred = Button(Analyzer, text = 'Detailed Predction',
    bg = '#8080b6',
    font=('arial',10),
    command = lambda: showframe(prediction))
AnalyzerPred.place(relx=0.40,rely=0.1)

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(Analyzer, bg = '#8080b6', text = "Report",command=openweb)
Btn.place(relx = 0.70, rely = 0.100,relwidth = 0.1)
new = 1
url = "report.html"


#_____________________PAPERS_______________________________
def openfile():
    currFile = listMenu.get()
    v.display_file("pdfs/"+currFile)    
    print(currFile)


#background
bgpdf = PhotoImage(file="background.png")
label_5=Label(papers, image=bgpdf)
label_5.place(x=0,y=0,relwidth=1,relheight=1)

folder = 'pdfs'
filelist = [fname for fname in os.listdir(folder) if fname.endswith('.pdf')]

listMenu = ttk.Combobox(papers,values = filelist,font = ('arial', 15))
listMenu.current(0)
listMenu.place(relx = 0.1,rely = 0.1,relwidth = 0.4,relheight = 0.05)

v = DocViewer(papers)
v.place(relx = 0.05,rely = 0.25, relheight = 0.7, relwidth =0.9)


papersSubmit = Button(papers,text = "open",font = ('arial',15), bg = 'blue',command = openfile)
papersSubmit.place(relx = 0.2,rely = 0.16,relwidth = 0.16,relheight = 0.05)

papersLogout = Button(papers, text = 'Logout',
    bg = '#8080b6',
    font=('arial',10),
    command = logout)
papersLogout.place(relx = 0.8,rely = 0.1,relwidth = 0.09)

papersBack = Button(papers, text = 'Back',
    bg = '#8080b6',
    font=('arial',10),
    command = lambda: showframe(selection))
papersBack.place(relx = 0.8,rely = 0.15,relwidth = 0.09)

papersFeedback = Button(papers, text = 'Feedback',
    bg = '#8080b6',
    font=('arial',10),
    command = lambda: showframe(Feedback))
papersFeedback.place(relx = 0.8,rely = 0.2,relwidth = 0.09)

#_____________________FEEDBACK FRAME_______________________
def FeedbackSubmit():
    feedFieldError.place_forget()
    feedbackSuccess.place_forget()
    fName = feedName.get()
    fContact = feedContact.get()
    fEmail = feedEmail.get()
    uFeedback = feedbackEntry.get(1.0,END)
    
    now = str(datetime.now())

    if(len(fName) <= 1 or len(fContact) <= 1 or len(fEmail) <= 1 or len(uFeedback) < 1):
        feedFieldError.place(relx = 0.1,rely = 0.75)
    else:
        file = open("Feedback.txt",'a')
        file.write(now+"\nName = "+fName+"\nContact = "+fContact+"\nEmail = "+fEmail+"\nFeedback : \n"+uFeedback+"\n\n\n")
        file.close()
        feedbackSuccess.place(relx = 0.1, rely = 0.75)


#background
bgfeed = PhotoImage(file="feedback.png")
label_6=Label(Feedback, image=bgfeed)
label_6.place(x=0,y=0,relwidth=1,relheight=1)

feedFieldError = Label(Feedback,bg = '#8080b6',text = 'All fields are required!!!',fg = 'red',font = ('arial',17))
feedbackSuccess = Label(Feedback,bg = '#8080b6',text = 'Feedback Submitted \nYour review is valuable to us',fg = 'green',font = ('arial',17))

feedName = StringVar()
feedContact = StringVar()
feedEmail = StringVar()
userFeedback = StringVar()
feedback = StringVar()

feedNameLabel = Label(Feedback,bg = '#8080b6', text = "Name: ",font = ('arial',15)).place(relx = 0.1, rely = 0.1)
feedNameEntry = Entry(Feedback, font = ('arial',15),textvariable = feedName).place(relx = 0.25, rely = 0.1)

feedContactLabel = Label(Feedback,bg = '#8080b6', text = "Contact: ",font = ('arial',15)).place(relx = 0.1, rely = 0.15)
feedContactEntry = Entry(Feedback, font = ('arial',15),textvariable = feedContact).place(relx = 0.25, rely = 0.15)

feedEmailLabel = Label(Feedback,bg = '#8080b6', text = "Email: ",font = ('arial',15)).place(relx = 0.1, rely = 0.2)
feedEmailEntry = Entry(Feedback, font = ('arial',15),textvariable = feedEmail).place(relx = 0.25, rely = 0.2)

feedbackLabel = Label(Feedback,bg = '#8080b6', text = "Feedback: ",font = ('arial',15)).place(relx = 0.1, rely = 0.25)
feedbackEntry = Text(Feedback,font = ('arial',15))
feedbackEntry.place(relx = 0.1,rely = 0.3,relheight = 0.3,relwidth = 0.6)

FeedbackSubmitBt = Button(Feedback,text = 'Submit',bg = '#d0d0ff',font = ('arial',12),height = 2,width = 10,command = FeedbackSubmit).place(relx = 0.1,rely = 0.65)

FeedbackBack = Button(Feedback, text = 'Back',
    bg = '#8080b6',
    font=('arial',10),
    command = lambda: showframe(selection))
FeedbackBack.place(relx=0.91,rely=0.9)

#_____________________ABOUT US FRAME_______________________
AboutUs = Frame(root,bg = '#8080b6')
AboutUs.grid(row=0,column=0,sticky='nsew')


#background
bgau = PhotoImage(file="aboutus.png")
label_6=Label(AboutUs, image=bgau)
label_6.place(x=0,y=0,relwidth=1,relheight=1)

var = StringVar()

w = Label(AboutUs,
    text = "Here we are proposing this project \nwhich will analyze the previous year exam \npapers and will conclude a pattern to cover \nthe complete syllabus efficiently",
    bg = '#FFD700', fg = 'black',
    justify = LEFT,
    font = ('arial',20))
w.place(relx = 0.01, rely = 0.1, relwidth = 0.9, relheight = 0.2)

nameLabel1 = Label(AboutUs, text = "Divyanshu Shrivastava",
font = ('arial',12),
bg = '#FFFFFF',fg = 'black').place(relx = 0.1,rely = 0.6,relwidth = 0.25)
nameLabel2 = Label(AboutUs, text = "Nayanpreet Chhabra",
font = ('arial',12),
bg = '#FFFFFF',fg = 'black').place(relx = 0.4,rely = 0.6,relwidth = 0.25)
nameLabel3 = Label(AboutUs, text = "Chaitanya Mishra",
font = ('arial',12),
bg = '#FFFFFF',fg = 'black').place(relx = 0.7,rely = 0.6,relwidth = 0.25)

mailLabel1 = Label(AboutUs, text = "divyanshu2k01@gmail.com",
font = ('arial',12),
bg = '#FF7F50',fg = 'black').place(relx = 0.1,rely = 0.65,relwidth = 0.25)
mailLabel2 = Label(AboutUs, text = "nayanpreetchhabra9261@gmail.com",
font = ('arial',12),
bg = '#FF7F50',fg = 'black').place(relx = 0.4,rely = 0.65,relwidth = 0.25)
mailLabel3 = Label(AboutUs, text = "chaitanyamishra402@gmail.com",
font = ('arial',12),
bg = '#FF7F50',fg = 'black').place(relx = 0.7,rely = 0.65,relwidth = 0.25)

AboutUs2login = Button(AboutUs,text = "Back",bg = '#d0d0ff',width = 10, command = logout)
AboutUs2login.place(relx = 0.86, rely = 0.95)

#-----------------------Aboutus Connectivity----------------------------------------------------------

new = 1
url1 = "https://www.linkedin.com/in/divyanshu-shrivastava-34a1a5179"



def openweb1():
    webbrowser.open(url1,new=new)


Btn = Button(AboutUs, text = "Linked In",command=openweb1)
Btn.place(relx = 0.2, rely = 0.70)

new = 2
url2 =  "https://www.linkedin.com/in/nayanpreet-chhabra-5b0092169"

def openweb2():
    webbrowser.open(url2,new=new)


Btn = Button(AboutUs, text = "Linked In",command=openweb2)
Btn.place(relx = 0.5, rely = 0.70)


new = 3
url3 = "https://www.linkedin.com/in/chaitanya-mishra-8b2b391b5/"

def openweb3():
    webbrowser.open(url3,new=new)

Btn = Button(AboutUs, text = "Linked In",command=openweb3)
Btn.place(relx = 0.8, rely = 0.70)

#_____________________FORGOT PASSWORD______________________
def forgotSubmit():
    forPassSuccess.place_forget()
    forPassError.place_forget()
    forPassName = forName.get()
    forPassMail = forMail.get()
    if(len(forPassName) > 0 and len(forPassMail) > 0):
        file = open("forgot.txt",'a')
        file.write("Usename = "+forPassName+"\nEmail = "+forPassMail+"\n\n")
        file.close()
        forPassSuccess.place(relx = 0.3,rely = 0.6)
    else:
        forPassError.place(relx = 0.35,rely = 0.6)

forPassError = Label(forgot, text = "All fields are required!!", fg = 'red',bg = '#8080b6', font = (12))
forPassSuccess = Label(forgot, text = "Request Submitted Successfully!!", fg = 'green',bg = '#8080b6', font = (12))


forName = StringVar()
forMail = StringVar()

forgotNameLabel= Label(forgot,text='Username:',width=20,height=2,bg = '#8080b6',font = ('arial',15)).place(relx=0.35,rely=0.3)
forgotNameEntry = Entry(forgot,width=20,textvariable = forName, font = (10))
forgotNameEntry.place(relx=0.35,rely=0.35,relheight = 0.035)

forgotEmailLabel= Label(forgot,text='Email:',width=20,height=2,bg = '#8080b6',font = ('arial',15)).place(relx=0.35,rely=0.45)
forgotEmailEntry = Entry(forgot,width=20,textvariable = forMail, font = (10))
forgotEmailEntry.place(relx=0.35,rely=0.501,relheight = 0.035)

forgotButton = Button(forgot, text = 'Submit',font = (12), padx = 35, pady = 12, command = forgotSubmit)
forgotButton.place(relx = 0.4, rely = 0.7)

forgotHome = Button(forgot, text = 'Back',font = (4),command = logout)
forgotHome.place(relx = 0.9, rely = 0.95)

#_____________________PREDICTION PAGE______________________
prediction = Frame(root,bg = '#8080b6')
prediction.grid(row=0,column=0,sticky='nsew')


#PREDICTION
df2=pd.read_csv("prediction_dataset.csv")
df2.columns.str.strip()
lc=LabelEncoder()
df2["Subject_n"]=lc.fit_transform(df2["Subject"])
#print(df2)
x_data=df2[['Year','Subject_n']]
x_data.head()

preSubList = df2["Subject"].tolist()
preSubList = list(dict.fromkeys(preSubList))

y_data=df2[['Total']]
y_data.head()
x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,test_size=0.3,random_state=9)
lr = LinearRegression()
lr.fit (x_train, y_train ) 

yhat=lr.predict(x_test)
subMarkList = []
for i in range(0,5):
    x_new=[[2022,i]]
    pre=lr.predict(x_new)
    subMarkList.append(float(pre))

subx = 0.25
suby = 0.2

predx = 0.5 
predy = 0.2

#GUI Contd.

#background
bgpred = PhotoImage(file="background.png")
label_8=Label(prediction, image=bgpred)
label_8.place(x=0,y=0,relwidth=1,relheight=1)

Label(prediction,text= 'Predicted Marks for Next examination:',bg='#8080b6',font=(12)).place(relx = 0.265,rely = 0.1)

for i in range(0,len(preSubList)):
    Label(prediction,font = (10),bg = '#8080b6',text = preSubList[i]).place(relx = subx,rely = suby)
    predM = str(":  "+str(subMarkList[i]))
    Label(prediction,font = (10),bg = '#8080b6',text = predM).place(relx = predx,rely = predy)
    predy+=0.05
    suby+=0.05

predBack = Button(prediction, text = 'Back', font = (12),command= lambda: showframe(Analyzer)).place(relx = 0.45,rely = suby+0.05)


# ____________________MAINLOOP_____________________________
showframe(login)
root.mainloop()