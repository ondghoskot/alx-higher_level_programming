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
        t = turtle.Turtle()
        t.speed(0)
        for r in list_rectangles:
            t.setpos(r.x, r.y)
            t.color("green")
            t.pendown()
            for i in range(2):
                t.forward(r.width)
                t.right(90)
                t.forward(r.height)
                t.right(90)
            t.penup()
        for s in list_squares:
            t.setpos(s.x, s.y)
            t.color("red")
            t.pendown()
            for j in range(4):
                t.forward(s.size)
                t.right(90)
            t.penup()
        turtle.done()
