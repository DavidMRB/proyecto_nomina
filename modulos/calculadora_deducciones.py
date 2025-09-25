# modulos/calculadora_deducciones.py
class CalculadoraDeducciones:
    """Módulo base para deducciones adicionales"""

    def calcular_deducciones(self, empleado):
        # Deduce préstamos si existen
        return empleado.get("prestamo", 0)