def divisors(num):
    divisors = [i for i in range(1, num + 1) if num % i == 0]

    return divisors

def main():
    try:
        num = int(input("Digita un número: "))
        print(divisors(num))
        print("Fin owo5")
    except ValueError:
        print("Ese no es un numero. Digita un numero")


if __name__ == "__main__":
    main()