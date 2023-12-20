import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random  # Эмулируем получение данных с датчика

class SensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Визуализация данных датчика")

        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(1, 1, 1)

        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.update_plot()

    def update_plot(self):
        # Эмулируем получение данных с датчика (замените этот блок кода реальным получением данных)
        sensor_data = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(50)]

        x_values, y_values = zip(*sensor_data)
        self.plot.clear()
        self.plot.scatter(x_values, y_values, color='b', marker='o')
        self.plot.set_title("Изображение окружающего мира")
        self.plot.set_xlabel("X-координата")
        self.plot.set_ylabel("Y-координата")
        self.canvas.draw()

        # Регулируйте интервал обновления данных с датчика по своему усмотрению
        self.root.after(1000, self.update_plot)

if __name__ == "__main__":
    root = tk.Tk()
    app = SensorApp(root)
    root.mainloop()