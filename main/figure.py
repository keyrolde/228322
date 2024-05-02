from typing import List

from dot import Dot


class Figure:
    def __init__(self, dot_list: List[Dot]):
        self.dot_list = dot_list

    def get_dot_list(self):
        result = []
        for dot in self.dot_list:
            result.append(dot.x)
            result.append(dot.y)
        return result

    def move_to_dot(self):
        pass

