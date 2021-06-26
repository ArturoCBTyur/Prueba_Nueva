def palindrome(string):
    assert len(string) > 0 and string != " ", "We cannot received a void string :c"
    return string == string[::-1]

def main():
    print(palindrome(""))

if __name__ == "__main__":
    main()