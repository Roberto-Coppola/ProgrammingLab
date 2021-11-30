class CSVfile():
    
    def __init__(self, name):
        if not isinstance(name, str):
                raise Exception ('Il nome del file("{}") non è una stringa'.format(name))
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
        except AttributeError:#scegliere tra le due righe seguenti:
            print('no')
            #pass
myobject=CSVfile(5)
myobject2=myobject.get_data()
print(myobject2)