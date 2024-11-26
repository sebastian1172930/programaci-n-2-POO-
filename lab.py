import matplotlib.pyplot as plt

# Datos experimentales
Ns_Np = [2, 0.5]  # Relación de espiras
Vs_Vp = [2.1, 0.52]  # Relación de voltajes

Pp = [3.2, 6.0, 12.0]  # Potencia primaria para lámparas
Ps = [0.76, 2.0, 5.0]  # Potencia secundaria para lámparas

num_lamparas = [1, 2, 3]
corriente_serie = [0.07, 0.05, 0.04]
corriente_paralelo = [0.10, 0.13, 0.15]
eficiencia = [(p_s / p_p) * 100 for p_s, p_p in zip(Ps, Pp)]

# 1. Relación Vs/Vp vs Ns/Np
plt.figure()
plt.plot(Ns_Np, Vs_Vp, marker='o', label="Experimental")
plt.plot(Ns_Np, Ns_Np, linestyle='--', label="Teórico (y=x)")
plt.xlabel("Relación Ns/Np")
plt.ylabel("Relación Vs/Vp")
plt.title("Relación Vs/Vp vs Ns/Np")
plt.legend()
plt.grid()

# 2. Potencia primaria vs secundaria
plt.figure()
plt.plot(Pp, Ps, marker='o', label="Potencia")
plt.plot(Pp, Pp, linestyle='--', label="Referencia (y=x)")
plt.xlabel("Potencia primaria (W)")
plt.ylabel("Potencia secundaria (W)")
plt.title("Potencia primaria vs secundaria")
plt.legend()
plt.grid()

# 3. Eficiencia vs número de lámparas
plt.figure()
plt.plot(num_lamparas, eficiencia, marker='o')
plt.xlabel("Número de lámparas")
plt.ylabel("Eficiencia (%)")
plt.title("Eficiencia vs número de lámparas")
plt.grid()

# 4. Corriente vs número de lámparas
plt.figure()
plt.plot(num_lamparas, corriente_serie, marker='o', label="Serie")
plt.plot(num_lamparas, corriente_paralelo, marker='o', label="Paralelo")
plt.xlabel("Número de lámparas")
plt.ylabel("Corriente (A)")
plt.title("Corriente vs número de lámparas")
plt.legend()
plt.grid()

plt.show()
