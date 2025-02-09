'''
Write a function that stutters a word as if someone is struggling to read it. 
The first two letters are repeated twice with an ellipsis ... and space after each, and then the word is pronounced with a question mark ?.
'''

def stutter(word):
    if len(word) < 2:
        return f"{word}... {word}... {word}?"
    
    dos = word[:2]
    return f"{dos}... {dos}... {word}?"

x = stutter('hola')
print(x)