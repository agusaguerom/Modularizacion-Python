from Vehiculo.Vehiculo import Vehiculo

class AutoVolador(Vehiculo):
    def __init__(self, año, modelo, color):
        super().__init__(año, modelo)
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color