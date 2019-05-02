#import library
# Amit Kumar De 02/05/2019
# Please subscribe to our channel https://www.youtube.com/channel/UCYtH9iBldgQo4ns2xI1PHhw
import tkinter
import mysql.connector
from mysql.connector import Error

def getWeather(selectedcity):
    
    import requests
    scity=selectedcity.get()
    url="https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=64605ab24bdd56eb5e21a114abcd92b8".format(scity)
    data=requests.get(url)
    data=data.json()
    
    swindow=tkinter.Tk()
    swindow.geometry('280x300')
    swindow.title('Weather Details')
    swindow.configure(background='black')
    tkinter.Label(swindow,text=" ").grid(row=0,column=0)
    
    if(data['cod']==200):
        
        tkinter.Label(swindow,text=" ",bg='black',fg='yellow').grid(row=0,column=0)
        tkinter.Label(swindow,text=" ",bg='black',fg='yellow').grid(row=1,column=0)
        tkinter.Label(swindow,text="Weather details in "+scity,bg='black',fg='yellow').grid(row=2,column=0)
        tkinter.Label(swindow,text="Overall:",bg='black',fg='yellow').grid(row=3,column=0)
        tkinter.Label(swindow,text=str(data['weather'][0]['main']),bg='black',fg='yellow').grid(row=3,column=1)
        tkinter.Label(swindow,text="Temperature:",bg='black',fg='yellow').grid(row=4,column=0)
        tkinter.Label(swindow,text=str(data['main']['temp'])+"C",bg='black',fg='yellow').grid(row=4,column=1)
        tkinter.Label(swindow,text="Pressure:",bg='black',fg='yellow').grid(row=5,column=0)
        tkinter.Label(swindow,text=str(data['main']['pressure'])+"hPa",bg='black',fg='yellow').grid(row=5,column=1)
        tkinter.Label(swindow,text="Humidity:",bg='black',fg='yellow').grid(row=6,column=0)
        tkinter.Label(swindow,text=str(data['main']['humidity'])+"%",bg='black',fg='yellow').grid(row=6,column=1)
        tkinter.Label(swindow,text="Maximum Temperature:",bg='black',fg='yellow').grid(row=7,column=0)
        tkinter.Label(swindow,text=str(data['main']['temp_max'])+"C",bg='black',fg='yellow').grid(row=7,column=1)
        tkinter.Label(swindow,text="Minimum Temperature:",bg='black',fg='yellow').grid(row=8,column=0)
        tkinter.Label(swindow,text=str(data['main']['temp_min'])+"C",bg='black',fg='yellow').grid(row=8,column=1)
        tkinter.Label(swindow,text="Wind Speed:",bg='black',fg='yellow').grid(row=9,column=0)
        tkinter.Label(swindow,text=str(data['wind']['speed'])+"meter/sec",bg='black',fg='yellow').grid(row=9,column=1)
        tkinter.Label(swindow,text="Wind Direction:",bg='black',fg='yellow').grid(row=11,column=0)
        tkinter.Label(swindow,text=str(data['wind']['deg'])+"deg",bg='black',fg='yellow').grid(row=11,column=1)
        swindow.mainloop()
    else:
        tkinter.Label(swindow,text=" ",bg='black',fg='yellow').grid(row=0,column=0)
        tkinter.Label(swindow,text=" ",bg='black',fg='yellow').grid(row=1,column=0)
        tkinter.Label(swindow,text="City Not Found",bg='black',fg='yellow').grid(row=2,column=0)
        swindow.mainloop()

