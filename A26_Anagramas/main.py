def main():
    primeiraPalavra = input("Informe a primeira palavra: ")
    segundaPalavra = input("Informe a segunda palavra: ")

    primeiraPalavra = ''.join(sorted(str.lower(primeiraPalavra)))
    segundaPalavra = ''.join(sorted(str.lower(segundaPalavra)))

    if primeiraPalavra == segundaPalavra:
        print("As palavras informadas são anagramas.")
    else:
        print("As palavras informadas não são anagramas.")

if __name__ == '__main__':
    main()
