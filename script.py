import sys

print(sys.version)
print(sys.executable)

def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting

print(greet('Otto'))
print(greet('Linda Mausi'))

name = input("What is your name? ")
print("Hello,", name)