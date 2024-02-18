#!/usr/bin/python3
"""Defines a class called Base"""
import json
import turtle


class Base:
    """class with a private attr, it will be
    the base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor that determines the id
        of the instance

        Args:
            id: the id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """method that returns the json representations
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        to a file"""
        lis = []
        if list_objs is None:
            return
        for i in list_objs:
            lis.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as file0:
            file0.write((cls.to_json_string(lis)))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the rectangles and squares"""
        turtle.Screen()
        for r in list_rectangle:
            turtle.setpos(r.x, r.y)
            turtle.color(green)
            turtle.pendown()
            for i in range(2):
                turtle.forward(r.width)
                turtle.right(90)
                turtle.down(r.height)
                turtle.right(90)
            turtle.penup()
        for s in list_squares:
            turtle.setpos(s.x, s.y)
            turtle.color(red)
            turtle.pendown()
            for j in range(4):
                turtle.forward(s.size)
                turtle.right(90)
        turtle.done()
