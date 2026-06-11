import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# =========================================================================
# 1. CARGA DE DATOS
# =========================================================================
datos_anuales = pd.read_csv("datos_anuales.csv")
resumen_cat_rango = pd.read_csv("resumen_cat.csv", index_col=0)
df_resumen = pd.read_csv("resumen_vtas.csv")

# =========================================================================
# 2. CONFIGURACIÓN DE LA BARRA LATERAL (SELECTORES INTERACTIVOS)
# =========================================================================
st.sidebar.header("🎯 Filtros del Dashboard")

# Obtenemos la lista de productos únicos de tu base de datos
productos_unicos = datos_anuales["producto"].unique()

# Creamos el selector interactivo (Menú desplegable)
producto_seleccionado = st.sidebar.selectbox(
    "Selecciona un Producto para las tendencias:",
    options=["Todos"] + list(productos_unicos)
)

# Lógica de filtrado: Si elige uno, filtramos la tabla; si elige 'Todos', se queda igual
if producto_seleccionado != "Todos":
    datos_filtrados = datos_anuales[datos_anuales["producto"] == producto_seleccionado]
else:
    datos_filtrados = datos_anuales.copy()


# =========================================================================
# 3. TÍTULO PRINCIPAL
# =========================================================================
st.title("📊 Dashboard de Control de Ventas y Categorías")
st.markdown("Análisis interactivo de rendimiento y distribución de productos.")


# =========================================================================
# 4. GRÁFICOS DE LÍNEAS (Filtrados dinámicamente)
# =========================================================================
st.header(f"📈 Tendencias Mensuales — Mostrando: {producto_seleccionado}")

# Gráfico 1: Ingresos Brutos
plt.clf()
sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(10,6))
# IMPORTANTE: Aquí pasamos 'datos_filtrados' en lugar de 'datos_anuales'
sns.lineplot(data=datos_filtrados, x="month", y="precio", hue="producto", palette="Set2")
plt.tick_params(axis='both', labelsize=10)
plt.title('Ingresos brutos ventas por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Ingresos', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()
st.pyplot(plt.gcf())

# Gráfico 2: Cantidades Vendidas
plt.clf()
plt.figure(figsize=(10,6))
# IMPORTANTE: Aquí también usamos 'datos_filtrados'
sns.lineplot(data=datos_filtrados, x="month", y="cantidad", hue="producto", palette="Set2")
plt.tick_params(axis='both', labelsize=10)
plt.title('Cantidades vendidas por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Cantidades', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()
st.pyplot(plt.gcf())


# =========================================================================
# 5. PARTICIPACIÓN SEGMENTO ORO
# =========================================================================
st.header("🥇 Segmentación del Mercado")

valores_oro = [5, 2, 1]
etiquetas_oro = ["Electrodomésticos", "Electrónica", "Decoración"]

plt.clf()
plt.figure(figsize=(10, 7))
plt.pie(
    valores_oro,
    labels=etiquetas_oro,
    autopct='%1.1f%%',
    startangle=140,
    colors=['#FFD700', '#3498db', '#2ecc71'], 
    explode=(0.1, 0, 0),  
    shadow=True
)
plt.title('Participación de Categorías en el Segmento "Oro"', fontsize=15, pad=20)
plt.legend(title="Categorías", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
st.pyplot(plt.gcf())


# =========================================================================
# 6. DISTRIBUCIÓN VENTAS TOTALES
# =========================================================================
st.header("🍰 Distribución Global de Ventas")

plt.clf()
plt.figure(figsize=(8, 8))
plt.pie(
    df_resumen['ventas_totales'],
    labels=df_resumen['categoria'],
    autopct='%1.1f%%',           
    startangle=140,              
    colors=['#ff9999','#66b3ff','#99ff99'], 
    explode=(0.05, 0.05, 0.05),  
    shadow=True                  
)
plt.title('Distribución de Ventas Totales por Categoría', fontsize=15)
plt.tight_layout()
st.pyplot(plt.gcf())
