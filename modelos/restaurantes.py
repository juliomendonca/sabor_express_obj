class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def _str_(self):
        return f"{self._nome} {self._categoria}"

    def alternar_estado(self):
        self._ativo = not self._ativo

    @classmethod
    def listar_restaurantes(cls):
        print(
            f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}"
        )
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        return "Ativo" if self._ativo else "Inativo"


restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante("pizza express", "Italiana")

Restaurante.listar_restaurantes()
