def main():
    # list_squares = []
    # pointers_list = []
    
    # pointer = 0
    # iterator = 1

    # for iterator in range(1,11):
    #     solve = iterator**2
    #     evaluator = solve % 3

    #     if evaluator != 0:
    #         pointers_list.append(pointer)
    #         pointer += 1
    #         list_squares.append(solve)
    #         print(f"Using the number {iterator} in the list the solve is: {solve}")
    
    # print(f"Values in ur list are : {list_squares}")
    # print(f"Pointersin ur list are: {pointers_list}")

    # Same but in oneline

    print("First part")

    squares = [i**2 for i in range(1, 100) if i % 3 != 0]

    print(squares)

    # Python Task

    print("Second part")

    challenge = [j for j in range(1, 100000) if j % 36 == 0]

    print(challenge)

    print("This is all in this part")


if __name__ == "__main__":
    main()