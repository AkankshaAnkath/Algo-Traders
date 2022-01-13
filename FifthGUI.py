import tkinter as tk
from tkinter.constants import BOTTOM
import tkinter.messagebox as tkmsg
import math
# from PIL import ImageTk
# from PIL import Image
import pandas as pd
from tkinter import PhotoImage, ttk
import os
import webbrowser
from googlesearch import search
import algo
from ThirdGUI import *
import SeventhGUI

class FifthGUI(tk.Tk):
    def __init__(self,df,Amount):
        # print(Amount,rf,period)
        # self.Amount=ThirdGUI.Amount
        # self.period=ThirdGUI.period
        # self.rf=ThirdGUI.rf

        super().__init__()
        self.df=df
        self.Amount=Amount
        
        self.geometry("850x600")
        self.minsize(850,690)
        # self.maxsize(850,600)
        self.title("Welcome To Algo Trader")
        self.no_stocks=math.floor(self.Amount/float(self.df.iloc[0,-3]))
        self.top()

    def top(self):
        self.top_frame=tk.Frame(self,bg="indigo").pack(fill=tk.BOTH)
        self.bottom_frame=tk.Frame(self,bg="indigo").pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="Name of the recommended Stock :",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=self.df.iloc[0,0],font="Calibri 12 bold",fg="black",bg="lavender",padx=5,pady=5).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=f"Latest Stock Price as of {self.df.columns[-3]}:",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=self.df.iloc[0,-3],font="Calibri 12 bold",fg="black",bg="lavender",padx=5,pady=5).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="Number of Stocks that can be purchased by You:",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text=self.no_stocks,font="Calibri 12 bold",fg="black",bg="lavender",padx=5,pady=5).pack(fill=tk.BOTH)
        tk.Label(self.top_frame,text="For More Information about the stock,click below:",font="Georgia 12 bold",fg="white",bg="indigo",padx=7,pady=7).pack(fill=tk.BOTH)
        def searching():
            query = f"{self.df.iloc[0,0]} yahoo finance"
            for j in search(query, tld="co.in", num=1, stop=1, pause=2):
                webbrowser.open(j)
        tk.Button(self.top_frame,text="Click Here",command=searching,font="Calibri 12 bold",padx=5,pady=5,bg="lavender").pack(fill=tk.BOTH)
        self.bottom()

    def bottom(self):
        self.img=tk.PhotoImage(file="recommend.png")
        # can=tk.Canvas(self,bg="red",height=500,width=850)
        # can.grid(row=4,column=0)
        # can.create_image(0,0,image=self.img)
           
        tk.Label(self.bottom_frame,image=self.img,bg="indigo").pack(fill=tk.BOTH)
        os.remove("recommend.png")
        def submit():
            self.destroy()
            seventh=SeventhGUI.SeventhGUI()
            seventh.mainloop()
        tk.Button(self.bottom_frame,text="Next!",font="Georgia 10 bold",fg="darkred",bg="lightcoral",command=submit,height=5,width=10).pack(fill=tk.BOTH)



# if __name__=="__main__":
#     df=algo.algo(Amount,period,rf)
#     fifth= FifthGUI(df,Amount,period,rf)
#     fifth.mainloop()