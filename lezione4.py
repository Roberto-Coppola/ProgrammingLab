class CSVfile():
    
    def __init__(self, name):
        self.name=name

    def get_data(self):
        value=[]
        file = open(self.name)
        for line in file:
            elements = line.split(',')
            if elements[0] != 'Date':
                date = elements[0]
                value1 = elements[1]
                value.append(elements)
        return value

myobject=CSVfile('shampoo_sales.csv')
myobject2=myobject.get_data()
print(myobject2)