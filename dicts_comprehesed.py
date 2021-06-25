# Dictionaries Comprehesed

def main():
    new_dict = {}
    for iterator in range(1, 101):
        
        solve = iterator**2
        new_dict.update(iterator = solve)
        print(f"Current iterator: {iterator} && Current value: {solve}")

    print(new_dict)

if __name__ == "__main__":
    main()