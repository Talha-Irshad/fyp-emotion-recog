import tkinter as tk
from tkinter import ttk
import subprocess
import os

root = tk.Tk()
root.geometry("1200x600")


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=1)


root.title("Emotion Recognition System")
def start_recog():
    subprocess.call("emotion-recog.py",shell=True)
def open_logs():
    os.startfile('logs.txt')
def exit_window():
    root.destroy()


# Empty line:
emptylabel1 = tk.Label(root, height=2).grid(row=0, column=1)

# Heading:
label1 = tk.Label(root, text="Emotion Recognition System",
                  font=("Arial", 25)).grid(row=1, column=1, pady=20)

# Empty line:
emptylabel2 = tk.Label(root, height=2).grid(row=2, column=1)

# Buttons:
button1 = tk.Button(root, text="Start Emotion Recognition",command=start_recog,
                    font=("Arial", 15)).grid(row=3, column=1, pady=5, ipadx=10, ipady=10)

button2 = tk.Button(root, text="See Logs", command=open_logs,
                    font=("Arial", 15)).grid(row=4, column=1, pady=5, ipadx=10, ipady=10)

button3 = tk.Button(root, text="How it works?",
                    font=("Arial", 15)).grid(row=5, column=1, pady=5, ipadx=10, ipady=10)

button4 = tk.Button(root, text="Exit", command=exit_window,
                    font=("Arial", 15)).grid(row=6, column=1, pady=5, ipadx=10, ipady=10)

# Empty line:
emptylabel3 = tk.Label(root, height=2).grid(row=7, column=1)

# Credits:
label2 = tk.Label(root, text="Developed By", font=(
    "Arial", 12)).grid(row=8, column=1, pady=5)
label3 = tk.Label(root, text="Talha Irshad - EP 1849122",
                  font=("Arial", 10)).grid(row=8, column=1, pady=3, sticky=tk.S)
label4 = tk.Label(root, text="Sameer Siddiqui - EP 1849063",
                  font=("Arial", 10)).grid(row=10, column=1, pady=3, sticky=tk.S)
label5 = tk.Label(root, text="Zeeshan Noorullah - EP 1849137",
                  font=("Arial", 10)).grid(row=11, column=1, pady=3, sticky=tk.S)
label6 = tk.Label(root, text="Abdul Wahab - EP 1849003",
                  font=("Arial", 10)).grid(row=12, column=1, pady=3, sticky=tk.S)


root.mainloop()
