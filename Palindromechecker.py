word = input("Enter test word:")

if list(word) == list(word)[::-1]:
    print("This word is a palindrome.")
else:
    print("this word is not a palindrome")