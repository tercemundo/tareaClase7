import pandas as pd
from colorama import Fore, Back, Style, init

# Inicializar colorama
init(autoreset=True)

# Datos del CSV
data = {
    'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'Ventas ($)': [45000, 52000, 38000, 61000, 48000],
    'Visitantes': [15000, 18200, 12500, 20500, 16800],
    'Conversión (%)': [3.2, 2.9, 3.8, 3.1, 2.7],
    'Gasto Publicidad ($)': [8500, 9800, 7200, 11200, 9500],
    'Productos Vendidos': [450, 520, 380, 610, 480]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar título
print(f"\n{Back.BLUE}{Fore.WHITE} {'='*70} {Style.RESET_ALL}")
print(f"{Back.BLUE}{Fore.WHITE} ANÁLISIS DE RENDIMIENTO E-COMMERCE {Style.RESET_ALL}")
print(f"{Back.BLUE}{Fore.WHITE} {'='*70} {Style.RESET_ALL}\n")

# Mostrar datos originales
print(f"{Fore.CYAN}📊 DATOS ORIGINALES:{Style.RESET_ALL}")
print(df.to_string(index=False))
print()

# Calcular métricas
df['Eficiencia (Ventas/Gasto)'] = df['Ventas ($)'] / df['Gasto Publicidad ($)']
df['Ticket Promedio'] = df['Ventas ($)'] / df['Productos Vendidos']
df['Tasa Conversión Real'] = (df['Productos Vendidos'] / df['Visitantes']) * 100

# Análisis 1: Mes con mayor eficiencia
print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.GREEN}1️⃣  MES CON MAYOR EFICIENCIA (Ventas/Gasto Publicidad){Style.RESET_ALL}")
print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
mes_eficiente = df.loc[df['Eficiencia (Ventas/Gasto)'].idxmax()]
print(f"{Fore.YELLOW}Mes: {Style.RESET_ALL}{mes_eficiente['Mes']}")
print(f"{Fore.YELLOW}Eficiencia: {Style.RESET_ALL}{mes_eficiente['Eficiencia (Ventas/Gasto)']:.2f}")
print(f"{Fore.YELLOW}Ventas: {Style.RESET_ALL}${mes_eficiente['Ventas ($)']:,.0f}")
print(f"{Fore.YELLOW}Gasto: {Style.RESET_ALL}${mes_eficiente['Gasto Publicidad ($)']:,.0f}")
print()

# Análisis 2: Mejor tasa de conversión
print(f"{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}2️⃣  MES CON MEJOR TASA DE CONVERSIÓN{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}{'='*70}{Style.RESET_ALL}")
mes_conversion = df.loc[df['Conversión (%)'].idxmax()]
print(f"{Fore.YELLOW}Mes: {Style.RESET_ALL}{mes_conversion['Mes']}")
print(f"{Fore.YELLOW}Conversión: {Style.RESET_ALL}{mes_conversion['Conversión (%)']:.1f}%")
print(f"{Fore.YELLOW}Costo por conversión: {Style.RESET_ALL}${mes_conversion['Gasto Publicidad ($)'] / mes_conversion['Productos Vendidos']:.2f}")
print()

# Análisis 3: Ticket promedio por mes
print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.CYAN}3️⃣  TICKET PROMEDIO POR MES{Style.RESET_ALL}")
print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
for idx, row in df.iterrows():
    print(f"{Fore.YELLOW}{row['Mes']}: {Style.RESET_ALL}${row['Ticket Promedio']:.2f}")
print(f"\n{Fore.GREEN}Ticket Promedio General: ${df['Ticket Promedio'].mean():.2f}{Style.RESET_ALL}")
print()

# Análisis 4: Relación visitantes y ventas
print(f"{Fore.BLUE}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.BLUE}4️⃣  RELACIÓN VISITANTES Y VENTAS{Style.RESET_ALL}")
print(f"{Fore.BLUE}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}{'Mes':<6} {'Visitantes':<12} {'Productos':<12} {'Tasa Real %':<15}{Style.RESET_ALL}")
print(f"{Fore.WHITE}{'-'*50}{Style.RESET_ALL}")
for idx, row in df.iterrows():
    print(f"{row['Mes']:<6} {row['Visitantes']:<12} {row['Productos Vendidos']:<12} {row['Tasa Conversión Real']:<15.2f}")
print()

# Resumen final
print(f"{Back.GREEN}{Fore.BLACK} RESUMEN EJECUTIVO {Style.RESET_ALL}")
print(f"{Fore.GREEN}━{Style.RESET_ALL}" * 70)
print(f"{Fore.CYAN}✓{Style.RESET_ALL} Mejor mes en ventas: {Fore.YELLOW}{df.loc[df['Ventas ($)'].idxmax()]['Mes']}{Style.RESET_ALL} (${df['Ventas ($)'].max():,.0f})")
print(f"{Fore.CYAN}✓{Style.RESET_ALL} Mejor eficiencia publicitaria: {Fore.YELLOW}{mes_eficiente['Mes']}{Style.RESET_ALL} ({mes_eficiente['Eficiencia (Ventas/Gasto)']:.2f})")
print(f"{Fore.CYAN}✓{Style.RESET_ALL} Mejor conversión: {Fore.YELLOW}{mes_conversion['Mes']}{Style.RESET_ALL} ({mes_conversion['Conversión (%)']:.1f}%)")
print(f"{Fore.CYAN}✓{Style.RESET_ALL} Total ventas periodo: {Fore.YELLOW}${df['Ventas ($)'].sum():,.0f}{Style.RESET_ALL}")
print(f"{Fore.CYAN}✓{Style.RESET_ALL} Total gasto publicidad: {Fore.YELLOW}${df['Gasto Publicidad ($)'].sum():,.0f}{Style.RESET_ALL}")
print(f"{Fore.CYAN}✓{Style.RESET_ALL} ROI General: {Fore.YELLOW}{(df['Ventas ($)'].sum() / df['Gasto Publicidad ($)'].sum()):.2f}x{Style.RESET_ALL}")
print()