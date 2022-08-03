import json

import plotly
import plotly.express as px


class LinearFunction:

    def __init__(self, name, point1=None, point2=None, slope=None, y_intersection=None):
        self.name = name
        self.point1: tuple = point1
        self.point2: tuple = point2
        self.slope: float = slope or self.compute_slope()
        self.y_intersection: float = y_intersection or self.compute_y_intersection()

    def check_points_required(self):
        if self.point1 is None or self.point2 is None:
            raise ValueError(f"Points are required for this calculation.")

    def compute_slope(self):
        """Calcula pendiente"""
        self.check_points_required()
        return (self.point2[1] - self.point1[1])/(self.point2[0] - self.point1[0])

    def compute_y_intersection(self):
        """Calcula intersección en y"""
        self.check_points_required()
        return self.point2[1] - self.slope * self.point2[0]

    def compute_y(self, x):
        """Calcula el valor de y para un valor de x dado"""
        return self.slope * x + self.y_intersection

    def compute_x(self, y):
        """Calcula el valor de x para un valor de y dado"""
        return (y - self.y_intersection)/self.slope

    def plot_line(self, title="", step=250, samples=10):
        x_values = range(0, samples*step, step)
        y_values = [self.compute_y(x) for x in x_values]
        return px.line(x=x_values, y=y_values, title=title)

    def graph_me(self, title="", step=250, samples=10):
        fig = self.plot_line(title, step, samples)
        fig.show()

    def graph_json(self, title="", step=250, samples=10):
        fig = self.plot_line(title, step, samples)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    def equilibrium_point(self, linear_func):
        x = (linear_func.y_intersection - self.y_intersection)/(self.slope-linear_func.slope)
        y = self.compute_y(x)
        return x, y

    def equation(self):
        b = f"{self.y_intersection:.2f}"
        return f"Y = {self.slope:.2f}X " \
               f"{f'+ {b}' if self.y_intersection > 0 else b}"

    def __repr__(self):
        """Imprime la ecuación de y(x)"""
        return self.equation()
