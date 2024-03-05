import tkinter as tk
from tkinter import ttk, StringVar


mainwindow = tk.Tk()
mainwindow.title("Sensex/Nifty Live Stock Market Update")

columns = ("Nifty", "Nifty_Time", "Sensex", "Sensex_Time")

tree = ttk.Treeview(mainwindow, columns=columns, show="headings")
tree.heading("Nifty", text="Nifty")
tree.heading("Nifty_Time", text="Nifty_Time")
tree.heading("Sensex", text="Sensex")
tree.heading("Sensex_Time", text="Sensex_Time")

tree.place(x=10, y=10)


mainwindow.geometry("825x255")
mainwindow.resizable(False, False)


mainwindow.mainloop()
