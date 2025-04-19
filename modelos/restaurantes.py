from modelos.avaliacao import Avaliacao


class Restaurante:
    """Classe Restaurante representa um restaurante.
    O restaurante é composto por um nome, uma categoria e uma lista de avaliações.
    """

    """Atributos da classe Restaurante:
    - nome: Nome do restaurante.
    """
    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa um novo restaurante.
        O restaurante é composto por um nome, uma categoria e uma lista de avaliações.

        Args:
            nome (_type_): _description_
            categoria (_type_): _description_
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        """Representa o restaurante como uma string.
        O restaurante é composto por um nome e uma categoria.

        Returns:
            _type_: _description_
        """
        return f"{self._nome} | {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        """Lista todos os restaurantes cadastrados.
        Esta função é responsável por listar os restaurantes cadastrados.
        """
        print(
            f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} |{'Status'}"
        )

        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} |{restaurante.ativo}"
            )

    @property
    def ativo(self):
        """Retorna o estado do restaurante.
        O estado do restaurante pode ser ativo ou inativo.

        Returns:
            _type_: _description_
        """
        return "⌧" if self._ativo else "☐"

    @property
    def media_avaliacoes(self):
        """Calcula a média das avaliações do restaurante.
        A média é calculada somando todas as notas e dividindo pelo número de avaliações.

        Returns:
            Retora um valor inteiro representando a média das avaliações do restaurante.
        Se não houver avaliações, retorna 0.
        """
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def alternar_estado(self):
        """Altera o estado do restaurante.
        O estado do restaurante pode ser ativo ou inativo.
        """
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """Recebe uma avaliação do restaurante.
        A avaliação é composta por um cliente e uma nota.

        Args:
            cliente (_type_): _description_
            nota (_type_): _description_
        """
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
