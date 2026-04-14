import streamlit as st
import libreria_funciones as lf
st.title("Mi primera app")

st.sidebar.title("Datos")
st.image("logo.png", width=100)
st.sidebar.image("logodmc.png")
st.title("clase 5 funciones")

p=st.number_input("ingrese el monto principal", value=1200)
t=st.number_input("ingrese la tasa anual", value= 0.05)
a= st.slider("seleccione el numero de años de prestamo", min_value=1, max_value=5)
pa= st.number_input("cantidad de pagos por años", value=12)
cuota= lf.cuota_prestamo(p,t,a,pa)
st.write(cuota)
