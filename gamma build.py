import tkinter as tk
import math

direction = 315
keys = {'Up': False, 'Down': False, 'Left': False, 'Right': False, 'Z': False, 'F': False, '0': False, 'B': False, 'T': False}
lines = []  # Список для хранения линий

def draw_line(event):
    global direction
    x1, y1 = event.x, event.y
    x2 = x1 + 100 * math.cos(math.radians(direction))
    y2 = y1 + 100 * math.sin(math.radians(direction))
    
    # Если клавиша 'B' зажата, рисуем двойную линию
    if keys['B']:
        double_bond(x1, y1, x2, y2)
    # Если клавиша 'T' зажата, рисуем тройную линию
    elif keys['T']:
        double_bond(x1, y1, x2, y2, triple=True)
    else:
        line = canvas.create_line(x1, y1, x2, y2, width=5)
        lines.append(line)
def delete_last_line():
    if lines:
        canvas.delete(lines.pop())

def delete_line_under_cursor(event):
    if keys['F']:  # Проверяем, зажата ли клавиша 'F'
        x, y = event.x, event.y
        for line in lines:
            coords = canvas.coords(line)
            if coords:  # Проверяем наличие координат линии
                x1, y1, x2, y2 = coords
                if (min(x1, x2) <= x <= max(x1, x2)) and (min(y1, y2) <= y <= max(y1, y2)):
                    canvas.delete(line)  # Удаляем линию
                    lines.remove(line)  # Убираем из списка


def double_bond(x1, y1, x2, y2, offset=8, triple=False):
    line1 = canvas.create_line(x1, y1, x2, y2, width=5)
    lines.append(line1)

    # Рисуем вторую линию параллельно первой
    dx = offset * math.sin(math.radians(direction))
    dy = offset * math.cos(math.radians(direction))
    line2 = canvas.create_line(x1 + dx, y1 - dy, x2 + dx, y2 - dy, width=5)
    lines.append(line2)

    # Если triple=True, добавляем третью линию для тройной связи
    if triple:
        line3 = canvas.create_line(x1 - dx, y1 + dy, x2 - dx, y2 + dy, width=5)
        lines.append(line3)

def key_press(event):
    if event.keysym in keys:
        keys[event.keysym] = True
    if keys['Z']:
        delete_last_line()
    update_direction()

def key_release(event):
    if event.keysym in keys:
        keys[event.keysym] = False
    update_direction()

def update_direction():
    global direction
    if keys['Up'] and not keys['Left'] and not keys['Right']:
        direction = 270
    elif keys['Down'] and not keys['Left'] and not keys['Right']:
        direction = 90
    elif keys['Left'] and not keys['Up'] and not keys['Down']:
        direction = 180
    elif keys['Right'] and not keys['Up'] and not keys['Down']:
        direction = 0
    elif keys['Left'] and keys['Up'] and not keys['Down']:
        direction = 225
    elif keys['Left'] and not keys['Up'] and keys['Down']:
        direction = 135
    elif keys['Right'] and keys['Up'] and not keys['Down']:
        direction = 315
    elif keys['Right'] and not keys['Up'] and keys['Down']:
        direction = 45

root = tk.Tk()
root.title("CHEMPAINT VER 0.0.0.0")
canvas = tk.Canvas(root, bg="white", width=1000, height=800)
canvas.pack()

canvas.bind("<Button-1>", draw_line)
canvas.bind("<KeyPress>", key_press)
canvas.bind("<KeyRelease>", key_release)
canvas.focus_set()
canvas.bind("<Motion>", delete_line_under_cursor)

root.mainloop()



