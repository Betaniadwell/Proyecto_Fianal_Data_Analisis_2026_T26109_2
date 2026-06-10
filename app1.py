import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 1. CARGAR LOS DATOS (¡Esto es lo más importante que faltaba!)
datos_anuales = pd.read_csv("datos_anuales.csv")


# 2. PRIMER GRÁFICO (Ingresos)
# Estilo
sns.set_theme(style="whitegrid", context="talk")

# Definimos el tamaño del lienzo
plt.figure(figsize=(10,6))

# Graficamos usando tus datos
sns.lineplot(data=datos_anuales, x="month", y="precio", hue="producto", palette="Set2")

# Ticks (valores de eje)
plt.tick_params(axis='both', labelsize=10)

# Ajustes de título y ejes
plt.title('Ingresos brutos ventas por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ingresos', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()

# Mostramos el primer gráfico en Streamlit
st.pyplot(plt.gcf())
plt.clf()


# 3. SEGUNDO GRÁFICO (Cantidades)
# Estilo
sns.set_theme(style="whitegrid", context="talk")

# Definimos el tamaño del lienzo
plt.figure(figsize=(10,6))

# Graficamos usando tus datos
sns.lineplot(data=datos_anuales, x="month", y="cantidad", hue="producto", palette="Set2")

# Ticks (valores de eje)
plt.tick_params(axis='both', labelsize=10)

# Ajustes de título y ejes
plt.title('Cantidades vendidas por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Cantidades', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()

# CORREGIDO: comando st.pyplot correcto sin errores de tipeo
st.pyplot(plt.gcf())
