from random import randint
class Dot:
    def __init__(self, x:int= None, y:int= None):
        """
        создание точки
        :param x: параметр х
        :param y: параметр у
        """
        print("constructor")
        self.x = x if x else randint(200,400)
        self.y = y if y else randint(200,400)
        self.cords()
        # self.summm_dot()


    def cords(self):
        print(f"[{self.x};{self.y}]")



