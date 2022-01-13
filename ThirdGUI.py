import tkinter as tk
import tkinter.messagebox as tkmsg
from PIL import ImageTk
from PIL import Image
import algo
import Graph
import FifthGUI


class ThirdGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.minsize(850,600)
        self.maxsize(850,590)
        self.title("Welcome To Algo Trader")
        self.make_title()

    def make_title(self):
        tk.Label(self,text="Please Enter the Following Details",font="CopperplateGothicBold 20 bold",pady=25,\
            fg="peachpuff",bg="black").pack(side=tk.TOP,fill=tk.BOTH)
        self.create_frames()

    def create_frames(self):
        self.center_frame=tk.Frame(self,borderwidth=3,relief=tk.FLAT,height=600,width=850,bg="black")
        self.center_frame.pack(side=tk.LEFT,fill=tk.BOTH)
        self.create_canvas()

    def create_canvas(self):
        self.bg_center = tk.PhotoImage(file = "center.png")
        self.canvas_center = tk.Canvas( self.center_frame, width = 850,height = 600,highlightthickness=0,bg="black")
        self.canvas_center.pack(fill = tk.BOTH, expand = True)
        self.canvas_center.create_image( 0, 0, image = self.bg_center, anchor = "nw")

        self.create_buttons()

    def create_buttons(self):
        self.canvas_center.create_text(425,400,text="!!  Make Sure You Enter Proper Details  !!\n",font="Georgia 12 bold underline"\
            ,fill="red")
        def exception_handling():
            if self.amountval.get() == 0.0:
              tkmsg.showwarning(title="Enter Amount",message="Please Enter Amount")
            if self.periodval.get() == 0:
              tkmsg.showwarning(title="Enter Period",message="Please Enter Time Period ")
            if self.rfval.get() == 0.0:
              tkmsg.showwarning(title="Enter Risk Factor",message="Please Enter Risk Factor")
            
            def check_float(potential_float):
                try:
                   float(potential_float)
                   return True
                except ValueError:
                   return False
            if check_float(self.amountval.get())!=True:
                tkmsg.showerror(title="Enter Amount",message="Please Enter Valid Amount")
            if check_float(self.periodval.get())!=True:
                tkmsg.showerror(title="Enter Period",message="Please Enter Valid Time Period")
            elif float(self.periodval.get())>60:
                tkmsg.showinfo(title="Sorry for Inconvienence",message="Sorry, We Only Have Data For 60 Months. Please Enter Time Period Less Than 60 ")
            if check_float(self.rfval.get())!=True:
                tkmsg.showerror(title="Enter Risk Factor",message="Please Enter Valid Risk factor ")
            elif float(self.rfval.get())>100:
                tkmsg.showerror(title="Enter Risk Factor",message="Percentage Cannot be more than 100 ")
            self.submit()
        b1=tk.Button(self,text="Continue",font="Georgia 10",command=exception_handling,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED)
        b1_canvas=self.canvas_center.create_window(425,450,window=b1)

        self.canvas_center.create_text(425,60,text="Enter the Amount in Rupees\n",font="Georgia 17 bold "\
            ,fill="cyan")
        self.canvas_center.create_text(425,70,text="(Amount is the total Capital what You want to INVEST)",font="Georgia 10  "\
            ,fill="greenyellow")
        self.canvas_center.create_text(425,180,text="Enter the time Period in Months\n",font="Georgia 17 bold"\
            ,fill="cyan")
        self.canvas_center.create_text(425,190,text="(Time Period is the Duration for which you want to INVEST Your Money)",font="Georgia 10  "\
            ,fill="greenyellow")
        self.canvas_center.create_text(425,300,text="Enter the Risk Factor in Percentage\n",font="Georgia 17 bold "\
            ,fill="cyan")
        self.canvas_center.create_text(425,320,text="    (Risk Factor is the value on scale 0-100 indicating\n\
            the Maximum loss you can bear on your investment)",font="Georgia 10  "\
            ,fill="greenyellow")
        self.canvas_center.create_text(425,500,text="As of Current Available Data, Maximum Time Period Can Only Be 60 Months ",font="Georgia 10 bold "\
            ,fill="greenyellow")

        self.amountval=tk.DoubleVar()
        self.periodval=tk.IntVar()
        self.rfval=tk.DoubleVar()

        amountentry=tk.Entry(self,textvariable=self.amountval,relief=tk.FLAT)
        periodentry=tk.Entry(self,textvariable=self.periodval,relief=tk.FLAT)
        rfentry=tk.Entry(self,textvariable=self.rfval,relief=tk.FLAT)

        self.canvas_center.create_window(425,100, window=amountentry)
        self.canvas_center.create_window(425,220, window=periodentry)
        self.canvas_center.create_window(425,360, window=rfentry)
        
    
    def submit(self):
        Amount=float(self.amountval.get())
        self.period=int(self.periodval.get())
        self.rf=float(self.rfval.get())
        try:
            d= algo.algo(Amount,self.period,self.rf)
            Graph.plotting(d)
            self.destroy()
            fifth=FifthGUI.FifthGUI(d,Amount)
            fifth.mainloop()
        
        except:
            tkmsg.showerror(title="No Stock Found",message="No suitable stock was found for the given set of data")
        # print(d)
        
        
        # return (Amount,period,rf)
        

        

# if __name__=="__main__":
#   third= ThirdGUI()
# #   Amount,period,rf=third.submit()
#   third.mainloop()