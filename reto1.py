import tkinter as sb_tk
from tkinter import ttk as sb_ttk
import numpy as sb_np
import matplotlib.pyplot as sb_plt

def sb_serie(sb_resistencias):
    return sb_np.sum(sb_resistencias)

def sb_paralelo(sb_resistencias):
    sb_resistencias = sb_np.array(sb_resistencias)
    return 1 / sb_np.sum(1 / sb_resistencias)

def sb_grafica(sb_conexion, sb_resistencias):
    sb_n_resistencias = list(range(1, len(sb_resistencias) + 1))
    sb_resistencias_t = []

    for sb_i in sb_n_resistencias:
        if sb_conexion == "Serie":
            sb_resistencias_t.append(sb_serie(sb_resistencias[:sb_i]))
        else:
            sb_resistencias_t.append(sb_paralelo(sb_resistencias[:sb_i]))

    sb_plt.plot(sb_n_resistencias, sb_resistencias_t, marker="o")
    sb_plt.xlabel("Número de resistencias")
    sb_plt.ylabel("Resistencia equivalente (Ohm)")
    sb_plt.title(f"Relación Resistencia Total vs Número de Resistencias ({sb_conexion})")
    sb_plt.grid(True)
    sb_plt.show()

def sb_calcular():
    sb_tip_conex = sb_conex.get()
    try:
        sb_resistencias = [float(sb_r) for sb_r in sb_entry_resistencias.get().split(",") if sb_r.strip()]
        
        if not sb_resistencias:
            sb_result.config(text="Error: Ingrese al menos una resistencia válida.")
            return

        if sb_tip_conex == "Serie":
            sb_r = sb_serie(sb_resistencias)
        else:
            sb_r = sb_paralelo(sb_resistencias)

        sb_result.config(text=f"Resistencia equivalente: {sb_r:.2f} Ohm")
        sb_grafica(sb_tip_conex, sb_resistencias)
    except ValueError:
        sb_result.config(text="Error: Asegúrate de ingresar solo números separados por comas.")

sb_ventana = sb_tk.Tk()
sb_ventana.title("Cálculo de Resistencia Equivalente")
sb_label_intro = sb_tk.Label(sb_ventana, text="Ingrese las resistencias separadas por coma:")
sb_label_intro.pack()
sb_entry_resistencias = sb_tk.Entry(sb_ventana)
sb_entry_resistencias.pack()
sb_label_conexion = sb_tk.Label(sb_ventana, text="Seleccione el tipo de conexión:")
sb_label_conexion.pack()
sb_conex = sb_ttk.Combobox(sb_ventana, values=["Serie", "Paralelo"])
sb_conex.pack()
sb_boton_calcular = sb_tk.Button(sb_ventana, text="Calcular", command=sb_calcular)
sb_boton_calcular.pack()
sb_result = sb_tk.Label(sb_ventana, text="")
sb_result.pack()
sb_ventana.mainloop()
