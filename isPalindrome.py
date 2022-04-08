def is_palindrome(phrase):

    return phrase == phrase[::-1]


phrase = "hannah"
result = is_palindrome(phrase)

if result is True:
    print("The phrase is a palindrome.")
else:
    print("Oops, your word is not a palindrome.")
