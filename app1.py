import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# =========================================================================
# 1. CARGA DE DATOS (Leemos los 3 archivos CSV de tu repositorio)
# =========================================================================
datos_anuales = pd.read_csv("datos_anuales.csv")
resumen_cat_rango = pd.read_csv("resumen_cat.csv", index_col=0)
df_resumen = pd.read_csv("resumen_vtas.csv")

# Título principal de la aplicación web
st.title("📊 Dashboard de Control de Ventas y Categorías")
st.markdown("Análisis interactivo de rendimiento y distribución de productos.")

# =========================================================================
# 2. BLOQUE ORIGINAL: GRÁFICOS DE LÍNEAS (datos_anuales.csv)
# =========================================================================
st.header("📈 Tendencias Mensuales de Ventas")

# Gráfico 1: Ingresos Brutos
plt.clf()
sns.set_theme(style="whitegrid", context="talk")
plt.figure(figsize=(10,6))
sns.lineplot(data=datos_anuales, x="month", y="precio", hue="producto", palette="Set2")
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
sns.lineplot(data=datos_anuales, x="month", y="cantidad", hue="producto", palette="Set2")
plt.tick_params(axis='both', labelsize=10)
plt.title('Cantidades vendidas por mes altos productos', fontsize=14)
plt.xlabel('Mes', fontsize=12)
plt.ylabel('Cantidades', fontsize=12)
plt.legend(title='Producto', fontsize=10, title_fontsize=11)
plt.tight_layout()
st.pyplot(plt.gcf())


# =========================================================================
# 3. NUEVO BLOQUE: PARTICIPACIÓN SEGMENTO ORO (resumen_cat.csv)
# =========================================================================
# =========================================================================
# 3. NUEVO BLOQUE: PARTICIPACIÓN SEGMENTO ORO (resumen_cat.csv)
# =========================================================================
st.header("🥇 Segmentación del Mercado")

# LEEMOS EL ARCHIVO DE NUEVO PERO SIN OBLIGARLO A TENER ÍNDICE FIXED
resumen_cat_rango = pd.read_csv("resumen_cat.csv")

# TRUCO: Mostramos la tabla en la app para ver cómo se llaman las columnas reales
st.subheader("Visualización de los datos cargados:")
st.dataframe(resumen_cat_rango)

plt.clf()
plt.figure(figsize=(10, 7))

# Intentamos graficar usando las dos primeras columnas del archivo dinámicamente
columnas = resumen_cat_rango.columns
valores = resumen_cat_rango.iloc[:, 1] # Toma la segunda columna (valores)
etiquetas = resumen_cat_rango.iloc[:, 0] # Toma la primera columna (nombres)

plt.pie(
    valores,
    labels=etiquetas,
    autopct='%1.1f%%',
    startangle=140,
    colors=['#FFD700', '#3498db', '#2ecc71'],
    explode=(0.1, 0, 0) if len(valores) == 3 else None,  # Evita errores si no son 3 elementos
    shadow=True
)
plt.title('Participación de Categorías en el Segmento "Oro"', fontsize=15, pad=20)
plt.legend(title="Categorías", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.tight_layout()
st.pyplot(plt.gcf())




# =========================================================================
# 4. NUEVO BLOQUE: DISTRIBUCIÓN VENTAS TOTALES (resumen_vtas.csv)
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
