# Importa los módulos necesarios
import streamlit as st

# Título de la aplicación web
st.title('Calculadora de Jubilación')

# Información de entrada
edad_actual = st.number_input('Ingresa tu edad actual', min_value=0, max_value=100, value=25)
edad_jubilacion = st.number_input('Ingresa la edad a la que planeas jubilarte', min_value=0, max_value=100, value=65)
ahorro_actual = st.number_input('Ingresa cuánto dinero tienes ahorrado para la jubilación', min_value=0.0)
ahorro_mensual = st.number_input('Ingresa cuánto dinero planeas ahorrar cada mes hasta la jubilación', min_value=0.0)
tasa_interes = st.number_input('Ingresa la tasa de interés anual de tus ahorros (por ejemplo, 0.05 para un 5%)', min_value=0.0)

# Calcula los años hasta la jubilación y los ahorros totales
anios_hasta_jubilacion = edad_jubilacion - edad_actual
ahorros_totales = ahorro_actual

for _ in range(anios_hasta_jubilacion * 12):  # Asume que los ahorros se calculan mensualmente
    ahorros_totales += ahorro_mensual
    ahorros_totales += (ahorros_totales * tasa_interes) / 12  # Asume que los intereses se calculan mensualmente

# Muestra los resultados
st.write(f'Necesitarás {ahorros_totales:,.2f} dólares para jubilarte a los {edad_jubilacion} años.')
