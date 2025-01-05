import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
import os

# --- Función para generar el informe PDF ---
def generar_pdf(nombre, contenido, nombre_archivo):
    c = canvas.Canvas(nombre_archivo, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, f"Informe Automatizado para {nombre}")
    c.drawString(100, 730, contenido)
    c.drawString(100, 700, "Este informe fue generado automáticamente con Streamlit y ReportLab.")
    c.save()

# --- Función para firmar el PDF (Simulado) ---
def firmar_pdf(input_pdf, output_pdf, firma):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    # Simulación de la firma digital como metadatos
    writer.add_metadata({"/Firma": firma})
    with open(output_pdf, "wb") as f:
        writer.write(f)

# --- Interfaz de Streamlit ---
st.title("📑 Generador de Informes Automatizados con Firma Digital")

# Datos del usuario
nombre = st.text_input("Nombre del destinatario:")
contenido = st.text_area("Contenido del informe:")
firma = st.text_input("Firma digital (texto para simular una firma):")

if st.button("Generar y Firmar Informe"):
    if nombre and contenido and firma:
        nombre_archivo = "informe_generado.pdf"
        nombre_archivo_firmado = "informe_firmado.pdf"
        
        # Generar el PDF
        generar_pdf(nombre, contenido, nombre_archivo)
        
        # Firmar el PDF
        firmar_pdf(nombre_archivo, nombre_archivo_firmado, firma)
        
        st.success("✅ Informe generado y firmado correctamente.")
        
        # Descargar el PDF firmado
        with open(nombre_archivo_firmado, "rb") as file:
            st.download_button(
                "📥 Descargar Informe Firmado",
                file,
                file_name=nombre_archivo_firmado,
                mime="application/pdf"
            )
        
        # Mostrar enlace para impresión
        st.markdown(
            f'<a href="{nombre_archivo_firmado}" target="_blank">🖨️ Vista Previa para Imprimir</a>',
            unsafe_allow_html=True
        )
        
        # Eliminar archivos temporales (opcional)
        os.remove(nombre_archivo)
        os.remove(nombre_archivo_firmado)
    else:
        st.error("❌ Por favor, completa todos los campos antes de generar el informe.")
