import tkinter as tk
from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import ttk, StringVar


mainwindow = tk.Tk()
mainwindow.title("Sensex/Nifty Live Stock Market Update")


def get_nifty_date_from_weburl():
    nifty_url = "https://www.moneycontrol.com/indian-indices/nifty-50-9.html"
    page = urlopen(nifty_url)
    soup = BeautifulSoup(page , 'html.parset')


    sensex_url = "https://www.moneycontrol.com/indian-indices/sensex-4.html"







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
