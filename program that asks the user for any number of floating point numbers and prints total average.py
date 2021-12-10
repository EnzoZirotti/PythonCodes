


total = 0
average = 0

numlist = list()
while input != 'done':
    inp = input('Enter a number or type "done" to finish: ')
    if inp == 'done': break
    value = float(inp)
    total = total + float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
print('The sum is',total)
print("the numbers were ",numlist)


