# Crear una Clase auto que permita ingresar los datos necesario para hallar
# la velocidad mediante un método.
# v=d/t
class Auto:
    def __init__(self,d,t):
        self.d=d
        self.t=t
    def velocidad(self):
        return f"La velocidad es: {self.d/self.t}"
    
sbj=Auto(100,2)
print(sbj.velocidad())