
from src.UI.style_base_layout import style_base_layout3
import streamlit as st
from src.database.db import enroll_student_to_subject
from src.database.db import supabase

@st.dialog("Enroll in Subject")
def enroll_dialog():
    style_base_layout3()
    st.write('Enter the subject code provided by your teacher to enroll in the subject')
    join_code = st.text_input("Subject Code",placeholder= "CS101")
    if st.button("Enroll Now", type = 'primary',width='stretch'):
        if join_code:
            res = supabase.table('subjects').select('subject_id,subject_code').eq('subject_code', join_code).execute()
            if res.data:
                subject=res.data[0]
                student_id = st.session_state.student_data['student_id']

                check = supabase.table('subject_students').select('*').eq('subject_id',subject['subject_id']).eq('student_id',student_id).execute()
                if check.data:
                    st.warning("You are already enrolled in this subject")
                else:
                    enroll_student_to_subject(student_id,subject['subject_id'])
                    st.success("Successfully Enrolled!")
                    import time
                    time.sleep(1)
                    st.rerun()


        else:
            st.warning("Please fill the subject code")

            
