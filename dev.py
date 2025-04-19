from modelos.restaurantes import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_mexicano.alternar_estado()


def main():
    """
    Main function to run the script.
    """
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
