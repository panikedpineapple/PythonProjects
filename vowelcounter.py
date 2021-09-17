word = input('Enter a string to count vowels:')

VOWEL_LIST = ['a','e','i','o','u']

final_dict = {}
for letter in VOWEL_LIST:
    count = 0
    for letters in word.lower():
        if letter == letters: count +=1
    final_dict[letter] = count

for key in final_dict:
    print(f'The letter {key.upper()} was found {final_dict[key]} times.')