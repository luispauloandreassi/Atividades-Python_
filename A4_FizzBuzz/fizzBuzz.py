def FizzBuzz(valorInicial, numeroFinal):

    print("Apresentacao:")
    for i in range(valorInicial, numeroFinal + 1):
        if i % 3 == 0 and i % 5 == 0:
            if i == numeroFinal:
                print("FizzBuzz", end="")
            else:
                print("FizzBuzz-", end="")
        elif i % 3 == 0:
            if i == numeroFinal:
                print("Fizz", end="")
            else:
                print("Fizz-", end="")
        elif i % 5 == 0:
            if i == numeroFinal:
                print("Buzz", end="")
            else:
                print("Buzz-", end="")
        else:
            if i == numeroFinal:
                print(str(i), end="")
            else:
                print(str(i) + "-", end="")