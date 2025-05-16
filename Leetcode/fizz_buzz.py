list_a = [x for x in range(1, 16)]
rules = {3: 'Fizz', 5: 'Buzz'}

printable_list = []

for element in list_a:
    element_to_word = ''
    
    for key in rules:
        if element % key == 0:
            element_to_word += rules[key]
            
    if not element_to_word:
        element_to_word = str(element)
    printable_list.append(element_to_word)

print(printable_list)