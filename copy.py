import generatechars
import pyperclip
import random

def copy_to_clipboard(text_output):
    listOfCharacters = generatechars.generateCharacters()
    password = ""
    for i in range(int(text_output.currentText())):
        password += random.choice(listOfCharacters)
        text_output.setText(password)
    pyperclip.copy(text_output.text())