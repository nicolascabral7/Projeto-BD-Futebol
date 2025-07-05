from db_manager import (
    adicionar_jogador, listar_jogadores,
    adicionar_time, listar_times,
    vincular_jogador_time, listar_jogadores_do_time,
    adicionar_jogo, listar_jogos,
    adicionar_partida, listar_partidas
)
from utils import validar_idade, validar_data

def menu():
    while True:
        print("\n=== Sistema de Torneios de eSports ===")
        print("1 - Cadastrar jogador")
        print("2 - Listar jogadores")
        print("3 - Cadastrar time")
        print("4 - Listar times")
        print("5 - Vincular jogador a time")
        print("6 - Listar jogadores de um time")
        print("7 - Cadastrar jogo")
        print("8 - Listar jogos")
        print("9 - Registrar partida")
        print("10 - Listar partidas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do jogador: ")
            idade = None
            while idade is None:
                idade = validar_idade(input("Idade: "))
            nickname = input("Nickname: ")
            adicionar_jogador(nome, idade, nickname)

        elif opcao == '2':
            jogadores = listar_jogadores()
            print("\nJogadores cadastrados:")
            for j in jogadores:
                print(f"ID: {j[0]} | Nome: {j[1]} | Idade: {j[2]} | Nickname: {j[3]}")

        elif opcao == '3':
            nome = input("Nome do time: ")
            adicionar_time(nome)

        elif opcao == '4':
            times = listar_times()
            print("\nTimes cadastrados:")
            for t in times:
                print(f"ID: {t[0]} | Nome: {t[1]}")

        elif opcao == '5':
            print("Vincular jogador a time")
            jogadores = listar_jogadores()
            for j in jogadores:
                print(f"ID: {j[0]} | Nickname: {j[3]}")
            times = listar_times()
            for t in times:
                print(f"ID: {t[0]} | Nome: {t[1]}")

            jogador_id = input("ID do jogador: ")
            time_id = input("ID do time: ")
            try:
                jogador_id = int(jogador_id)
                time_id = int(time_id)
                vincular_jogador_time(jogador_id, time_id)
            except ValueError:
                print("IDs inválidos.")

        elif opcao == '6':
            times = listar_times()
            for t in times:
                print(f"ID: {t[0]} | Nome: {t[1]}")
            time_id = input("Digite o ID do time para listar os jogadores: ")
            try:
                time_id = int(time_id)
                jogadores = listar_jogadores_do_time(time_id)
                print(f"\nJogadores do time {time_id}:")
                for j in jogadores:
                    print(f"ID: {j[0]} | Nome: {j[1]} | Nickname: {j[2]}")
            except ValueError:
                print("ID inválido.")

        elif opcao == '7':
            nome = input("Nome do jogo: ")
            categoria = input("Categoria (FPS, MOBA, etc): ")
            adicionar_jogo(nome, categoria)

        elif opcao == '8':
            jogos = listar_jogos()
            print("\nJogos cadastrados:")
            for j in jogos:
                print(f"ID: {j[0]} | Nome: {j[1]} | Categoria: {j[2]}")

        elif opcao == '9':
            print("Registrar partida")
            times = listar_times()
            print("Times:")
            for t in times:
                print(f"ID: {t[0]} | Nome: {t[1]}")

            jogos = listar_jogos()
            print("Jogos:")
            for j in jogos:
                print(f"ID: {j[0]} | Nome: {j[1]}")

            try:
                time1_id = int(input("ID do Time 1: "))
                time2_id = int(input("ID do Time 2: "))
                jogo_id = int(input("ID do Jogo: "))
                data = None
                while data is None:
                    data = validar_data(input("Data (AAAA-MM-DD): "))
                vencedor_id = int(input("ID do time vencedor: "))

                if vencedor_id != time1_id and vencedor_id != time2_id:
                    print("Vencedor deve ser um dos dois times participantes.")
                else:
                    adicionar_partida(time1_id, time2_id, jogo_id, data, vencedor_id)
            except ValueError:
                print("Entrada inválida. Use números inteiros para IDs.")

        elif opcao == '10':
            partidas = listar_partidas()
            print("\nPartidas registradas:")
            for p in partidas:
                print(f"ID: {p[0]} | {p[1]} vs {p[2]} | Jogo: {p[3]} | Data: {p[4]} | Vencedor: {p[5]}")

        elif opcao == '0':
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == '__main__':
    menu()
