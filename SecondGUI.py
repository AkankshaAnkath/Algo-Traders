import tkinter as tk
from tkinter.constants import ANCHOR
import tkinter.messagebox as tkmsg
from PIL import ImageTk
from PIL import Image
import ThirdGUI
import FourthGUI



class SecondGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.minsize(850,600)
        self.maxsize(850,600)
        self.title("Welcome To Algo Trader")
        
        self.make_title()
    
    # def bg_image(self):
    #     img=Image.open("C:\\Users\\Swaroop\\Desktop\\Algo Trader\\1.jpg")
    #     img=img.resize((850,500),Image.ANTIALIAS)
    #     photo=ImageTk.PhotoImage(img)

    #     F1=tk.Frame(self,width=850,height=500)
 
    #     self.make_title()

    def make_title(self):
        tk.Label(self,text="Choose any one of the Functionality",font="CopperplateGothicBold 20 bold",pady=25,\
            fg="peachpuff",bg="black").pack(side=tk.TOP,fill=tk.BOTH)
        self.create_frames()

    def create_frames(self):
        self.left=tk.Frame(self,borderwidth=3,relief=tk.FLAT,height=420,width=425,bg="black")
        self.left.pack(side=tk.LEFT,fill=tk.BOTH)
        self.right=tk.Frame(self,borderwidth=3,relief=tk.FLAT,height=420,width=425,bg="black")
        self.right.pack(side=tk.RIGHT,fill=tk.BOTH)
        self.create_canvas()

    def create_canvas(self):
        self.bg_left = tk.PhotoImage(file = "left.png")
        self.canvas_left = tk.Canvas( self.left, width = 425,height = 420,highlightthickness=0,bg="black")
        self.canvas_left.pack(fill = tk.BOTH, expand = True)
        self.canvas_left.create_image( 0, 0, image = self.bg_left, anchor = "nw")

        # canvas_line=tk.Canvas(self)
        # canvas_line.pack(fill = tk.BOTH, expand = True)
        # canvas_line.create_line(425,0,425,600,fill='white',width=5)

        self.bg_right=tk.PhotoImage(file = "right.png")
        self.canvas_right = tk.Canvas( self.right, width = 425,height = 420,bg="black",highlightthickness=0)
        self.canvas_right.pack(fill = tk.BOTH, expand = True)
        self.canvas_right.create_image( 425,0, image = self.bg_right, anchor = "ne")

        self.create_buttons()

    def create_buttons(self):
        self.canvas_left.create_text(210,150,text="Let  Us  Recommend  you  a  stock  as  \n\tper  your  Comfort",font="Georgia 14 bold"\
            ,fill="yellow")
        
        def gui3():
            self.destroy()
            third=ThirdGUI.ThirdGUI()
            third.mainloop()
        
        b1=tk.Button(self,text="Let's Go!",font="Georgia 10",command=gui3,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED)
        b1_canvas=self.canvas_left.create_window(210,300,window=b1)
        
        self.canvas_right.create_text(210,150,text="Want to Analize a Stock of Your Choice?"\
            ,font="Georgia 14 bold",fill="lawngreen")
        self.canvas_right.create_text(200,250,text="We are here to help you using previous years' \n\tperformance of the stock",\
            font="Georgia 12 bold",fill="gold")
        
        def gui4():
            self.destroy()
            Fourth=FourthGUI.FourthGUI()
            Fourth.mainloop()
        
        b1=tk.Button(self,text="Continue",font="Georgia 10",command=gui4,bg="mistyrose",fg="black",height=1,activebackground="lawngreen",borderwidth=3,relief=tk.RAISED)
        b1_canvas=self.canvas_right.create_window(210,350,window=b1)

# if __name__=="__main__":
#   first=SecondGUI()
#   first.mainloop()