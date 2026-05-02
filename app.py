import streamlit as st
import numpy as np
import pandas as pd
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

secciones= st.sidebar.selectbox("Secciones", ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"])
if secciones == "Home":
    st.title("Proyecto Aplicado en Streamlit – Fundamentos de Programación")
    
    col_texto, col_foto = st.columns([2, 1])
    with col_texto:
        st.write("**Módulo:** Especialización en Python for Analytics")
        st.write("**Nombre:** Leonel Eberth Escalante Izquierdo")
        st.write("**Edad:** 26 años")
        st.write("**Año:** 2026")
        
    with col_foto:
        st.image("logo.png", width=150) 
        
    col_izq, col_dmc, col_medio, col_py, col_der = st.columns([1.5, 1.2, 0.5, 1, 1.5])
    
    with col_dmc:
        st.image("logodmc.png", width=160)
    with col_py:
        st.image("python.png", width=90) 
        
    st.divider() 

    st.write("Este proyecto representa la primera aplicación práctica del módulo y permitirá evidenciar el uso de estructuras de datos, widgets, funciones, clases y lógica de programación en una interfaz interactiva.")
    
    st.markdown("### Tecnologías y Herramientas Usadas:")

    st.markdown("""
    * **Streamlit:** Construcción de la interfaz gráfica interactiva, uso de widgets y gestión de memoria con session_state.
    * **NumPy:** Procesamiento y estructuración de datos utilizando arreglos (arrays) multidimensionales.
    * **Pandas:** Transformación de listas y diccionarios en DataFrames para una visualización tabular limpia.
    * **Programación Orientada a Objetos (POO):** Uso de clases, atributos y métodos para empaquetar la lógica de negocio (Inventarios).
    * **Modularidad:** Importación de scripts externos (libreria_funciones_proyecto1, libreria_clases_proyecto1) para mantener el código principal ordenado.
    * **Lógica de Control:** Implementación de bucles condicionales, validaciones de seguridad (try...except) y diccionarios.
    """)

elif secciones == "Ejercicio 1":
    st.markdown("# Descripcion") 
    st.markdown("En este ejercicio se desarrollo un pequeño módulo para registrar movimientos financieros en una lista vacía.") 
   

    if "lista_movimientos" not in st.session_state:
        st.session_state.lista_movimientos = []

    concepto= st.text_input("Ingrese el concepto")
    tm= st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor= st.number_input("Igrese un Valor")


    colu1, colu2= st.columns(2)
    guardar= colu1.button("Guardar") 
    Borrar= colu2.button("Borrar")        

    if guardar:
        if concepto != "" and tm != "" and valor !="": 
            if tm == "Ingreso":
                nuevo_mov = {
                "Concepto": concepto,
                "Tipo": tm,
                "Valor": valor
                }
            if tm == "Gasto":
                nuevo_mov = {
                "Concepto": concepto,
                "Tipo": tm,
                "Valor": -valor
                }
            st.session_state.lista_movimientos.append(nuevo_mov)
            st.success("Movimiento guardado")
        else:
            st.error("Rellena todos los recuadros")

    if Borrar:
        if st.session_state.lista_movimientos:
            st.session_state.lista_movimientos.pop()
            st.success("Último movimiento borrado")

    Total_ingreso=0
    Total_gasto=0
    for movimientos in st.session_state.lista_movimientos:
        if movimientos["Tipo"] == "Ingreso":
            Total_ingreso += movimientos["Valor"]
        if movimientos["Tipo"] == "Gasto":
            Total_gasto += movimientos["Valor"]
    
    saldo_final= Total_ingreso + Total_gasto


    

    st.divider() 


    st.markdown("### Tabla de Movimientos")
    
    if len(st.session_state.lista_movimientos) == 0:
        st.info("No hay movimientos para mostrar.")
    else:
        st.dataframe(st.session_state.lista_movimientos, use_container_width=True)

    st.markdown("### Flujo de Caja")
    

    
    if saldo_final > 0:
        st.success("Hay ganancias") 
    elif saldo_final < 0:
        st.error("Hay perdidas") 
    else:
        st.warning("El flujo está en cero")
    
    dicc= {
        "Total ingreso" : Total_ingreso,
        "Total Gasto" : Total_gasto,
        "Resultado" : saldo_final
    }
    lista_final= [dicc]

    if not (Total_ingreso == 0 and Total_gasto== 0 and saldo_final== 0):
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Ingresos", f"S/ {Total_ingreso}")
        col2.metric("Total Gastos", f"S/ {Total_gasto}")
        col3.metric("Saldo Final", f"S/ {saldo_final}")

elif secciones == "Ejercicio 2":
    st.markdown("### Descripicion")
    st.markdown("En este ejercicio se deberá crear un formulario para registrar información usando arreglos de NumPy")

    st.markdown("## Registro de Productos")
    Producto = st.text_input("Ingrese el nombre del producto")
    Categoria = st.selectbox("Elija una categoria", ["Alimentos", "Higiene y belleza", "Cuidado del hogar", "Bebidas no alcohólicas" ]) 
    Precio = st.number_input("Precio")
    Cantidad = st.number_input("cantidad",1,step=1)
    tot = Precio*Cantidad

    Total =st.metric("Total", f"S/ {tot}")

    if "Registro" not in st.session_state:
        st.session_state.Registro = []

    colu1, colu2= st.columns(2)
    E2_guardar= colu1.button("Guardar") 
    E2_Borrar= colu2.button("Borrar")  


    if E2_guardar:
        if Producto != "" and Categoria != "" and Precio != 0 and Cantidad !="": 
            nuevo_reg = [Producto, Categoria, Precio, Cantidad, tot]
            st.session_state.Registro.append(nuevo_reg)
            st.success("Registro guardado")
        else:
            st.error("Rellena todos los recuadros")

    if E2_Borrar:
        if st.session_state.Registro:
            st.session_state.Registro.pop()
            st.success("Último registro borrado")

    st.divider() 


    st.markdown("### Tabla de Registros")
    
    if len(st.session_state.Registro) == 0:
        st.info("No hay registros para mostrar.")
    else:
        arreglo_lista = np.array(st.session_state.Registro)
        df_final = pd.DataFrame( arreglo_lista, columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"])

        st.dataframe(df_final, use_container_width=True)





elif secciones == "Ejercicio 3":

    st.markdown("## Cálculo de Indicadores Clave de Mantenimiento (KPIs)")
    if "historial" not in st.session_state:
        st.session_state.historial = []

    lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    E3_mes = st.selectbox("Seleccione el mes a evaluar", lista_meses)

    E3_tiempo_de_operacion = st.number_input("Ingrese el tiempo de operacion del mes (hr)")
    E3_fallas = st.number_input("Numero de fallas", 1)
    E3_reparacion = st.number_input("Ingrese el tiempo de raparacion (hr)")
    
    E3_guardar = st.button("Mostrar Resultado y guardar") 
    
    if E3_guardar:
        if E3_tiempo_de_operacion == 0 and E3_fallas == 1 and E3_reparacion == 0:
            st.info("Ingrese los datos")
        else:
            try:
                resultado = lf.calcular_indicadores_mantenimiento(E3_tiempo_de_operacion, E3_fallas, E3_reparacion)
                mtbf = resultado["mtbf_h"]
                mttr = resultado["mttr_h"]
                disponibilidad = resultado["disponibilidad_pct"]
                
                col1, col2, col3 = st.columns(3)
                col1.metric("MTBF", f"{mtbf} hrs")
                col2.metric("MTTR", f"{mttr} hrs")
                col3.metric("Disponibilidad", f"{disponibilidad} %")
                dicc3 = {
                    "Mes": E3_mes,
                    "MTBF": mtbf,
                    "MTTR": mttr,
                    "Disponibilidad" :  disponibilidad 
                }
                st.session_state.historial.append(dicc3)
                st.success(f"Cálculo de {E3_mes} guardado en el historial")

            except ValueError as e:
                st.error(f"Error en los datos ingresados: {e}")

    E3_borrar = st.button("Borrar ultimo resultado") 
    if E3_borrar:
        if len(st.session_state.historial) == 0:
            st.info("Sin datos")
        else:
            st.session_state.historial.pop()

    st.markdown("### Historial de Cálculos")
    if len(st.session_state.historial) == 0:
        st.info("No hay cálculos para mostrar.")
    else:
        st.dataframe(st.session_state.historial, use_container_width= True)



elif secciones == "Ejercicio 4":
    st.markdown("### Descripción")
    st.markdown("En este ejercicio implementaremos Programación Orientada a Objetos (POO) usando clases para gestionar el inventario.")
    
    st.markdown("## Registro Inteligente de Inventario")

    if "inventario_poo" not in st.session_state:
        st.session_state.inventario_poo = []

    col1, col2 = st.columns(2)
    with col1:
        E4_nombre = st.text_input("Nombre del Producto")
        E4_costo = st.number_input("Costo Unitario (S/)", min_value=0.01)
        E4_precio = st.number_input("Precio de Venta (S/)", min_value=0.01)
    with col2:
        E4_stock_actual = st.number_input("Stock Actual", min_value=0, step=1)
        E4_stock_minimo = st.number_input("Stock Mínimo Permitido", min_value=0, step=1)

    E4_guardar = st.button("Registrar y Analizar Producto")


    if E4_guardar:
        if E4_nombre == "":
            st.error("Por favor, ingresa el nombre del producto.")
        else:
            try:

                nuevo_producto = lc.InventarioProducto(
                    E4_nombre, 
                    E4_costo, 
                    E4_precio, 
                    E4_stock_actual, 
                    E4_stock_minimo
                )
                

                datos_empaquetados = nuevo_producto.resumen()
                
                st.session_state.inventario_poo.append(datos_empaquetados)
                st.success(f"Producto '{E4_nombre}' registrado y analizado con éxito.")
                
            except ValueError as e:

                st.error(f"Error en los datos: {e}")

    st.divider()


    st.markdown("### Panel de Control de Inventario")
    if len(st.session_state.inventario_poo) == 0:
        st.info("El inventario está vacío.")
    else:

        st.dataframe(st.session_state.inventario_poo, use_container_width=True)