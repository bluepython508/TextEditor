#A simple text editor
from guizero import App, Box, Text, MenuBar
from tkinter.filedialog import FileDialog
from tkinter import Label, LEFT, StringVar

def saveas():
	global filename
	
	
def save():
	pass
def openfile():
	pass
	





keyreplace = {
"\x08":"\b",
"\r":"\n"
}
CURSOR = '|'
def keybind(event):
	global text
	letter = (str(event.char))
	if letter in keyreplace.keys():
		letter = keyreplace[letter]
	if letter == '\b':
		text= text[:-1]
	else:
		text += letter
	text += CURSOR
	textshow.configure(text=text)
	text = text[:-1]
	
	


def mainwindow():
	global text, filename
	filename = ''
	text = ''
	app = App('TextEdit')
	window = Box(app)
	menu = MenuBar(app, ['File'], [[['Save', save], ['Save As', saveas],['Open', openfile]]])
	textshow = Text(window)
	app.bind("<Key>", keybind)
	return app, textshow

app, textshow = mainwindow()

app.display()
