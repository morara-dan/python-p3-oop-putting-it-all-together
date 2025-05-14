#!/usr/bin/env python3

class Shoe:


    def __init__(self, brand, size, condition=None):
        self._brand = brand
        self._size = size
        self._condition = condition

    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand
        
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    @property
    def condition(self):
        return self._condition

    @condition.setter
    def condition(self, condition):
        self._condition = condition

    def cobble(self):
        self._condition = "New"
        print("Your shoe is as good as new!")
