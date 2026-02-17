
import streamlit as st
from pathlib import Path
from services.pdf_service import extract_text_from_pdf
from services.excel_service import export_excel
from services.logger_service import setup_logger
from engine.scorer import decide

BASE_DIR = Path(__file__).parent
logger = setup_logger(BASE_DIR)

st.set_page_config(page_title="Auditoría PDF PRO", layout="wide")
st.title("Auditoría PDF Clínica - Enterprise (Fixed)")

folder = st.text_input("Carpeta con PDFs")

if st.button("Ejecutar Auditoría"):
    base = Path(folder)
    pdfs = list(base.rglob("*.pdf"))

    results = []

    for pdf in pdfs:
        text = extract_text_from_pdf(pdf)
        hits = []
        decision = decide(hits)

        logger.info(f"{pdf.name} -> {decision}")

        results.append({
            "archivo": pdf.name,
            "decision": decision
        })

    export_excel(BASE_DIR / "reporte.xlsx", results)

    st.success("Auditoría completada")
    st.write(results)
