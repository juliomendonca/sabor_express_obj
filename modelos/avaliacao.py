class Avaliacao:
    """Classe Avaliacao representa uma avaliação de um restaurante.
    A avaliação é composta por um cliente e uma nota.
    """

    def __init__(self, cliente, nota):
        """Inicializa uma nova avaliação.
        A avaliação é composta por um cliente e uma nota.

        Args:
            cliente (_type_): _description_
            nota (_type_): _description_
        """
        self._cliente = cliente
        self._nota = nota
