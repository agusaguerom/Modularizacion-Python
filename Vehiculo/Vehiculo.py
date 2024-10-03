class Vehiculo:
    def __init__(self, año, modelo):
        self._año = año
        self.__modelo = modelo

    def get_año(self):
        return self._año

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    def set_año(self, año):
        self.__año = año