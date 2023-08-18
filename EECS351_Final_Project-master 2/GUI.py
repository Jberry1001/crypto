import subprocess, sys
import tkinter as tk
import yfinance as yf
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

r = tk.Tk()
r.geometry('750x600')
r.title("Financial Simulator")

def source():
    subprocess.Popen('main.py', shell=True)
    subprocess.call(["python", "main.py"])

button = tk.Button(r, text='Run', width=500, font=("Arial Bold", 50), command=source)
button2 = tk.Button(r, text='Stop', width=500, font=("Arial Bold", 50), command=r.destroy)

txt = tk.Entry(r, text="Stock Choice")

def clicked():
    res = "Welcome to " + txt.get()
    tk.configure(text=res)

txt = tk.Entry(r, text="Stock Choice")
#btn_input = tk.Entry(r, text="Stock Choice", width=500, font=("Arial Bold", 50), command=clicked)
button.pack()
button2.pack()
txt.pack()
r.mainloop()

# class Window(QMainWindow):
#
#     def __init__(self):
#         super(Window, self).__init__()
#         self.setGeometry(50, 50, 500, 300)
#         self.setWindowTitle("Financial Simulator")
#
#         self.home()
#
#     def home (self):
#         btn_run = QPushButton("Run", self)
#         btn_run.clicked.connect(self.execute)
#         self.show()
#
#     def home2 (self):
#         btn_stop = QPushButton("Stop", self)
#         btn_stop.clicked.connect(self.destroy)
#         self.show()
#
#     def execute(self):
#         subprocess.Popen('main.py', shell=True)
#         subprocess.call(["python", "main.py"])
#
# if not QApplication.instance():
#     app = QApplication(sys.argv)
# else:
#     app = QApplication.instance()
#
# GUI = Window()
# app.exec_()