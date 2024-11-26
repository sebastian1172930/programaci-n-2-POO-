import symbols
import plot

# Definir una variable simbólica
x = symbols('x')

# Definir una expresión simbólica (la función a graficar)
expr = x**2

# Graficar la función en el rango -5 a 5
plot(expr, (x, -5, 5), title="Gráfica de f(x) = x^2", xlabel="x", ylabel="f(x)")
