#!/usr/bin/env python3
def animal_voice(animal):
    animal.voice()

class Duck():
    def voice(self):
        print("quack")

class Dog():
    def voice(self):
        print("bow-wow")

class Cow():
    def voice(self):
        print("moo")

for animal in Duck(), Dog(), Cow():
    animal_voice(animal)
