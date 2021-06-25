# Dictionaries Comprehesed

def main():
    # new_dict = {}
    # for iterator in range(1, 101):
    #     if iterator % 3 != 0:
    #         solve = iterator**3
    #         new_dict[iterator] = solve
    #         print(f"Current iterator: {iterator} && Current value: {solve}")

    new_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(new_dict)

if __name__ == "__main__":
    main()