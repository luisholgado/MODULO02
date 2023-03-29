def suma(num01,num02):
    return num01+num02
def resta(num01,num02):
    return num01-num02
def multiplicacion(num01,num02):
    return num01*num02
def division(num01,num02):
    return num01/num02

print(suma(5,3))

class Operacion():
    def __init__(self,num01,num02):
        self.num01=num01
        self.num02=num02
    def sumar(self):
        return self.num01+self.num02
    def restar(self):
        return self.num01-self.num02
    def multiplicar(self):
        return self.num01*self.num02
    def division(self):
        return self.num01/self.num02

