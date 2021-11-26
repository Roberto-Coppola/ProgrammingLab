class CSVfile():
    
    def __init__(self, name):
        try:
            aper= open(name, 'r')#self.name
            aper.read()[0:1]
            self.name=name
        except:
            print("Il file non esiste")

    def get_data(self):
        try:
            value=[]
            file = open(self.name)
            for line in file:
                elements = line.split(',')
                if elements[0] != 'Date':
                    date = elements[0]
                    value1 = elements[1]
                    value.append(elements)
            return value
        except AttributeError:#scegliere tra i 2:
            print('no')
            #pass
myobject=CSVfile('shpoo_sales.csv')
myobject2=myobject.get_data()
print(myobject2)