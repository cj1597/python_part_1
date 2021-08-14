def palindrome(given_string):
    if list(given_string.upper()) == list(reversed(given_string.upper())):
        print(f"{given_string} - true")

    else:
        print(f"{given_string} - false")

palindrome('clarence')
