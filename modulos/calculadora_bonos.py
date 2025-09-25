# modulos/calculadora_bonos.py
class CalculadoraBonos:
    """Módulo base para cálculo de bonos"""

    def calcular_bonos(self, empleado):
        # Bonificación fija del 10% si el empleado tiene "antigüedad" > 5
        if empleado.get("antiguedad", 0) > 5:
            return empleado["salario_base"] * 0.10
        return 0