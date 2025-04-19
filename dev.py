from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_praca.receber_avaliacao("Teste 1", 8)
restaurante_praca.receber_avaliacao("Teste 2", 4)
restaurante_praca.receber_avaliacao("Teste 3", 3)


def main():
    """Função principal do programa.
    Esta função é responsável por criar um restaurante e listar os restaurantes cadastrados.
    """
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
