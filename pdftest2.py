import streamlit as st
#base64, way to represent binary data (like a PDF file) as text, safely embedded within HTML string.
import base64


st.set_page_config(page_title="PDF TEST2")

def show_pdf(file_path):
    """
    Shows a PDF file on the webpage.
    """
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding the PDF in a view-only mode
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="500" height="800" type="application/pdf"></iframe>'

    # Rendering the HTML with the iframe
    st.markdown(pdf_display, unsafe_allow_html=True)

# Main Streamlit app
st.title("View a PDF File")
st.write("Below is a view-only PDF document.")
st.write("bole view-only mode pdf file in streamlit")

# Assuming 'busacc.pdf' is in the same directory as this script
show_pdf('busacc.pdf')