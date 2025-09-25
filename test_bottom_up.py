import pytest
from nomina_sistema import NominaSistema
from modulos.calculadora_impuestos import CalculadoraImpuestos
from drivers.test_driver import TestDriver

class TestNivelBase:
    """Nivel 1: Prueba módulos atómicos"""

    def setup_method(self):
        self.calc = CalculadoraImpuestos()
        self.driver = TestDriver(self.calc)

    def test_isr_salario_bajo(self):
        # ARRANGE
        salario = 8000
        # ACT
        resultado = self.calc.calcular_isr(salario)
        # ASSERT
        assert resultado == 400  # 5% de 8000

    def test_isr_salario_medio(self):
        resultado = self.calc.calcular_isr(15000)
        assert resultado == 1500  # 10% de 15000

    def test_seguro_social(self):
        resultado = self.calc.calcular_seguro_social(10000)
        assert resultado == 625  # 6.25% de 10000

    def test_isr_salario_alto(self):
        resultado = self.calc.calcular_isr(30000)
        assert resultado == 4500  # 15% de 30000

    def test_isr_limite_bajo(self):
        assert self.calc.calcular_isr(10000) == 500

    def test_isr_limite_medio(self):
        assert self.calc.calcular_isr(20000) == 2000

    def test_seguro_social_salario_alto(self):
        assert self.calc.calcular_seguro_social(20000) == 1250

class TestIntegracion:
    """Nivel 2: Integración de módulos"""

    def setup_method(self):
        self.nomina = NominaSistema()

    def test_nomina_con_bonos(self):
        empleado = {"salario_base": 12000, "antiguedad": 6, "prestamo": 1000}
        resultado = self.nomina.calcular_nomina_neta(empleado)
        # salario=12000, bono=1200, isr=1200, seguro=750, prestamo=1000
        esperado = 10250
        assert resultado == esperado

    def test_nomina_sin_bonos_ni_prestamos(self):
        empleado = {"salario_base": 9000, "antiguedad": 2}
        resultado = self.nomina.calcular_nomina_neta(empleado)
        # salario=9000, bono=0, isr=450, seguro=562.5
        esperado = 7987.5
        assert resultado == esperado

    def test_nomina_con_prestamo_sin_bono(self):
        empleado = {"salario_base": 9500, "antiguedad": 3, "prestamo": 500}
        resultado = self.nomina.calcular_nomina_neta(empleado)
        # salario=9500, bono=0, isr=475, seguro=593.75, prestamo=500
        esperado = 7931.25
        assert resultado == esperado

    def test_nomina_con_bono_sin_prestamo(self):
        empleado = {"salario_base": 15000, "antiguedad": 7}
        resultado = self.nomina.calcular_nomina_neta(empleado)
        # salario=15000, bono=1500, isr=1500, seguro=937.5
        esperado = 14062.5
        assert resultado == esperado