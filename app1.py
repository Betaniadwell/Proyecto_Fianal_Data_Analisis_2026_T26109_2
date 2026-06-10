import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Estilo
sns.set_theme(style="whitegrid", context="talk")

# Definimos el tamaño del lienzo
plt.figure(figsize=(10,6))

# Graficamos
sns.lineplot(data=datos_anuales, x="month", y="precio", hue="producto", palette = "Set2")

# Ticks (valores de eje)
plt.tick_params(axis='both', labelsize=10)

# Ajustes de título y ejes
plt.title('Ingresos brutos ventas por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ingresos', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()
st.pyplot(plt.gcf())
plt.clf()



# Estilo
sns.set_theme(style="whitegrid", context="talk")

# Definimos el tamaño del lienzo
plt.figure(figsize=(10,6))

# Graficamos
sns.lineplot(data=datos_anualesl, x="month", y="cantidad", hue="producto", palette = "Set2")

# Ticks (valores de eje)
plt.tick_params(axis='both', labelsize=10)

# Ajustes de título y ejes
plt.title('Cantidades vendidas  por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Cantidades', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()

st.pylot(plt.gcf())




