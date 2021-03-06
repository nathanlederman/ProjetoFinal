from tkinter import *
from PIL import Image, ImageTk
janela = Tk()
janela.configure(background="black")




class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("topa_ou_nao_topa.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)



e = Example(janela)
e.pack(fill=BOTH, expand=YES)
janela.geometry("1200x900+200+200")
janela.title("background")
janela.mainloop()