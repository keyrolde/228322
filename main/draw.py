from tkinter import Tk, ttk, Canvas, Frame

# from main.dot import Dot

from figure import Figure, Dot

root = Tk()
root.title("да")
root.geometry("800x600")
root.resizable(False, False)


class Risovalka(Frame):
    def __init__(self):
        self.btn = ttk.Button(text="передвинуть", command=self.click_button)
        self.btn.pack()
        self.figure = Figure([Dot(), Dot(), Dot()])
        self.canvas = Canvas(root, width=400, height=400, bg="gray", cursor="pencil")
        self.triangle = None
        self.do_triangle()
        self.en1 = ttk.Entry()
        self.en1.pack()
        self.en2 = ttk.Entry()
        self.en2.pack()



    def do_triangle(self):
        self.triangle = self.canvas.create_polygon(self.figure.get_dot_list(), width=2, fill="white", outline="black")
        self.canvas.pack()
       def click_button(self):
        self.canvas.move(self.triangle, self.en1.get(), self.en2.get())


a = Risovalka()






root.mainloop()