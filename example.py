from FunctionCollection import FunctionCollection
from LinearFunction import LinearFunction

if __name__ == '__main__':
    oferta = LinearFunction(
        name="Oferta",
        point1=(2000, 250),
        point2=(4000, 750)
    )
    demanda = LinearFunction(
        name="Demanda",
        point1=(2500, 450),
        point2=(3000, 300)
    )

    FunctionCollection(
        oferta,
        demanda,
        LinearFunction(
            name="Otra",
            point1=(3500, 450),
            point2=(6000, 300)
        )
    ).graph_all(step=20, samples=200)

    print(demanda.compute_x(250)*250)

    print(demanda.compute_y(3000*1.2))

    print(oferta.compute_x(0))

    print(oferta.equilibrium_point(demanda))
