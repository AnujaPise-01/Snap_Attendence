import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.config import supabase
from PIL import Image
from src.database.db import create_attendence

import time

@st.dialog("Attendence Reports")
def attendence_result_dialog(df, logs):
    st.write('Please review attendence before confirming. ')
    st.dataframe(df , hide_index =True, width = 'stretch')

    col1 , col2 = st.columns(2)

    with col1:
        if st.button('Discard', width = 'stretch'):
            st.rerun()

    with col2:
        if st.button('Confirm & Save',width = 'stretch',type ='primary'):
            # try:
                create_attendence(logs)
                st.toast("Attendence Taken")
                st.session_state.attendence_images = []
                st.rerun()

            # except Exception as e:
            #     st.error('Sync failed!')
