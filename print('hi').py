# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt


# X = np.linspace(-10, 10, 200)


# polynomial = X**3 - X**2 + X + 1
# harmonic = np.sin(X)
# harmonic_with_poly = np.sin(polynomial)


# data = {
#     'X': X,
#     'Полином 3-й степени': polynomial,
#     'Гармоническая функция': harmonic,
#     'Гармоническая с полиномом': harmonic_with_poly
# }

# df = pd.DataFrame(data)

# # print(df)

# # Построение графиков
# plt.figure(figsize=(15, 10))


# # Общий график
# plt.subplot(1,1,1)
# plt.plot(df['X'], df['Полином 3-й степени'], label='Полином 3-й степени')
# plt.plot(df['X'], df['Гармоническая функция'], label='Гармоническая функция')
# plt.plot(df['X'], df['Гармоническая с полиномом'], label='Гармоническая с полиномом')
# plt.title('Все функции на одном графике')
# plt.legend()
# plt.grid()

# plt.tight_layout()
# plt.ylim(-10, 10)

# plt.show()


# import tkinter as tk

# class InfiniteCanvas:
#     def __init__(self, master):
#         self.master = master
#         self.canvas = tk.Canvas(master, bg="light blue")
#         self.canvas.pack(expand=True, fill=tk.BOTH)

#         self.scrollbar_x = tk.Scrollbar(master, orient=tk.HORIZONTAL, command=self.canvas.xview)
#         self.scrollbar_y = tk.Scrollbar(master, orient=tk.VERTICAL, command=self.canvas.yview)
#         self.canvas.configure(xscrollcommand=self.scrollbar_x.set, yscrollcommand=self.scrollbar_y.set)

#         self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
#         self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

#         self.canvas.bind("<Button-1>", self.draw_point)

#         # Установка прокрутки
#         self.canvas.config(scrollregion=self.canvas.bbox("all"))
        
#     def draw_point(self, event):
#         x, y = event.x, event.y
#         self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")

# root = tk.Tk()
# root.title("Infinite Canvas")
# app = InfiniteCanvas(root)
# root.mainloop()

import pygame
import sys
from screeninfo import get_monitors

class InfiniteCanvas:
    def __init__(self):
        for monitor in get_monitors():
             self.screen_width, self.screen_height = monitor.width, monitor.height
        self.offset_x, self.offset_y = 0, 0
        self.points = []

        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Infinite Canvas")
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.points.append(event.pos)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.offset_x += 10
                    elif event.key == pygame.K_RIGHT:
                        self.offset_x -= 10
                    elif event.key == pygame.K_UP:
                        self.offset_y += 10
                    elif event.key == pygame.K_DOWN:
                        self.offset_y -= 10

            self.screen.fill((255, 255, 255))
            for point in self.points:
                pygame.draw.circle(self.screen, (0, 0, 0), (point[0] + self.offset_x, point[1] + self.offset_y), 5)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    canvas = InfiniteCanvas()
    canvas.run()