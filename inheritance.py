# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 03:21:00 2022

@author: Admin
"""

class Animal:  
    def speak(self):  
        print("Animal Speaking")    
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
d = Dog()  
d.bark()  
d.speak()  