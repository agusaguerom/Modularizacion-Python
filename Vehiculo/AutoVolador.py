from Vehiculo import Vehiculo

class AutoVolador(Vehiculo.Vehiculo):
    def __init__(self, año, modelo, tiempovuelo):
        super().__init__(año, modelo)
        self.tiempovuelo = tiempovuelo

    def get_tiempovuelo(self):
        return self.tiempovuelo
    
    def set_tiempovuelo(self, tiempovuelo):
        self.tiempovuelo = tiempovuelo
