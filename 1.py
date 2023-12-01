str = '1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'
splitstr = str.splitlines()

list = []

for line in splitstr:
    temp_digit = ''
    for char in line:
        if char.isdigit():
            temp_digit += char
    list.append(temp_digit)

sum = 0
temp = []
for i in list:
    temp_digit = ''
    for j in i:
        if j == i[0] or j == i[-1]:
            temp_digit += j
        if len(i) == 1:
            temp_digit+= j

    temp.append(temp_digit) 


for n in temp:
   sum += int(n) 

print(sum)
