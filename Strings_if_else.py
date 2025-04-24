fruit = input('Eneter a fruit name')
#user dir(fruit) to get the methods/functions related to string
if fruit.lower() < 'banana': #Change case to lower.
    print('Your word '+fruit+' comes before banana')
    #if first letter comes before b then returns this
elif fruit > 'banana':
    print('Your word '+fruit+' comes after banana')
    #if first letter comes after b then returns this
else:
    print('Your word '+fruit+' is banana')
    #if banana equals entered word