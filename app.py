import streamlit as st
from streamlit_option_menu import option_menu

# Configuración de la barra de navegación con pestañas
with st.sidebar:
    selected = option_menu(
        menu_title="Navegación",  # Título del menú
        options=["Nosotros", "Reporte"],  # Opciones del menú
        icons=["people", "activity"],  # Iconos de cada opción
        menu_icon="cast",  # Icono del menú general
        default_index=0,  # Índice por defecto al cargar
    )

# Pestaña "Nosotros"
if selected == "Nosotros":
    st.title("Presentación del Equipo de Trabajo")
    st.write("""
    **Equipo de Predicción de COVID-19**
    
    Nuestro equipo está compuesto por los siguientes miembros:
    
    - **Ignacio Cardetti** (Data Engineer): [LinkedIn](https://www.linkedin.com/in/ignaciocardetti/) | [GitHub](https://github.com/C4rde)
    - **Cande Utello** (Data Analyst): [LinkedIn](https://www.linkedin.com/in/candelautello/) | [GitHub](https://github.com/CandeUtello)
    - **Carlos Jose Ospino de Leon** (Data Analyst): [LinkedIn](https://www.linkedin.com/in/carlosdeleono/) | [GitHub](https://github.com/CarlosJDO30)
    - **Fabrizio Flamini** (Data Engineer): [LinkedIn](https://www.linkedin.com/in/fabrizioflamini/) | [GitHub](https://github.com/FlamInIFabrIzIo)
    - **Belkys Dellamea** (Data Analyst): [LinkedIn](https://www.linkedin.com/in/belkys-dellamea/) | [GitHub](https://github.com/Beldell)
    
    Nuestro objetivo es proporcionar predicciones precisas y útiles para ayudar en la optimización de vuelos y asientos.
    """)

# Pestaña "Reporte"
elif selected == "Reporte":
    st.title("Reporte de Power BI")
    embed_url = "https://app.powerbi.com/view?r=eyJrIjoiNTEzM2M3MjQtNDE2ZS00OTc2LTk5ZDEtZDg1OWUyZmRjZmIwIiwidCI6Ijk4YjVlNzlkLWEwODYtNGU3OC04NDUxLTgxMmE3MGM0NWRlNyIsImMiOjR9&pageName=ee96d4157dfda6adb7a8"
    
    # Usar la función iframe para incrustar el informe de Power BI
    st.components.v1.iframe(src=embed_url, height=800, width=1100)