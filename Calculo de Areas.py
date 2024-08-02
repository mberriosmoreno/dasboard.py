import streamlit as st
from PIL import Image

# Mostrar imágenes de las formas centradas
def show_shape_image(shape):
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if shape == "Cuadrado":
            image = Image.open("Logo\Cuadrado.png")
        elif shape == "Triángulo":
            image = Image.open("Logo\Triangulo.png")
        elif shape == "Círculo":
            image = Image.open("Logo\Circulo.png")
        elif shape == "Rombo":
            image = Image.open("Logo\Rombo.png")
        st.image(image, caption=shape, use_column_width=True)

# Función para calcular el área del cuadrado
def calculate_square_area(side):
    return side * side

# Función para calcular el área del triángulo
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Función para calcular el área del círculo
def calculate_circle_area(radius):
    import math
    return math.pi * radius * radius

st.title("Calculadora de Áreas con Chatbot")

shape = st.selectbox("Selecciona una forma", ["Cuadrado", "Triángulo", "Círculo"])

# Mostrar la imagen de la forma seleccionada centrada
show_shape_image(shape)

if shape == "Cuadrado":
    side = st.number_input("Introduce el lado del cuadrado", min_value=0.0)
    if st.button("Calcular área"):
        area = calculate_square_area(side)
        st.write(f"El área del cuadrado es {area:.2f}")
        
elif shape == "Triángulo":
    base = st.number_input("Introduce la base del triángulo", min_value=0.0)
    height = st.number_input("Introduce la altura del triángulo", min_value=0.0)
    if st.button("Calcular área"):
        area = calculate_triangle_area(base, height)
        st.write(f"El área del triángulo es {area:.2f}")
        
elif shape == "Círculo":
    radius = st.number_input("Introduce el radio del círculo", min_value=0.0)
    if st.button("Calcular área"):
        area = calculate_circle_area(radius)
        st.write(f"El área del círculo es {area:.2f}")
