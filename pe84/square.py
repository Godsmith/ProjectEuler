from enum import Enum


class Square:
    class Type(Enum):
        GO = 1,
        CC = 2,
        CH = 3,
        G2J = 4,
        JAIL = 5,
        R = 6,
        U = 7,
        C = 8,
        E = 9,
        H = 10

    def __init__(self, type):
        self.type = type

    def __str__(self, *args, **kwargs):
        return self.type.name

    @staticmethod
    def create(type: Type):
        return Square(type)
