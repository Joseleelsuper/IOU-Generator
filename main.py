"""
The main module for the application.
"""
from src.ui import UI
import tkinter as tk

def main():
    ui = UI()
    root = tk.Tk()
    root.destroy()
    ui.run()

if __name__ == "__main__":
    main()