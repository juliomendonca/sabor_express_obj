class Restaurante:
    """Classe Restaurante
    Representa um restaurante com nome, categoria e estado (ativo/inativo).
    """

    """Atributos da classe:
    - restaurantes: lista de todos os restaurantes cadastrados.

    Returns:
        Listagem com todos os restaurantes cadastrados.
    """
    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa um novo restaurante com nome e categoria.
        O nome é convertido para título e a categoria é convertida para maiúsculas.

        Args:
            nome (_type_): _description_
            categoria (_type_): _description_
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def _str_(self):
        """Representação em string do restaurante.
        Exibe o nome e a categoria do restaurante.

        Returns:
            Nome | Categoria
        """
        return f"{self._nome} | {self._categoria}"

    def alternar_estado(self):
        """Alterna o estado do restaurante entre ativo e inativo.
        Se o restaurante estiver ativo, ele será inativo e vice-versa.
        """
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        """Listar todos os restaurantes cadastrados.
        Exibe o nome, categoria e status (ativo/inativo) de cada restaurante.
        """
        print(
            f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}"
        )
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        """Retorna o status do restaurante (ativo/inativo).
        Exibe o status do restaurante de forma legível.

        Returns:
            Ativo ou Inativo: O status do restaurante.
        """
        return "Ativo" if self._ativo else "Inativo"