def openweatherpage():
    owindow=tkinter.Toplevel(window)
    owindow.geometry('280x300')
    owindow.title('Welcome to Weather365')
    owindow.configure(background='black')
    global selectedcity
    selectedcity=tkinter.StringVar()
    tkinter.Label(owindow,text=" ",bg='black',fg='yellow').grid(row=0,column=0)
    tkinter.Label(owindow,text=" ",bg='black',fg='yellow').grid(row=1,column=0)
    tkinter.Label(owindow,text="Get today's weather",bg='black',fg='yellow').grid(row=2,column=0)
    tkinter.Label(owindow,text='Enter the City name:',bg='black',fg='yellow').grid(row=3,column=0)
    tkinter.Entry(owindow,textvariable=selectedcity).grid(row=3,column=1)
    print("City::"+selectedcity.get())
    tkinter.Label(owindow,text=" ",bg='black',fg='yellow').grid(row=4,column=1)
    tkinter.Button(owindow,text="Check", command=lambda: getWeather(selectedcity),bg='yellow',fg='black').grid(row=5,column=0)
    owindow.mainloop()
    
def checkPass(formpass,datapass):
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["pbkdf2_sha256","md5_crypt", "des_crypt"],default="pbkdf2_sha256",pbkdf2_sha256__default_rounds=30000)
    match=pwd_context.verify(formpass,datapass)
    return match

def login(userid,password):
    usrid=userid.get()
    print('login attempted'+usrid)
    
    uname=userid.get()
    pas=password.get()
    try:
        passfile=open('pwd.txt')
        pas=passfile.readline()
        mydb = mysql.connector.connect(host="localhost",user="root",passwd=pas)
        cursor=mydb.cursor()
        dbselectquery="use openweatherstore"
        
        selectquery="select password from User where email=%s"
        arg=(uname,)
        cursor.execute(dbselectquery)
        cursor.execute(selectquery,arg)
        records=cursor.fetchall()
        if cursor.rowcount==1:
            for row in records:
                pasw=row[0]
                print("Password..."+pasw)
                loginsuccess=checkPass(pas,pasw)
                if loginsuccess:                    
                    openweatherpage()
                else:
                    fwindow=tkinter.Toplevel(window)
                    fwindow.geometry("280x300")
                    fwindow.configure(background='black')
                    tkinter.Label(fwindow,text="Please provide correct password",bg='black',fg='yellow').grid(row=0,column=0)
                    fwindow.mainloop()
        else:
            awindow=tkinter.Toplevel(window)
            awindow.geometry("280x300")
            awindow.configure(background='black')
            tkinter.Label(awindow,text=" ",bg='black',fg='yellow').grid(row=0,column=0)
            tkinter.Label(awindow,text=" ",bg='black',fg='yellow').grid(row=1,column=0)
            tkinter.Label(awindow,text="Username does not exist",bg='black',fg='yellow').grid(row=0,column=0)
            awindow.mainloop()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        mydb.close()

def encryptPass(password):
    from passlib.context import CryptContext
    global pwd_context
    pwd_context = CryptContext(schemes=["pbkdf2_sha256","md5_crypt", "des_crypt"],default="pbkdf2_sha256",pbkdf2_sha256__default_rounds=30000)
    enpass=pwd_context.hash(password)
    return enpass

def dbconnectRegister(firstname,lastname,email,rpassword,rwindow):
    fname=firstname.get()
    print("firstname",fname)
    lname=lastname.get()
    print("lastname",lname)
    e=email.get()
    print("email",e)
    pas=password.get()
    enpas=encryptPass(pas)
    
    try:
        passfile=open('pwd.txt')
        pas=passfile.readline()
        connector=mysql.connector.connect(host='localhost',user='root',passwd=pas) 
        cursor=connector.cursor()   
        dbselectquery="use openweatherstore"
        createtablequery="create table if not exists User(firstname varchar(30), lastname varchar(30), email varchar(30) primary key, password varchar(300))"
        insertquery="Insert into User(firstname,lastname,email,password) values(%s,%s,%s,%s)"
        arg=(fname,lname,e,enpas)
        cursor.execute(dbselectquery)
        cursor.execute(createtablequery)
        count=cursor.execute(insertquery,arg)
        print(count)
        connector.commit()
        rwindow.destroy()
        swindow=tkinter.Tk()
        swindow.title('Success')
        swindow.geometry('280x300')
        swindow.configure(background='black')
        tkinter.Label(swindow,text=' ',bg='black',fg='yellow').grid(row=0,column=0)
        tkinter.Label(swindow,text=' ',bg='black',fg='yellow').grid(row=1,column=0)
        tkinter.Label(swindow,text=' ',bg='black',fg='yellow').grid(row=2,column=0)
        tkinter.Label(swindow,text='You have successfully registered to Open Weather',bg='black',fg='yellow').grid(row=3,column=0)
        tkinter.Button(swindow,text='Ok',command=swindow.destroy,bg='yellow',fg='black').grid(row=5,column=0)
        swindow.mainloop()
    except Error as error:
        print(error)    
    finally:
        cursor.close()
        connector.close()    
      
