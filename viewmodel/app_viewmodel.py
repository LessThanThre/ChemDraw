# viewmodel/app_viewmodel.py

import math
from model.line_model import LineModel

class AppViewModel:
    def __init__(self, canvas_view):
        self.canvas_view = canvas_view
        self.line_model = LineModel()
        self.direction = 315
        self.keys = {'Up': False, 'Down': False, 'Left': False, 'Right': False, 'Z': False, 'F': False, '0': False, 'B': False, 'T': False}

    def on_draw_line(self, event):
        global direction
        x1, y1 = event.x, event.y
        x2 = x1 + 100 * math.cos(math.radians(self.direction))
        y2 = y1 + 100 * math.sin(math.radians(self.direction))

        if self.keys['B'] or self.keys['T']:
            self.draw_double_or_triple_bond(x1, y1, x2, y2)
        else:
            line = self.canvas_view.draw_line(x1, y1, x2, y2)
            self.line_model.add_line(line)

    def draw_double_or_triple_bond(self, x1, y1, x2, y2, offset=8):
        line1 = self.canvas_view.draw_line(x1, y1, x2, y2)
        self.line_model.add_line(line1)

        dx = offset * math.sin(math.radians(self.direction))
        dy = offset * math.cos(math.radians(self.direction))

        line2 = self.canvas_view.draw_line(x1 + dx, y1 - dy, x2 + dx, y2 - dy)
        self.line_model.add_line(line2)

        if self.keys['T']:
            line3 = self.canvas_view.draw_line(x1 - dx, y1 + dy, x2 - dx, y2 + dy)
            self.line_model.add_line(line3)

    def on_key_press(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = True
        if self.keys['Z']:
            self.delete_last_line()
        self.update_direction()

    def on_key_release(self, event):
        if event.keysym in self.keys:
            self.keys[event.keysym] = False
        self.update_direction()

    def update_direction(self):
        global direction
        if self.keys['Up'] and not self.keys['Left'] and not self.keys['Right']:
            self.direction = 270
        elif self.keys['Down'] and not self.keys['Left'] and not self.keys['Right']:
            self.direction = 90
        elif self.keys['Left'] and not self.keys['Up'] and not self.keys['Down']:
            self.direction = 180
        elif self.keys['Right'] and not self.keys['Up'] and not self.keys['Down']:
            self.direction = 0
        elif self.keys['Left'] and self.keys['Up'] and not self.keys['Down']:
            self.direction = 225
        elif self.keys['Left'] and not self.keys['Up'] and self.keys['Down']:
            self.direction = 135
        elif self.keys['Right'] and self.keys['Up'] and not self.keys['Down']:
            self.direction = 315
        elif self.keys['Right'] and not self.keys['Up'] and self.keys['Down']:
            self.direction = 45

    def on_delete_line_under_cursor(self, event):
        if  self.keys['F']:
            x, y = event.x, event.y
            for line in self.line_model.get_lines():
                coords = self.canvas_view.canvas.coords(line)
                if coords:
                    x1, y1, x2, y2 = coords
                    if (min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)):
                        self.canvas_view.delete_line(line)
                        self.line_model.get_lines().remove(line)

    def delete_last_line(self):
        line = self.line_model.delete_last_line()
        if line:
            self.canvas_view.delete_line(line)
