import streamlit as st

st.set_page_config(page_title="PDF TEST")

st.title("PDF File")
st.write("Click the button below to download.")
st.write("bole input pdf file in streamlit")

#file read directly from computer's local file system
with open("busacc.pdf", "rb") as file:
    btn = st.download_button(
            label="KPPIT PDF",
            data=file,
            file_name="busacc.pdf",
            mime="application/pdf"
          )
    