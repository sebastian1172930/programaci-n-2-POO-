import sympy as sp
import math
# Definimos la variable simbólica
x = sp.symbols('x')

# Definimos una función simbólica
f = x**2 + 3*x + 2

# Derivamos la función con respecto a x
f_derivada = sp.diff(f, x)

# Integramos la función con respecto a x
f_integrada = sp.integrate(f, x)

# Mostramos los resultados
print("Función original: ", f)
print("Derivada de la función: ", f_derivada)
print("Integral de la función: ", f_integrada)
