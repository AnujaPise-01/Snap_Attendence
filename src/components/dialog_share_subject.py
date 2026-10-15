import streamlit as st
from src.UI.style_base_layout import style_base_layout3
import segno
import io
@st.dialog("Share Class Link")
def share_subject_dialog(subject_name,subject_code):
    
    app_domain = "snapclass-main07.streamlit.app"  # Replace with your actual app domain
    join_url = f"{app_domain}/?join-code={subject_code}"
    st.header("Scan to Join")

    qr = segno.make(join_url)

    out = io.BytesIO()
    qr.save(out, kind='png', scale=10)

    col1 , col2 = st.columns(2)

    with col1:
        style_base_layout3()
        st.markdown(
        "<h3 style='color: white;'>Copy Link</h3>",
        unsafe_allow_html=True
    )
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info("Copy the link to share on Whatsapp or Email")
    with col2:
        style_base_layout3()
        st.markdown(
            "<h3 style='color: white;'>Scan QR Code</h3>",
            unsafe_allow_html=True
        )
        st.image(out.getvalue(),caption="QRCODE for class joining")




