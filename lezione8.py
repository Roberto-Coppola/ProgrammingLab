class model()
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')
class IncrementModel(model)
    def predict(self, data):
        prev_value=None
        n=len(data)
        tot=0
        for item in data:
            var=1
            tot=tot+item[var]-item[var-1]
            var=var+1
        predict=tot/n
        valore_incrementato=data[n-1]+IncrementModel
dati=[50, 52, 60]
print('presdizione {}'. format(IncrementModel().predict(dati)))