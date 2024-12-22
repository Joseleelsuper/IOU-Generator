"""
The main module for the application.
"""
from src.ui import UI
import tkinter as tk

def main():
    ui = UI()
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    if screen_width == 1920 and screen_height == 1080:
        ui.tamx, ui.tamy = 1280, 720
    elif screen_width == 1366 and screen_height == 768:
        ui.tamx, ui.tamy = 1024, 576
    else:
        ui.tamx, ui.tamy = screen_width // 2, screen_height // 2

    root.destroy()
    ui.run()

if __name__ == "__main__":
    main()