import pandas as pd 
import plotly.graph_objects as go
import streamlit as st

# Titulo del encabezado de la aplicación
st.header('Cuadro de mandos interactivo')

# Leer los datos del archivo CSV
car_data = pd.read_csv(r'vehicles_us.csv')

st.write('Este conjunto de datos contiene información sobre anuncios de venta de coches en los Estados Unidos.')

# Crear un botón en la aplicación Streamlit
build_hist = st.checkbox('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if build_hist:
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Creación del botón para gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión (precio vs kilometraje)')

    fig2 = go.Figure(data=go.Scatter(
        x=car_data['odometer'],
        y=car_data['price'],
        mode='markers',
        marker=dict(color='royalblue', opacity=0.6)
    ))

    fig2.update_layout(title_text='Precio vs Kilometraje', xaxis_title='Kilometraje', yaxis_title='Precio (USD)')

    st.plotly_chart(fig2, use_container_width=True)