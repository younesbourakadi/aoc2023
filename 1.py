file_path = "aoc_input/day1.txt"
file = open(file_path, 'r').read()
lines = file.split('\n')

word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


# list = []
# sum = 0
# temp = []

# for line in lines:
#     temp_digit = ''
#     for char in line:
#         if char.isdigit():
#             temp_digit += char
#     list.append(temp_digit)

# for i in list:
#     temp_digit = ''
#     if len(i) == 1:
#         temp_digit = i * 2
#     else :
#         temp_digit = i[0] + i[-1]
#     temp.append(temp_digit) 


# for n in temp:
#    sum += int(n) 




# part 2

inputs = open('aoc_input/day1.txt', 'r').readlines()

number_names = {'one' : '1',
                'two' : '2',
                'three' : '3',
                'four' : '4',
                'five' : '5',
                'six' : '6',
                'seven' : '7',
                'eight' : '8',
                'nine' : '9'}
total = 0

for line in inputs:
    nums = []
    for n in number_names:
        # replace word with number but keep first and last letter of the word in case of overlapping words
        line = line.replace(n, n[0] + number_names.get(n) + n[-1], line.count(n))
    for char in line:
        if char.isnumeric():
            nums.append(char)
    total += int(nums[0] + nums[-1])
print(total)
