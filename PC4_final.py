# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

estilos_fondo = """
<style>
[data-testid="stAppViewContainer"]{
background-color: #94568d;
}
[data-testid="stSidebar"]{
background-color: #6e2e66;
}
div[data-baseweb="select"] > div{
background-color: #fcc7f6;
border-color: #fcc7f6;
color: #363435
}
[data-testid="stHeader"] {
background-color: #94568d;
}
</style>
"""

st.markdown(estilos_fondo, unsafe_allow_html=True)

# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y el atributo style se utiliza para agregar estilos CSS. 
st.markdown("<h1 style='text-align: center; color: rgb(250, 220, 247); font-size: 35px'>Creatividad en Movimiento: Mi Viaje Entre la Publicidad, el Ballet y la Programación</h1><br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
# col1.markdown("<img src='https://static.streamlit.io/examples/dog.jpg' width='250' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)
col1.image("images/cciara.jpeg", caption='Yo en el estudio de ballet', width=340)

texto = """Mi nombre es Cciara Alva y soy de Lima, Perú. Estudio Publicidad en la PUCP, lo que más me gusta de la carrera es su caracterísitica de ser multidiciplinaria; me permite desarrollar mi creatvidad y mi gusto por el estudio de la sociedad. Además, estudio desde los 12 años para ser bailarina profesional de ballet en el 'Ballet Municipal de Lima', este arte me apasiona por su capacidad de expresar y transmitir emociones sin necesidad de palabras, solo a través del cuerpo. Son dos profesiones que estudio y llevo en paralelo. En mis tiempos libres disfruto de la lectura, la pintura y ver series o películas. """  

col2.markdown(f"<div style='text-align: justify; font-size: 18px'>{texto}</div>", unsafe_allow_html=True)


st.markdown("<br><h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>", unsafe_allow_html=True)

texto2 = """Al principio, al adentrarme en el mundo de la programación con Python, 
me sentí un poco abrumada por la cantidad de conceptos nuevos y la lógica que debía aprender. 
Sin embargo, esa sensación pronto se transformó en curiosidad y entusiasmo a medida que comencé a entender cómo funcionaban los códigos y a resolver problemas simples. 
La satisfacción de ver mis primeros programas ejecutándose correctamente fue una gran motivación para seguir aprendiendo y mejorando mis habilidades."""

texto3 = """La programación me ha enseñado a pensar de manera lógica y estructurada, a descomponer problemas complejos en partes manejables y a ser perseverante ante los desafíos. 
Lo que más me gusta de programar es la posibilidad de crear soluciones innovadoras y eficientes para diversos problemas, además de la constante oportunidad de aprender algo nuevo. 
En el futuro, me gustaría utilizar la programación para desarrollar dashboards que faciliten la visualización de datos para proyectos publicitarios más conscientes y empáticos, entonces podrán contribuir positivamente a la sociedad."""

st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto2}</div><br>", unsafe_allow_html=True)
st.markdown(f"<div style='text-align: justify; font-size: 18px;'>{texto3}</div>", unsafe_allow_html=True)



sidebar.markdown("<h2 style='text-align: center;'>GRÁFICOS</h2>", unsafe_allow_html=True)
# Creamos una lista de gráficos
graficos = ['Gráfico Lenguas por familia', 'Gráfico lugar filmación de películas', 'Gráfico Sudamérica']

# Creamos un cuadro de selección en la barra lateral
grafico_seleccionado = sidebar.selectbox('Selecciona un gráfico', graficos)

# Mostramos el gráfico seleccionado
if grafico_seleccionado == 'Gráfico Lenguas por familia':
    sidebar.markdown("""<div style='text-align: justify '>El gráfico muestra la diversidad de lenguas por familia lingüística, destacando que la familia Arawakan tiene la mayor cantidad con 41 lenguas, seguida por Pano-Tacanan (20 lenguas) y Tupian (19 lenguas). 
                     La mayoría de las familias lingüísticas tienen un número pequeño de lenguas, con muchas familias representadas por solo una lengua cada una. Esta distribución refleja una gran diversidad lingüística con concentraciones significativas en unas pocas 
                     familias y sugiere la vulnerabilidad de muchas lenguas, especialmente aquellas en familias con solo una o pocas lenguas, subrayando la importancia de los esfuerzos de preservación.</div><br>""", unsafe_allow_html=True)
    sidebar.image("images/G_barras.jpeg", caption='Gráfico Lenguas por familia', width=500)
    pass
elif grafico_seleccionado == 'Gráfico lugar filmación de películas':
    sidebar.markdown("""<div style='text-align: justify'>El gráfico muestra la localización geográfica de los lugares asociados con el rodaje o la ambientación de varias películas icónicas, destacando la diversidad de escenarios cinematográficos. 
                     Jurassic Park está en América del Norte, representando las locaciones de Hawái. Titanic también en América del Norte, refiriéndose a Baja California, México, donde se filmaron escenas del naufragio. 
                     Gladiador en Europa, cubriendo Italia, Malta y Marruecos. Inception en Asia, con escenarios en Tokio, Japón. El Señor de los Anillos en Oceanía, específicamente en Nueva Zelanda, donde se filmó la trilogía. 
                     Este mapa ilustra cómo las grandes producciones abarcan múltiples continentes para crear ambientes auténticos y visualmente impresionantes.</div><br>""", unsafe_allow_html=True)
    sidebar.image("images/G_global.jpeg", caption='Gráfico lugar filmación de películas', width=500)
    pass
elif grafico_seleccionado == 'Gráfico Sudamérica':
    sidebar.markdown("""<div style='text-align: justify'>El gráfico muestra la distribución geográfica de la familia lingüística Arawakan en Sudamérica, destacando las ubicaciones de diferentes lenguas pertenecientes a esta familia. Las lenguas Arawakan están ampliamente dispersas por la región, con concentraciones significativas en países como Perú, Brasil, Bolivia, y Venezuela. 
                     <br>En Perú, encontramos lenguas como Asháninka y Nomatsiguenga, mientras que en Brasil se encuentran lenguas como Apurinã, Baure, y Paunaka. 
                     En Bolivia, destacan lenguas como Terena y Paunaka; y en Venezuela se hallan lenguas como Achagua y Lokono. 
                     Esta dispersión sugiere una amplia difusión histórica y cultural de los pueblos Arawakan a lo largo de Sudamérica. 
                     <br>Además, la presencia de estas lenguas en diversas zonas ecológicas, desde la Amazonía hasta los Andes, refleja la adaptación y diversidad cultural de los pueblos hablantes de lenguas Arawakan. 
                     El gráfico subraya la importancia de la preservación y el estudio de estas lenguas, muchas de las cuales están en peligro de extinción debido a la influencia de idiomas dominantes y cambios socioculturales.</div><br>""", unsafe_allow_html=True)
    sidebar.image("images/G_sudamerica.jpeg", caption='Mapa de las lenguas sudamericanas', width=450)
    pass