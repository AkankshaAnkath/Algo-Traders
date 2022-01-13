import tkinter as tk
import tkinter.messagebox as tkmsg
# from PIL import ImageTk
# from PIL import Image
import pandas as pd
from tkinter import ttk
import desired_plot
import SixthGUI

class FourthGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.minsize(850,600)
        self.maxsize(850,600)
        self.title("Welcome To Algo Trader")
        self.make_title()

    def make_title(self):
        tk.Label(self,text="Please select the Desired Stock",font="CopperplateGothicBold 20 bold",pady=25,\
            fg="peachpuff",bg="black").pack(side=tk.TOP,fill=tk.BOTH)
        self.create_frames()
    
    def create_frames(self):
        self.center_frame=tk.Frame(self,borderwidth=3,relief=tk.FLAT,height=600,width=850,bg="black")
        self.center_frame.pack(side=tk.LEFT,fill=tk.BOTH)
        self.create_canvas()

    def create_canvas(self):
        self.bg_center = tk.PhotoImage(file = "4.png")
        self.canvas_center = tk.Canvas( self.center_frame, width = 850,height = 600,highlightthickness=0,bg="black")
        self.canvas_center.pack(fill = tk.BOTH, expand = True)
        self.canvas_center.create_image( 0, 0, image = self.bg_center, anchor = "nw")
        self.drop_down()

    def drop_down(self):
        df_original=pd.read_csv('Data.csv')
        df=df_original.copy(True)
        company_names=[]
        
        for i in range(1,len(df)):
            company_names.append(df.iloc[i,0])
        
        self.company=tk.StringVar()
        self.company.set("Name of the company")

        drop = tk.OptionMenu( self , self.company , *company_names )

        s = ttk.Combobox(drop, textvariable=self.company, values=company_names,state='readonly',height=30,width=50)
        s.pack()
        self.canvas_center.create_text(425,60,text="Select the Stock of Your Choice",font="Georgia 14 bold "\
            ,fill="greenyellow")
        self.canvas_center.create_window(425,100, window=drop)
        self.canvas_center.create_text(200,200,text="Select the beginning Date",font="Georgia 14 bold "\
        ,fill="greenyellow")
        # self.canvas_center.create_window(425,400, window=s)
        # print(df.columns)

        self.dates=[]
        
        for i in range(1,len(df.columns)):
            self.dates.append(df.columns[i])

        self.begin_date=tk.StringVar()
        self.begin_date.set(df.columns[1])

        drop = tk.OptionMenu( self , self.begin_date , *self.dates )
        s = ttk.Combobox(drop, textvariable=self.begin_date, values=self.dates,state='readonly',height=30,width=30)
        s.pack()
        self.canvas_center.create_window(200,230, window=drop)

        self.canvas_center.create_text(650,200,text="Select the End Date",font="Georgia 14 bold "\
        ,fill="greenyellow")

        self.end_date=tk.StringVar()
        self.end_date.set(df.columns[-1])

        drop = tk.OptionMenu( self , self.end_date , *self.dates )
        s = ttk.Combobox(drop, textvariable=self.end_date, values=self.dates,state='readonly',height=30,width=30)
        s.pack()

        self.canvas_center.create_window(650,230, window=drop)

        def exception_handling():
            begin_index=self.dates.index(self.begin_date.get())
            end_index=self.dates.index(self.end_date.get())
            if (begin_index>=end_index):
                tkmsg.showerror(title="Invalid Response",message="Begin Date Needs To Be Before End Date")
            else:
                self.submit()
        


        b1=tk.Button(self,text="Continue",font="Georgia 10",command=exception_handling,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED)
        self.canvas_center.create_window(425,350,window=b1)

    def submit(self):
        c=self.company.get()
        bd=self.begin_date.get()
        ed=self.end_date.get()
        desired_plot.desired_plot(c,bd,ed)
        # print(self.company.get(),self.begin_date.get(),self.end_date.get())
        self.destroy()
        
        sixth=SixthGUI.SixthGUI(c,bd,ed)
        sixth.mainloop()

        

# if __name__=="__main__":
#   fourth= FourthGUI()
#   fourth.mainloop()