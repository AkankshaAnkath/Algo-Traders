import tkinter as tk
import tkinter.messagebox as tkmsg
import SecondGUI

class SeventhGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.minsize(800,600)
        self.maxsize(800,600)
        self.title("Welcome To Algo Trader")
        self.create_canvas()

    def create_canvas(self):
        self.bg_center = tk.PhotoImage(file = "final.png")
        self.canvas_center = tk.Canvas( self, width = 850,height = 600,highlightthickness=0,bg="black")
        self.canvas_center.pack(fill = tk.BOTH, expand = True)
        self.canvas_center.create_image( 0, 0, image = self.bg_center, anchor = "nw")
        self.text()

    def text(self):
        self.canvas_center.create_text(425,100,text="THANK YOU FOR CHOOSING ALGO TRADERS\n",font="Georgia 17 bold",fill="maroon")
        self.feedback()

    def feedback(self):
        
        self.canvas_center.create_text(400,210,text="Share your experience",font="Georgia 14 bold "\
            ,fill="maroon")

        self.FeedBack=tk.StringVar()
        enter=tk.Entry(self,textvariable=self.FeedBack,relief=tk.FLAT)
        self.canvas_center.create_window(400,250, window=enter,height=30,width=150)
        def msg():
          if(self.FeedBack.get()!=""):
            tkmsg.showinfo(title="Hope you enjoyed!",message="We will note your response!")
            text_file = open("feedback.txt", "a")
            text_file.write(self.FeedBack.get()+"\n")
            text_file.close()
            self.destroy()
          else:
            tkmsg.showinfo(title="Hope you enjoyed!",message="Please Enter your FeedBack!")

        b2=tk.Button(self,text="SUBMIT",font="Georgia 10",command=msg,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED)
        b2_canvas=self.canvas_center.create_window(400,290,window=b2)
        self.restart()

    def restart(self):
        self.canvas_center.create_text(400,400,text="Press the below button to Start Again",font="Georgia 14 bold",fill="maroon")
        def restarting():
            self.destroy()
            second=SecondGUI.SecondGUI()
            second.mainloop()
        
        b1=tk.Button(self,text="Restart Again",font="Georgia 10",command=restarting,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED)
        b1_canvas=self.canvas_center.create_window(400,440,window=b1)
        
        
        self.quit_button()


    def quit_button(self):
        def end():
          self.destroy()
          
        b1=tk.Button(self,text="QUIT",font="Georgia 10",command=end,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED,width=10)
        b1_canvas=self.canvas_center.create_window(400,530,window=b1)

        
    
# if __name__=="__main__":
#     final= SeventhGUI()
#     final.mainloop()

  


