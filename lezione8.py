class model():
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')
class IncrementModel(model):
    def predict(self, data):
        prev_value=None
        n=len(data)-1
        tot=0
        var=0
        for item in data:
            if var==0:
                var=var+1
            else:
                tot=tot+item-data[var-1]
                var=var+1
        predict=tot/n
        valore_incrementato=data[n]+predict
        return valore_incrementato
dati=[50, 52, 60]
print('predizione {}'. format(IncrementModel().predict(dati)))