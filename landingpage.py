import streamlit as st

# Custom CSS style
st.markdown("""
    <style>
        body { background-color: #f8f9fa; }
        .main { background-color: #f8f9fa; }
        .header {background:#4361ee;color:white;padding:1rem;position:sticky;top:0;z-index:100;box-shadow:0 2px 10px rgba(0,0,0,0.1);}
        .hero {padding:2rem 1rem;text-align:center;background: linear-gradient(135deg, #4361ee, #3a0ca3);color:white;}
        .section-title {text-align:center;margin-bottom:1.5rem;font-size:1.5rem;font-weight:600;}
        .feature-card {background:white;border-radius:10px;padding:1.5rem;box-shadow:0 4px 6px rgba(0,0,0,0.05);}
    </style>
""", unsafe_allow_html=True)
#to inject custom HTML and CSS

# Header
st.markdown('<div class="header"><h2>  </h2></div>', unsafe_allow_html=True)

# Hero section
st.markdown('<div class="hero"></div>', unsafe_allow_html=True)


# Features section
st.markdown('<h2 class="section-title">Majlis Kita</h2>', unsafe_allow_html=True)
st.markdown('<div class="feature-card">', unsafe_allow_html=True)
st.markdown('<h3 style="text-align:center;">Sila masukkan nombor ID</h3>', unsafe_allow_html=True)

# Input field (numeric only)
id_number = st.number_input("nombor ID", min_value=0, step=1, format="%d", help="Masukkan nombor ID sahaja", key="idnum")

# Center the button and give it full width using columns
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    hantar = st.button("Hantar", key="checkin", help="Klik untuk hantar nombor ID anda")

if hantar:
    if id_number != 0:
        st.success("Berjaya hantar")
    else:
        st.warning("Sila masukkan nombor ID")

st.markdown('</div>', unsafe_allow_html=True)