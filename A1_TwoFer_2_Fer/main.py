from A1_TwoFer_2_Fer.twofer import twofer



def main():
    print("Bem-vindo ao programa TwoFer")
    print("Informe um nome qualquer: ", end="") #end="" para o cursor não pular para a próxima linha, haja vista que o padrão é "\n"
    nome = input()
    twofer(nome)

if __name__ == "__main__":
    main()