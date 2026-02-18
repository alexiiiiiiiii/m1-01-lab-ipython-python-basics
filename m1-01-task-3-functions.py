def userInput(answer):
    # answer = input("Please input a value: ")
    if answer.isdigit():
        answer = float(answer)
        
    else:
        return None

# userInput()

def cleanedString(answer):
    # answer = input('Please input your text: ')
    answer = ' '.join(answer.split())
    answer = answer.lower()
    return answer

test_List = ['123',
             '12saoeW',
             'My words dont count there      but why?',
             'just a     simple TEST to check      my whitespace and LOWERcase',
             'numbers number     and again        numbers'
             ]

for i in test_List:
    print(userInput(i))
    print(cleanedString(i))