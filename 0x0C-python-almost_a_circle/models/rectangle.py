#!/usr/bin/python3
''' This class  inherits from Base '''
from models.base import Base


class Rectangle(Base):
    ''' Child class '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Class constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width of this rectangle '''
        return self.__width

    @width.setter
    def width(self, value):
        self.test_integer('width', value, False)
        self.__width = value

    @property
    def height(self):
        ''' height of this rectangle '''
        return self.__height

    @height.setter
    def height(self, value):
        self.test_integer('height', value, False)
        self.__height = value

    @property
    def x(self):
        ''' x of this rectangle '''
        return self.__x

    @x.setter
    def x(self, value):
        self.test_integer('x', value)
        self.__x = value

    @property
    def y(self):
        ''' y of this rectangle '''
        return self.__y

    @y.setter
    def y(self, value):
        self.test_integer('x', value)
        self.__y = value

    def test_integer(self, name, value, eq=True):
        ''' Method to validare the value '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if eq and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        elif not eq and value <= 0:
            raise ValueError('{} must be > 0'.format(name))
