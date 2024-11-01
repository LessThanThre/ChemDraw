# view/app_view.py

import tkinter as tk
from view.canvas_view import CanvasView

class AppView:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CHEMPAINT VER 0.0.0")
        self.canvas_view = CanvasView(self.root)  # Создаем CanvasView без view_model

    def run(self):
        self.root.mainloop()
