# view/canvas_view.py

import tkinter as tk

class CanvasView:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, bg="white", width=1000, height=800)
        self.canvas.pack()
        self.view_model = None  # Изначально view_model не установлен

    def set_view_model(self, view_model):
        self.view_model = view_model  # Устанавливаем view_model отдельно

    def bind_events(self):
        # Привязываем события к методам view_model
        self.canvas.bind("<Button-1>", self.view_model.on_draw_line)
        self.canvas.bind("<KeyPress>", self.view_model.on_key_press)
        self.canvas.bind("<KeyRelease>", self.view_model.on_key_release)
        self.canvas.bind("<Motion>", self.view_model.on_delete_line_under_cursor)
        self.canvas.focus_set()
        
    def draw_line(self, x1, y1, x2, y2, width=5):
        return self.canvas.create_line(x1, y1, x2, y2, width=width)

    def delete_line(self, line_id):
        self.canvas.delete(line_id)
