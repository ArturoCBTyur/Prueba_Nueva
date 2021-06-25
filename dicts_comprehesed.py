# Dictionaries Comprehesed

# Now we merge the same code but in one line

def main():
    # new_dict = {}
    # for iterator in range(1, 101):
    #     if iterator % 3 != 0:
    #         solve = iterator**3
    #         new_dict[iterator] = solve
    #         print(f"Current iterator: {iterator} && Current value: {solve}")

    new_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    print(new_dict)

    # The task number 2

    task_dict = {j: round(j**(1/2), 2) for j in range(1, 1001)}

    print(task_dict)

if __name__ == "__main__":
    main()