
import tkinter as tk
import tkinter.messagebox as tkmsg
from PIL import ImageTk
from PIL import Image
import SecondGUI

class FirstGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        # image=Image.open("photo.jpg")  
        # photo=ImageTk.PhotoImage(image) 
        # photo=tk.PhotoImage(file="C:\\Users\\Swaroop\\Desktop\\Algo Trader\\1.png")
        # tk.Label(self,image=photo).pack()
        # bg = tk.PhotoImage(file = "C:\\Users\\Swaroop\\Desktop\\Algo Trader\\1.png")
        # bg = bg.resize((225, 265), Image.ANTIALIAS)
        # canvas1 = tk.Canvas( self, width = 850,height = 500)
        # canvas1.pack(fill = "both", expand = True)
        # canvas1.create_image( 0, 0, image = bg, anchor = "nw")
        self.minsize(850,500)
        self.title("Welcome To Algo Trader")
        # self.wm_iconbitmap("1.ico")
        self.config(bg="lightgrey")
        self.make_title()

    def make_title(self):
        f1=tk.Frame(self)
        f1.pack(pady=15)
        title=tk.Label(f1,text="Welcome To Algo Trader",font="CopperplateGothicBold 24 bold",pady=25,bg="lightgrey",fg="black")
        title.grid(row=0)
        self.disclamer()

    def disclamer(self):
        f2=tk.Frame(self)
        f2.pack(pady=25)
        disclamer="Investments in Stock Markets are subject to market risks as well as at your own risk."
        tk.Label(f2,text=disclamer,font="Georgia 14",bg="lightgrey",fg="black").pack(anchor=tk.W,fill=tk.BOTH)
        disclamer="WE ARE NOT RESPONSIBLE FOR ANY LOSSES OR PROFITS DUE TO USAGE OF THIS SOFTWARE."
        tk.Label(f2,text=disclamer,font="Calibri 14 bold",bg="lightgrey",fg="crimson").pack(anchor=tk.W,fill=tk.BOTH)
        disclamer="Please Read All Scheme Related Documents Carefully."
        tk.Label(f2,text=disclamer,font="Georgia 14 ",bg="lightgrey",fg="black").pack(anchor=tk.W,fill=tk.BOTH)
        f3=tk.Frame(self)
        f3.pack(pady=20)
        
        off_color = "red"
        on_color = "green"
        def on_check():    #this function will run on click on checkbutton
            if self.cbVar.get() == 1:
               chbox["fg"] = on_color     # if (get current checkbutton state) is "1" then....
            else:
                chbox["fg"] = off_color
        self.cbVar = tk.IntVar()     #making variable for checkbutton
        self.cbVar.set(0)          #turning off the checkbutton (initialy)
        chbox = tk.Checkbutton(self,variable = self.cbVar,text="I agree to all the Terms and Conditions",command=on_check,\
            fg=off_color,bg="lightgrey",borderwidth=3,pady=10,font="Georgia 10" )     #making the checkbutto
        chbox.pack()

        f4=tk.Frame(self)
        f4.pack(pady=15)
        tk.Button(f4,text="Submit",font="Georgia 10",bg="lightgrey",borderwidth=3,relief=tk.RIDGE,command=self.submission).pack()
        self.names()

    def names(self):
        f5=tk.Frame(self)
        f5.pack(pady=25)
        tk.Label(self,text="This Software was made by Swaroop Talakwar,Akanksha Ankath and Nikhil Bhisle",font="Calibri 12 ",\
            bg="lightgrey",fg="black").pack(anchor=tk.S,fill=tk.X)

    def submission(self):
        if(self.cbVar.get()==0):
            tkmsg.showerror(title="Warning",message="Please accept the Terms and Conditions")
        else: 
            self.destroy()
            second=SecondGUI.SecondGUI()
            second.mainloop()

        
                


        




# root=tk.Tk()
# root.title("Two Player Chess")
# root.geometry("800x800")
# first=FirstGUI(root)
# first.mainloop()