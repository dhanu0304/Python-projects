def palindrome(text):
    # Base case
    if len(text) <= 1:
        return True

    # Check first and last characters
    if text[0] == text[-1]:
        return palindrome(text[1:-1])
    else:
        return False

word = "madam"
if palindrome(word):
    print(word, "is a palindrome.")
else:
    print(word, "is not a palindrome.")