import plotly.express as px


class LinearFunction:

    def __init__(self, name, point1, point2):
        self.name = name
        self.point1: tuple = point1
        self.point2: tuple = point2
        self.slope: float = self.compute_slope()
        self.y_intersection: float = self.compute_y_intersection()

    def compute_slope(self):
        """Calcula pendiente"""
        return (self.point2[1] - self.point1[1])/(self.point2[0] - self.point1[0])

    def compute_y_intersection(self):
        """Calcula intersección en y"""
        return self.point2[1] - self.slope * self.point2[0]

    def compute_y(self, x):
        """Calcula el valor de y para un valor de x dado"""
        return self.slope * x + self.y_intersection

    def compute_x(self, y):
        """Calcula el valor de x para un valor de y dado"""
        return (y - self.y_intersection)/self.slope

    def graph_me(self, title="", step=250, samples=10):
        x_values = range(0, samples*step, step)
        y_values = [self.compute_y(x) for x in x_values]
        fig = px.line(x=x_values, y=y_values, title=title)
        fig.show()

    def equilibrium_point(self, linear_func):
        x = (linear_func.y_intersection - self.y_intersection)/(self.slope-linear_func.slope)
        y = self.compute_y(x)
        return x, y

    def __repr__(self):
        """Imprime la ecuación de y(x)"""
        return f"y = {self.slope}x + {self.y_intersection}"