from computador_builder import ComputadorBuilder


if __name__ == '__main__':
    computador_basico = (ComputadorBuilder().set_processador("Intel Core i5")
                         .set_ram("8GB")
                         .set_armazenamento("256GB SSD").build())

    computador_gamer = (ComputadorBuilder().set_processador("Intel Core i9")
                        .set_ram("32GB")
                        .set_armazenamento("1TB SSD")
                        .set_placa_de_video("NVIDIA RTX 4070").build())

    print(f'=== COMPUTADOR BÁSICO ===\n{computador_basico}')
    print(f'=== COMPUTADOR GAMER ===\n{computador_gamer}')
