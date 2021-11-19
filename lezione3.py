somma=[]
file = open('shampoo_sales.csv', 'r')
for line in file:
    elements = line.split(',')
    if elements[0] != 'Date':
        date = elements[0]
        value = elements[1]
        somma.append(float(value))
print ('La somma è: {}'. format(sum(somma)))