# Dictionaries Comprehesed

def main():
    new_dict = {}
    for iterator in range(1, 101):
        solve = iterator**3
        new_dict[iterator] = solve
        print(f"Current iterator: {iterator} && Current value: {solve}")

    print(new_dict)

if __name__ == "__main__":
    main()