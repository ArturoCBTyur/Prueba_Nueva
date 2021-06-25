from functools import reduce

def main():
    # First type function -> filter

    # Without filter
    my_list = [1,2,3,4,5,6,7]
    output = [i for i in my_list if i % 2 != 0]
    print(output)

    # With filter
    result = list(filter(lambda x: x % 2 != 0, my_list))
    print(result)

    # Second type function -> map

    # Without map
    my_list_2 = [1,2,3,4,5,6,7]
    output_2 = [i**2 for i in my_list]
    print(output_2)

    # With map
    result_2 = list(map(lambda x: x**2, my_list_2))
    print(result_2)

    # Third type function -> filter

    # Without reduce
    my_list_3 = [1,2,3,4,5,6,7]
    output_3 = 1
    for i in my_list_3:
        output_3 *= i
    print(output_3)

    # With reduce
    result_3 = reduce(lambda x, y: x*y, my_list_3)
    print(result_3)

if __name__ == "__main__":
    main()