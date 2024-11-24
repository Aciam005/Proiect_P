import numpy as np
import collections
import pandas as pd
import string as string
import tkinter as tk

def RemovePunctuation(sentence):
    sentence = sentence.translate(str.maketrans('','',string.punctuation))
    return sentence
    
    

#           This function extracts words from a string
#           and returns them as an array
def ExtractWords(sentence):
    
    sentence = RemovePunctuation(sentence)
    
    #TODO:Add a word filter (an 'ignore' list)
    str
    
    sentence = str.lower(sentence)
    return sentence.split()

#           This function extracts words from a list,and puts them in a dictionary
#           returns the dictionary
def CalculateBOW(wordList):
    l_dict = dict.fromkeys(wordList ,0)
    
    for word in wordList:
        l_dict[word] = wordList.count(word)
    
    return l_dict


#Main function begins here

#className = window title
gui = tk.Tk()

gui.title("Proiect Python | Byte-Builders")

ex = "MUIE FURTUNA! MILSUGI..."

wordList = ExtractWords(ex)
dictionary = CalculateBOW(wordList=wordList)
print(dictionary)

textInput = tk.Text(gui,width = 20 , height=3)
textInput.pack()


gui.mainloop()