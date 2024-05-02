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
        self.do_triangle()


    def do_triangle(self):
        self.canvas.create_polygon(self.figure.get_dot_list(), width=2, fill="white", outline="black")
        self.canvas.pack()
    def click_button(self):
        print("авд")
        self.canvas.delete("all")
        self.figure = Figure([Dot(), Dot(), Dot()])
        self.do_triangle()


a = Risovalka()

en1 = ttk.Entry()
# en1.place(x=10, y=10)
en1.pack(padx=10, pady=10)




root.mainloop()