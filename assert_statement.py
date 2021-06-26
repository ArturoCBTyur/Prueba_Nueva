def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors

def main():
    num = input("Digita un número: ")
    assert num.isnumeric(), "You cannot put a character"
    print(divisors(int(num)))
    print("Fin owo")
    print("Ese no es un numero. Digita un numero")


if __name__ == "__main__":
    main()