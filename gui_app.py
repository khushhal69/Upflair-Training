# GUI - graphical User Interface
#Libraries
#PyQT
#Turtle
#tkinter
 
import tkinter as ttk
app = ttk.Tk()
app.title('My App')
app.geometry('600x400')
ttk.Label(app, text = 'a simple text label').place(x=50,y=30)
ttk.Label(app,text='Nothing').place(x=300,y=200)







app.mainloop()