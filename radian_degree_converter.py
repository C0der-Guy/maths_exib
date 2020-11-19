from tkinter import * #Importing tkinter which is used for making GUI programs

window = Tk()
window.title("Degree and Radian Converter")#Title of the window
pi=3.14 #Declaring the value of pi

def deg_to_rad():
    radian=float(e2_value.get())*pi/180 #Converting degree measure to radian using the equation rad=pi/180 x degree
    t1.delete("1.0", END) #Deleting the last converted radian value
    t1.insert(END,radian) #Printing the calculated radian measure

def rad_to_deg():
    degree=float(e5_value.get())*180/pi #Converting radian measure to degree using the equation degree=108/pi x rad
    t2.delete("1.0", END) #Deleting the last converted degree value
    t2.insert(END,degree) #Printing the calculated degree measure

deg = Label(window,text="Degree to Radian Converter")
e1 = Label(window, text = "Enter the Degree measure") 
e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value) #Taking the Degree measure from the user
e3 = Label(window, text = 'Radian Measure') 

blank = Label(window, text='\n')

rad = Label(window, text="Radian to Degree Converter") 
e4 = Label(window, text = "Enter the Radian measure") 
e5_value = StringVar() 
e5 = Entry(window, textvariable = e5_value) #Taking the Radian measure from the user
e6 = Label(window, text = 'Degree Measure') 

t1 = Text(window, height = 1, width = 20) 
t2 = Text(window, height = 1, width = 20) 

#Button used to print the result
b1 = Button(window, text = "Convert", command = deg_to_rad) 
b2 = Button(window, text= "Convert", command=rad_to_deg) 

#Postion of the degree measure widgets
deg.grid(row=0,column=0) 
e1.grid(row = 1, column = 0) 
e2.grid(row = 1, column = 1) 
e3.grid(row = 2, column = 0)

blank.grid(row=4,column=0)

#Position of the radian measure widgets
rad.grid(row = 5, column=0)
e4.grid(row = 6, column = 0) 
e5.grid(row = 6, column = 1)
e6.grid(row = 7, column = 0)

t1.grid(row = 3, column = 0) 
t2.grid(row = 8, column = 0) 

#Position of the calculate buttons
b1.grid(row = 1, column = 2) 
b2.grid(row=6,column=2)

window.mainloop() 
