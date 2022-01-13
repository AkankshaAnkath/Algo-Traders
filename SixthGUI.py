import tkinter as tk
from tkinter.constants import ANCHOR
import tkinter.messagebox as tkmsg
from PIL import ImageTk
from PIL import Image
import SeventhGUI
import os
import webbrowser
from googlesearch import search

class SixthGUI(tk.Tk):
    def __init__(self,company,start_date,end_date):
        super().__init__()
        self.company=company
        self.start_date=start_date
        self.end_date=end_date
        self.geometry("850x600")
        self.minsize(850,690)
        self.title("Welcome To Algo Trader")
        self.top()

    def top(self):
        self.top_frame=tk.Frame(self,bg="indigo").pack(fill=tk.BOTH)
        self.bottom_frame=tk.Frame(self,bg="indigo").pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="Name of the Selected Stock :",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=self.company,font="Calibri 12 bold",fg="black",bg="lavender",padx=5,pady=5).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="Start Date:",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=self.start_date,font="Calibri 12 bold",fg="black",bg="lavender",padx=5,pady=5).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="End Date:",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=self.end_date,font="Calibri 12 bold",fg="black",bg="lavender",padx=5,pady=5).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="For More Information about the stock,click below:",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        def searching():
            query = f"{self.company} yahoo finance"
            for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(j)
        tk.Button(self.top_frame,text="Click Here",command=searching,font="Calibri 12 bold",padx=5,pady=5,bg="lavender").pack(fill=tk.BOTH)
        self.bottom()

    def bottom(self):
        self.img=tk.PhotoImage(file="desired.png")
        tk.Label(self.bottom_frame,image=self.img,bg="indigo").pack(fill=tk.BOTH)
        os.remove("desired.png")
        def submit():
            self.destroy()
            seventh=SeventhGUI.SeventhGUI()
            seventh.mainloop()
        tk.Button(self.bottom_frame,text="Next!",font="Georgia 10 bold",fg="darkred",bg="lightcoral",command=submit,height=5,width=10).pack(fill=tk.BOTH)

    
