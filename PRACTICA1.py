
class Vehiculo:
    """
    Clase base que representa un vehículo genérico
    """

    def __init__(self, marca: str):
        """
        Constructor de la clase Vehiculo.

        Parámetros:
            marca (str): Marca del vehículo.
        """
        self.__marca = marca        # Atributo privado (encapsulado)
        self.__velocidad = 0        # Velocidad inicial en km/h (encapsulada)

    # ---------------- Métodos comunes ---------------- #

    def acelerar(self, incremento: int) -> None:
        """
        Aumenta la velocidad del vehículo.

        Parámetros:
            incremento (int): Valor positivo que se sumará a la velocidad.
        """
        self.__velocidad += incremento

    def frenar(self, decremento: int) -> None:
        """
        Disminuye la velocidad del vehículo.

        Parámetros:
            decremento (int): Valor positivo que se restará de la velocidad.
        """
        self.__velocidad -= decremento
        if self.__velocidad < 0:
            self.__velocidad = 0    # La velocidad no puede ser negativa

    def get_marca(self) -> str:
        """Devuelve la marca del vehículo."""
        return self.__marca

    def get_velocidad(self) -> int:
        """Devuelve la velocidad actual del vehículo."""
        return self.__velocidad

    def mostrar_datos(self) -> None:
        """
        Muestra los datos básicos del vehículo.
        Este método puede ser sobrescrito por las subclases.
        """
        print(f"Marca: {self.__marca} | Velocidad: {self.__velocidad} km/h")

    def consumo_combustible(self, distancia: float) -> float:
        """
        Calcula el consumo de combustible (litros) de forma genérica.
        Este método debe ser sobrescrito por las subclases.

        Parámetros:
            distancia (float): Distancia recorrida en km.

        Retorna:
            float: Consumo de combustible en litros.
        """
        return distancia * 0.1   # Suposición genérica: 0.1 L/km



# Subclase Coche

class Coche(Vehiculo):
    """
    Clase que representa un coche
    Hereda de Vehiculo e implementa comportamientos específicos.
    """

    def __init__(self, marca: str, num_puertas: int = 4):
        """
        Parámetros:
            marca (str): Marca del coche.
            num_puertas (int): Número de puertas del coche.
        """
        super().__init__(marca)  # Llamada al constructor de Vehiculo
        self.__num_puertas = num_puertas

    def mostrar_datos(self) -> None:
        """Muestra los datos específicos de un coche."""
        print(f"[Coche] Marca: {self.get_marca()} | "
              f"Velocidad: {self.get_velocidad()} km/h | "
              f"Puertas: {self.__num_puertas}")

    def consumo_combustible(self, distancia: float) -> float:
        """
        Calcula el consumo de combustible para un coche.

        Suposición:
            - Un coche consume 0.08 L/km

        Parámetros:
            distancia (float): Distancia recorrida en km.

        Retorna:
            float: Consumo de combustible en litros.
        """
        return distancia * 0.08

# Subclase Moto

class Moto(Vehiculo):
    """
    Clase que representa una motocicleta.
    Hereda de Vehiculo e implementa comportamientos específicos.
    """

    def __init__(self, marca: str, tipo_casco: str = "Integral"):
        """
        Constructor de la clase Moto.

        Parámetros:
            marca (str): Marca de la moto.
            tipo_casco (str): Tipo de casco recomendado.
        """
        super().__init__(marca)
        self.__tipo_casco = tipo_casco

    def mostrar_datos(self) -> None:
        """Muestra los datos específicos de una moto."""
        print(f"[Moto] Marca: {self.get_marca()} | "
              f"Velocidad: {self.get_velocidad()} km/h | "
              f"Casco recomendado: {self.__tipo_casco}")

    def consumo_combustible(self, distancia: float) -> float:
        """
        Calcula el consumo de combustible para una moto.

        Suposición:
            - Una moto consume 0.04 L/km

        Parámetros:
            distancia (float): Distancia recorrida en km.

        Retorna:
            float: Consumo de combustible en litros.
        """
        return distancia * 0.04


# ------------------------------------------------------ #

if __name__ == "__main__":
    # Crear un coche
    mi_coche = Coche("Toyota", 4)
    mi_coche.acelerar(50)
    mi_coche.mostrar_datos()
    mi_coche.frenar(20)
    mi_coche.mostrar_datos()
    print(f"Consumo coche en 100 km: {mi_coche.consumo_combustible(100)} L\n")

    # Crear una moto
    mi_moto = Moto("Yamaha", "Modular")
    mi_moto.acelerar(80)
    mi_moto.mostrar_datos()
    mi_moto.frenar(50)
    mi_moto.mostrar_datos()
    print(f"Consumo moto en 100 km: {mi_moto.consumo_combustible(100)} L")
