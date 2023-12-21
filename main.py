import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
from itertools import count
import math

DELAY_MS: int = 100

class SensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Визуализация данных датчика")

        self.figure = Figure(figsize=(10, 10), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)
        
        self.plot.set_xlim(0, 10)
        self.plot.set_ylim(0, 10)

        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Используем itertools.count для генерации уникальных идентификаторов для каждой точки
        self.point_counter = count()

        # Интервал обновления данных с датчика
        self.root.after(DELAY_MS, self.update_plot)

    def update_plot(self):
        # Эмулируем получение новых данных с датчика
        new_point = self.get_coord_from_sensor()
        
        # Добавляем новую точку к текущему графику
        self.plot.scatter(*new_point, color='b', marker='o')

        # Обновляем подписи и отображение
        self.plot.set_title("Изображение окружающего мира")
        self.plot.set_xlabel("X-координата")
        self.plot.set_ylabel("Y-координата")
        self.plot.legend()

        self.canvas.draw()

        # Интервал обновления данных с датчика
        self.root.after(DELAY_MS, self.update_plot)
    
    def get_coord_from_sensor(self):
        angle = random.uniform(0, 2*math.pi)
        radius = 4 + random.uniform(0, 0.2)
        
        x_shift = 5
        y_shift = 5
        
        return (radius*math.cos(angle) + x_shift, radius*math.sin(angle) + y_shift)

if __name__ == "__main__":
    root = tk.Tk()
    app = SensorApp(root)
    root.mainloop()