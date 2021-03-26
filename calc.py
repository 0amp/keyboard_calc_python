import tkinter as tk
import tkinter.font as tkFont
from func import calc

"""

IDEAS FOR IMPROVEMENT LATER DOWN THE ROAD:
1. REFACTOR -- program is very inefficient, far too many type castings, etc
2. MAKE PROGRAM MORE MODULAR -- replace the functions with one main calc function that accepts in 
an array of functions to be performed at that set PEMDAS level
3. GUI W/ TKINTER -- 

"""
window = tk.Tk()

fontStyle = tkFont.Font(family="Roboto", size=20)

calc_entry = tk.Entry(
  fg = "blue", 
  bg = "#f5f5f5",
  font = fontStyle)
calc_entry.insert(0,">")
calc_entry.pack()
backlog = tk.Text(
  bg = "#f5f5f5",
  width = 20,
  height = 8,
  font = fontStyle)
backlog.pack()

entry = ""

def handle_enter(event):

  entry = calc_entry.get()
  backlog.insert("1.0", "\n\n")
  entry = entry[1:len(entry)]
  entry_equals = entry + " = "
  entry = "   " + str(calc(entry))
  backlog.insert("1.0", entry_equals)
  backlog.insert("2.0", entry)
  calc_entry.delete(0,"end")
  calc_entry.insert(0,">")

calc_entry.bind("<KeyPress-Return>", handle_enter)

window.mainloop()