vowel_list = ['a','e','i','o','u']

input_word = input("Enter a word to translate:")
index = len(input_word)
if input_word[0].lower() in vowel_list:
    new_word = input_word + 'yay'
    print(new_word.title())
else:
    for letter in vowel_list:
        new_index = input_word.find(letter)
        if new_index < index and new_index != -1: index = new_index

    new_word = input_word[index:]+input_word[:index]+'ay'
    print(new_word.title())