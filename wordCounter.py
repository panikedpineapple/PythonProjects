#open a txt file called testfile.txt.

# with open('testfile.txt', 'r') as f:
#     new_string_list = f.readlines()
# count = 0
# for s in new_string_list:
#     count += len(s.split())

# print(f'The string is {count} words long.')

#--------------------------------------------

# input styring versdion

new_string = input('enter a string to count:')

count = len(new_string.split())

print(f'The string is {count} words long.')