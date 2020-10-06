import string
import random
from tkinter import simpledialog
import tkinter as tk
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    ROOT = tk.Tk()

    ROOT.withdraw()
    pascodelen = simpledialog.askinteger(title="Password Genrator",
                                         prompt="Enter Password length")

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    print("".join(s[0:pascodelen]))
