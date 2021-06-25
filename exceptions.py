def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("We cannot catch a void string")
        return string == string[::-1]
    except ValueError as ex:
        print(ex)
        return False

def main():
    try:
        # print(palindrome(121))
        print(palindrome(""))
    except TypeError as e:
        print(f"Only we can catch strings. Error: {e}. This is bad.")



if __name__ == "__main__":
    main()