import json

import plotly

from LinearFunction import LinearFunction
import pandas as pd
import plotly.express as px


def get_function():
    data = []
    name = input("Ingrese el nombre de la función: ")
    print(f"A continuación se le solicitará los datos (pares ordenados) para la función lineal.")
    for i in range(2):
        print(f"Ingrese el par ordenado #{i+1}")
        x = float(input(f"Valor de X{i+1}: "))
        y = float(input(f"Valor de Y{i+1}: "))
        data.append((x, y))
    return LinearFunction(name, *data)


class FunctionCollection:

    def __init__(self, *args):
        self.functions: list[LinearFunction] = args
    #     self.init_functions()
    #
    # def init_functions(self):
    #     count = int(input("Por favor indique cuantas funciones lineales desea calcular: "))
    #     for i in range(count):
    #         self.functions.append(
    #             get_function()
    #         )

    @staticmethod
    def x_axes(step, samples):
        return list(range(0, samples*step, step))

    def graph_all(self, title, step=5, samples=100):
        data = {}
        x_axes = self.x_axes(step, samples)
        for f in self.functions:
            data[f.name] = pd.Series([f.compute_y(x) for x in x_axes], index=x_axes)
        df = pd.DataFrame(data)
        fig = px.line(df, title=title)
        return fig
        # fig.show()

    def graph_json(self, step=5, samples=100):
        fig = self.graph_all(" vs ".join([f.name for f in self.functions]), step, samples)
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
