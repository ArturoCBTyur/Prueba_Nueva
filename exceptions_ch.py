def parameter(num):
    try:
        if num < 0:
            raise ValueError("You cannot type a negative number.")
        else:
            return(print("That's correct c:"))
    except ValueError as ex:
        print(ex)
        print("That's Wrong :c")



def main():
    num = int(input("Digite un numero positivo: "))
    parameter(num)


if __name__ == "__main__":
    main()