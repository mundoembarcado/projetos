from pynput.keyboard import Key, Controller
f = open("demofile.txt", "r")
texto = f.read()


keyboard = Controller()


# Press and release space
keyboard.type(texto)

#code
#https://www.codegrepper.com/code-examples/python/py+keyboard



