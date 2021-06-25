import functools

def main():
    # First type function -> filter

    # Without filter
    my_list = [1,2,3,4,5,6,7]
    output = [i**2 for i in my_list if i % 2 != 0]
    print(output)

    # Second type function -> map

    # Without map
    my_list_2 = [1,2,3,4,5,6,7]
    output_2 = [i**2 for i in my_list]
    print(output_2)

    # Third type function -> filter

    # Without reduce
    my_list_3 = [1,2,3,4,5,6,7]
    output_3 = 1
    for i in my_list_3:
        output_3 *= i
    print(output_3)

if __name__ == "__main__":
    main()