def register():
    print('register')
    firstname= tkinter.StringVar()
    lastname=tkinter.StringVar()
    email=tkinter.StringVar()
    rpassword=tkinter.StringVar()
    
    rwindow=tkinter.Toplevel(window)
    rwindow.title("Register Weather365")
    rwindow.geometry('280x300')
    rwindow.configure(background='black')
    tkinter.Label(rwindow, text = "Welcome to Open Weather",bg='black',fg='yellow').grid(row=0,columnspan=4)
    tkinter.Label(rwindow,text="First Name",bg='black',fg='yellow').grid(row=1,column=0)
    tkinter.Label(rwindow,bg='black',fg='yellow').grid(row=1,column=1)
    tkinter.Entry(rwindow, textvariable=firstname).grid(row=1,column=2)
    tkinter.Label(rwindow,text="Last Name",bg='black',fg='yellow').grid(row=2,column=0)
    tkinter.Entry(rwindow, textvariable=lastname).grid(row=2,column=2)
    tkinter.Label(rwindow, text="Email ID",bg='black',fg='yellow').grid(row=3,column=0) 
    tkinter.Entry(rwindow, textvariable=email).grid(row=3,column=2)
    tkinter.Label(rwindow, text="Password",bg='black',fg='yellow').grid(row=4,column=0) 
    tkinter.Entry(rwindow,show="*",textvariable=rpassword).grid(row=4,column=2)  
    tkinter.Label(rwindow,bg='black',fg='yellow').grid(row=6,column=0)
    
    print("firstname....",firstname.get())
    print("lastname....",lastname.get())
    print("email",email.get())
    print("password",rpassword.get())
    tkinter.Button(rwindow, text="Register", command=lambda: dbconnectRegister(firstname,lastname,email,rpassword,rwindow),bg='yellow',fg='black').grid(row=8,column=0)
    tkinter.Button(rwindow, text="Cancel", command=rwindow.destroy,bg='yellow',fg='black').grid(row=8,column=2)    
    rwindow.mainloop()


    
window=tkinter.Tk()
window.title('Open Weather')
window.geometry('280x300')
window.configure(background='black')
userid=tkinter.StringVar()
password=tkinter.StringVar()
remember=tkinter.StringVar()
language=tkinter.StringVar()
tkinter.Label(window,text='Welcome to Open Weather',bg='black',fg='yellow').grid(row=0,column=0)
tkinter.Label(window,text='User ID',bg='black',fg='yellow').grid(row=1,column=0)
tkinter.Entry(window,textvariable=userid).grid(row=1,column=1)
tkinter.Label(window,text='Password',bg='black',fg='yellow').grid(row=2,column=0)
tkinter.Entry(window,show="*",textvariable=password).grid(row=2,column=1)
tkinter.Label(window,text='',bg='black',fg='yellow').grid(row=3,column=0)
tkinter.Button(window,text="Login",bg='yellow',fg='black',command=lambda: login(userid,password)).grid(row=4,column=0)
tkinter.Button(window,text="Register",bg='yellow',fg='black',command=register).grid(row=4,column=1)
tkinter.Checkbutton(window,text='Remember me', variable=remember,onvalue='yes',offvalue='no',bg='black',fg='yellow').grid(row=5,column=0)
tkinter.Radiobutton(window,text='English',variable=language,value='English').grid(row=6,column=0)
tkinter.Radiobutton(window,text='Hindi',variable=language,value='Hindi').grid(row=6,column=1)

window.mainloop()
