
import streamlit as st
from pathlib import Path
from engine.scorer import decide
from services.pdf_service import extract_text_from_pdf
from services.excel_service import export_excel
from services.file_service import copy_preserve_structure
from services.logger_service import setup_logger

BASE_DIR = Path(__file__).parent
logger = setup_logger(BASE_DIR)

st.set_page_config(page_title="Auditoría PDF Clínica Enterprise", layout="wide")
st.title("Auditoría PDF Clínica - Enterprise Full")

origin_folder = st.text_input("Carpeta ORIGEN (con subcarpetas)")
output_folder = st.text_input("Carpeta SALIDA")

if st.button("Ejecutar Auditoría"):

    origin = Path(origin_folder)
    output = Path(output_folder)

    approved_dir = output / "APROBADOS"
    rejected_dir = output / "RECHAZADOS"
    review_dir = output / "REVISION"

    approved_dir.mkdir(parents=True, exist_ok=True)
    rejected_dir.mkdir(parents=True, exist_ok=True)
    review_dir.mkdir(parents=True, exist_ok=True)

    pdfs = list(origin.rglob("*.pdf"))

    results = []

    for pdf in pdfs:
        text = extract_text_from_pdf(pdf)

        # Aquí iría tu motor completo de reglas
        hits = []

        decision = decide(hits)

        logger.info(f"{pdf.name} -> {decision}")

        results.append({
            "archivo": pdf.name,
            "ruta_relativa": str(pdf.relative_to(origin)),
            "decision": decision
        })

        if decision == "APROBADO":
            copy_preserve_structure(pdf, origin, approved_dir)

    export_excel(output / "reporte_auditoria.xlsx", results)

    st.success("Auditoría completada")
    st.write(results)
