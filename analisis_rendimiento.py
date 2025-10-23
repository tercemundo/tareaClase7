
"""
Este script analiza los datos de ventas y marketing para identificar tendencias y oportunidades.
"""
import pandas as pd
import io

# Datos proporcionados en formato de cadena de texto
csv_data = """
Mes,Ventas ($),Visitantes,Conversión (%),Gasto Publicidad ($),Productos Vendidos
Ene,45000,15000,3.2,8500,450
Feb,52000,18500,2.9,9800,520
Mar,38000,12500,3.6,7200,380
Abr,61000,20500,3.1,11500,610
May,48000,16800,2.7,9300,480
"""

# Cargar los datos en un DataFrame de pandas
df = pd.read_csv(io.StringIO(csv_data))

# --- 1. Identificar el mes con mayor eficiencia (ventas / gasto en publicidad) ---
df['Eficiencia'] = df['Ventas ($)'] / df['Gasto Publicidad ($)']
mes_mayor_eficiencia = df.loc[df['Eficiencia'].idxmax()]

print("--- Análisis de Rendimiento de Ventas ---")
print("\n1. Mes con Mayor Eficiencia:")
print(f"El mes con mayor eficiencia es {mes_mayor_eficiencia['Mes']} con un ratio de {mes_mayor_eficiencia['Eficiencia']:.2f} (Ventas/Gasto).")

# --- 2. Determinar el mes con la mejor tasa de conversión ---
mes_mejor_conversion = df.loc[df['Conversión (%)'].idxmax()]

print("\n2. Mes con Mejor Tasa de Conversión:")
print(f"El mes con la mejor tasa de conversión es {mes_mejor_conversion['Mes']} con un {mes_mejor_conversion['Conversión (%)']}% de conversión.")
print("Análisis de la causa: A pesar del menor gasto publicitario y número de visitantes, una tasa de conversión más alta sugiere campañas más enfocadas y efectivas.")

# --- 3. Calcular el ticket promedio (ventas / productos) por mes ---
df['Ticket Promedio'] = df['Ventas ($)'] / df['Productos Vendidos']

print("\n3. Ticket Promedio Mensual:")
print(df[['Mes', 'Ticket Promedio']].to_string(index=False))

# --- 4. Evaluar la relación entre visitantes y ventas ---
correlacion = df['Visitantes'].corr(df['Ventas ($)'])

print("\n4. Relación entre Visitantes y Ventas:")
print(f"La correlación entre el número de visitantes y las ventas es de {correlacion:.2f}.")
print("Esto indica una fuerte relación positiva: a más visitantes, mayores son las ventas.")
print("\n--- Fin del Análisis ---")
