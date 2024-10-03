from Vehiculo.AutoVolador import AutoVolador

autovolador = AutoVolador(2022, "Peugeot", 24)


print("Año y Modelo Originales")
print(autovolador.get_modelo())
print(autovolador.get_año())



autovolador.set_modelo("Chevrolet")
autovolador.set_año(2024)


print("\nAño y Modelo Modificados")
print(autovolador.get_modelo())
print(autovolador.get_año())