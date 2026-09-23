import tkinter as tk
import math


class KolovratApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Коловрат")
        self.root.configure(bg='white')
        self.root.resizable(False, False)

        self.size = 800
        self.canvas = tk.Canvas(
            root,
            width=self.size,
            height=self.size,
            bg='white',
            highlightthickness=0
        )
        self.canvas.pack()

        self.cx = self.size // 2
        self.cy = self.size // 2
        self.R = 320          # длина луча (внешний радиус)
        self.W = 40          # толщина луча
        self.L = 75           # длина верхней перекладины "Г"
        self.OVER = 50        # насколько луч заходит за центр (убирает дырку)

        # Форма буквы "Г", направленной ВВЕРХ:
        # вертикальная палка + горизонтальная перекладина сверху справа
        self.base_points = [
            (-self.W / 2, self.OVER),                 # низ левой стороны (за центром)
            (-self.W / 2, -self.R),                   # верхний левый угол
            (self.W / 2 + self.L, -self.R),           # правый конец перекладины (верх)
            (self.W / 2 + self.L, -self.R + self.W),  # правый конец перекладины (низ)
            (self.W / 2, -self.R + self.W),           # внутренний угол "Г"
            (self.W / 2, self.OVER),                  # низ правой стороны (за центром)
        ]

        self.angle = 0.0
        self.speed = 2.5  # отрицательная скорость = против часовой стрелки
        self.paused = False

        self.root.bind('<space>', self.toggle_pause)
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.root.bind('<Button-1>', self.toggle_pause)

        self.animate()

    def toggle_pause(self, event=None):
        self.paused = not self.paused

    def draw_kolovrat(self):
        self.canvas.delete("all")

        for i in range(8):
            rot = math.radians(self.angle + i * 45)
            rotated = []
            for x, y in self.base_points:
                rx = x * math.cos(rot) - y * math.sin(rot)
                ry = x * math.sin(rot) + y * math.cos(rot)
                rotated.extend([self.cx + rx, self.cy + ry])

            self.canvas.create_polygon(
                rotated,
                fill='black',
                outline='black'
            )

    def animate(self):
        if not self.paused:
            self.angle = (self.angle + self.speed) % 360
            self.draw_kolovrat()
        self.root.after(20, self.animate)


if __name__ == "__main__":
    root = tk.Tk()
    KolovratApp(root)
    root.mainloop()