import streamlit as st
from src.components.header_home import header_dashboard
from src.UI.style_base_layout import style_base_dashboard
from src.UI.style_base_layout import style_base_layout2
from src.components.footer import footer_dashboard
from src.database.db import check_teacher_exists,create_teacher
from src.database.db import teacher_login , get_teacher_subjects
from src.components.subject_card import subject_card
from src.components.dialog_create_subject import create_subject_dialog
from src.components.dialog_share_subject import share_subject_dialog
from src.components.dialog_add_photos import add_photos_dialog
from src.pipelines.face_pipeline import predict_attendence
from src.components.dialog_attendance_result import attendence_result_dialog 
import pandas as pd
from datetime import datetime
import numpy as np
from src.database.config import supabase
from src.database.db import get_attendence_for_teacher
def teacher_screen():
    style_base_dashboard()
    
    style_base_layout2()
    if "teacher_data" in st.session_state:
         teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
         teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
         teacher_screen_register()
def teacher_dashboard():
     teacher_data = st.session_state.teacher_data
     c1,c2 = st.columns(2,vertical_alignment="center",gap="large")
     style_base_layout2()
     with c1:
             header_dashboard()
     with c2:
             st.subheader(f"Welcome, {teacher_data['name']}")
             if st.button("Logout",type='secondary',key='loginbackbtn',shortcut="ctrl+backspace"):
                 st.session_state['is_loged_in'] = False
                 del st.session_state.teacher_data
                 st.rerun()

     st.space()
     if "current_teacher_tab" not in st.session_state:
          st.session_state.current_teacher_tab = 'take_attendence'
     tab1,tab2,tab3 = st.columns(3)
     with tab1 :
          type1 = "primary" if st.session_state.current_teacher_tab == 'take_attendence' else "tertiary"
          if st.button("Take Attendence",width= 'stretch',type=type1,icon = ':material/ar_on_you:'):
               st.session_state.current_teacher_tab = 'take_attendence'
               st.rerun()
     with tab2 :
          type2 = "primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
          if st.button("Manage Subjects",width= 'stretch',type=type2,icon = ':material/book_ribbon:'):
               st.session_state.current_teacher_tab = 'manage_subjects'
               st.rerun()
     with tab3 :
          type3 = "primary" if st.session_state.current_teacher_tab == 'attendence_records' else "tertiary"
          if st.button("Attendence Records",width= 'stretch',type=type3,icon = ':material/cards_stack:'):
               st.session_state.current_teacher_tab = 'attendence_records'
               st.rerun()


     st.divider()
     if st.session_state.current_teacher_tab == "take_attendence":
          teacher_tab_take_attendence()
     if st.session_state.current_teacher_tab == "manage_subjects":
          teacher_tab_manage_subjects()
     if st.session_state.current_teacher_tab == "attendence_records":
          teacher_tab_attendence_records()


     footer_dashboard()

def teacher_tab_take_attendence():
     teacher_id =st.session_state.teacher_data['teacher_id']

     st.header('Take AI Attendence')
     if 'attendence_images' not in st.session_state:
          st.session_state.attendence_images = []
     subjects = get_teacher_subjects(teacher_id)

     if not subjects:
          st.warning("No Subjects Found , Create One to Begin!")
          return
     subject_options = {f"{s['name']} - {s['subject_code']}":s['subject_id'] for s in subjects}
     col1,col2 = st.columns([3,1],vertical_alignment='bottom')
     with col1 :
          selected_subject_label = st.selectbox("Select Subject",options=list(subject_options.keys()))
     with col2:
          if st.button('Add Photos', type='primary',icon =':material/photo_prints:', width = 'stretch'):
               add_photos_dialog()
     selected_subject_id = subject_options[selected_subject_label] 
     st.divider()
     if st.session_state.attendence_images:
          st.header('Added Photos')
          gallery_cols = st.columns(4)

          for idx , img in enumerate (st.session_state.attendence_images):
               with gallery_cols[idx % 4]:
                    st.image(img,width = 'stretch',caption=f'Photo {idx+1}')
     has_photos = bool(st.session_state.attendence_images)
     c1, c2 = st.columns(2)
     with c1:
               if st.button('Clear all photos',width = 'stretch',type ='tertiary',icon =':material/delete:', disabled= not has_photos):
                    st.session_state.attendence_images = []
                    st.rerun()
     with c2 :
               
               if st.button('Run Face Analysis',width = 'stretch',type ='secondary',icon =':material/thumb_up:', disabled= not has_photos):
                    with st.spinner('Deep scanning classroom photos ...'):
                         all_detected_ids = {}

                         for idx , img in enumerate(st.session_state.attendence_images):
                              img_np = np.array(img.convert('RGB'))

                              detected ,_,_ = predict_attendence(img_np)

                              if detected:
                                   for sid in detected.keys():
                                        student_id = int(sid)
                                        all_detected_ids.setdefault(student_id ,[]).append(f'Photo {idx+1}')
                         enrolled_res = supabase.table('subject_students').select("* , students(*)").eq('subject_id',selected_subject_id).execute()
                         enrolled_students = enrolled_res.data

                         if not enrolled_students:
                              st.warning('No students enrolled in this course')
                         else:
                              attendance_to_log = [] 
                              results = []

                              current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

                              for node in enrolled_students:
                                   student = node['students']
                                   sources = all_detected_ids.get(int(student['student_id']), [])
                                   is_present = len(sources)>0
                                   results.append({
                                        "Name": student['name'],
                                        "ID": student['student_id'],
                                        "Source": ",".join(sources) if is_present else "-",
                                        "Status": "Present" if is_present else "Absent"
                                          })
                                   attendance_to_log.append({
                                        'student_id': student['student_id'],
                                        'subject_id': selected_subject_id,
                                        'time_stamp': current_timestamp,
                                        'is_present':bool(is_present)
                                  })
                         attendence_result_dialog(pd.DataFrame(results),attendance_to_log)
def teacher_tab_manage_subjects ():
     
     teacher_id = st.session_state.teacher_data['teacher_id']
     col1 ,col2 = st.columns(2)
     with col1:
          st.header('Manage Subjects', width = 'stretch')
     with col2:
          if st.button('Create New Subject',width = 'content'):
               create_subject_dialog(teacher_id)
     # List all subjects
     subjects = get_teacher_subjects(teacher_id)
     if subjects:
          for sub in subjects:
               stats = [
                    ("🧑🏻‍🎓", "<span style='color: black;'>Students</span>", sub['total_students']),
                    ("📅", "<span style='color: black;'>Classes</span>", sub['total_classes']),
               ]
          def share_btn(s = sub):
               if st.button(f"Share Code:{s['name']}",key = f"share_{s['subject_code']}"):
                    share_subject_dialog(s['name'],s['subject_code'])
               st.space()
          subject_card(
               name = sub['name'],
               code = sub['subject_code'],
               section = sub['section'],
               stats = stats,
               footer_callback = share_btn
          )
     else:
         st.info("No Subjests Found , Create One Above") 


# def teacher_tab_attendence_records():
#      st.header('Attendence Records')

#      teacher_id = st.session_state.teacher_data['teacher_id']

#      records = get_attendence_for_teacher(teacher_id)

#      if not records:
#           return
#      data = []
#      for r in records:
#           ts = r.get('timestamp')
#           formatted_time = 'N/A'
#           sort_key = ''
#           if ts:
#                try:
#         # Handle trailing 'Z' if present in ISO format
#                     dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
#                     formatted_time = dt.strftime('%Y-%m-%d %I:%M %p')
#                     sort_key = (
#                          ts  # Keep the raw ISO string as a reliable sorting/grouping key
#                     )
#                except Exception:
#                     formatted_time = ts  # Fallback to raw string if parsing fails
#                     sort_key = ts
#           data.append({
#                "ts_group": ts.split(".") if ts else None,
#                "Time": datetime.fromisoformat(ts).strftime("%Y-%m-%d %I:%M %p") if ts else "N'A",
#                "Subject": r['subjects']['name'],
#                "Subject Code":r['subjects']['subject_code'],
#                "is_present": bool(r.get('is_present',False))
#           })
#      df = pd.DataFrame(data)


#      summary =(

#           df.groupby(['ts_group', 'Time','Subject' , 'Subject Code'])
#           .agg(
#                Present_Count = ('is_present','sum'),
#                Total_Count = ('is_present','count')
#           ).reset_index()
#      )
#           # Older pandas syntax fallback
#      # summary = (
#      # df.groupby(['ts_group', 'Time', 'Subject', 'Subject Code'])['is_present']
#      # .agg(Present_Count='sum', Total_Count='count').reset_index()
#      # )

#      summary['Attendance Stats'] = (
#           summary['Present_Count'].astype(str)+ "/"
#           + summary['Total_Count'].astype(str) + 'Students'
#      )
#      display_df = ( summary.sort_values(by = 'ts_group',ascending = False)
#                    [['Time','Subject','Subject Code','Attendance Stats']]
#                    )
#      st.dataframe(display_df , width = 'stretch', hide_index=True)
def teacher_tab_attendence_records():
    st.header("Attendance Records")

    teacher_data = st.session_state.get("teacher_data", {})
    teacher_id = teacher_data.get("teacher_id")

    if not teacher_id:
        st.warning("Teacher information is unavailable.")
        return

    records = get_attendence_for_teacher(teacher_id)

    if not records:
        st.info("No attendance records found.")
        return

    data = []
    for r in records:
        ts = r.get("timestamp")
        dt = None

        if ts:
            try:
                # Convert a trailing Z to an explicit UTC offset.
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            except (TypeError, ValueError):
                pass

        data.append({
            # A string is hashable and can be used as a pandas group key.
            "ts_group": dt.replace(microsecond=0).isoformat() if dt else str(ts or ""),
            "Time": dt.strftime("%Y-%m-%d %I:%M %p") if dt else str(ts or "N/A"),
            "Subject": (r.get("subjects") or {}).get("name", "Unknown"),
            "Subject Code": (r.get("subjects") or {}).get("subject_code", "N/A"),
            "is_present": bool(r.get("is_present", False)),
        })

    df = pd.DataFrame(data)

    summary = (
        df.groupby(
            ["ts_group", "Time", "Subject", "Subject Code"],
            dropna=False,
        )
        .agg(
            Present_Count=("is_present", "sum"),
            Total_Count=("is_present", "count"),
        )
        .reset_index()
    )

    summary["Attendance Stats"] = (
        summary["Present_Count"].astype(str)
        + "/"
        + summary["Total_Count"].astype(str)
        + " Students"
    )

    display_df = (
        summary.sort_values("ts_group", ascending=False)
        [["Time", "Subject", "Subject Code", "Attendance Stats"]]
    )

    st.dataframe(display_df, width="stretch", hide_index=True)
     

def login_teacher(username,password):
     if not username or not password:
          return False
     teacher = teacher_login(username,password)
     if teacher :
          st.session_state.user_role = 'teacher'
          st.session_state.teacher_data = teacher
          st.session_state.is_logged_in = True
          return True
     return False
def register_teacher(teacher_username,teacher_name,teacher_password,teacher_pass_confirm):
     if teacher_password != teacher_pass_confirm:
          return False,"Password doesn't match."
     if not teacher_username or not teacher_name or not teacher_password or not teacher_pass_confirm:
          return False,"All fields are required!"
     if check_teacher_exists(teacher_username):
               return False,"Username already taken"
     
     try:
        create_teacher(teacher_username,teacher_password,teacher_name)
        return True,"Successfully Created! Login Now"
     except Exception as e:
        return False,"unexpected Error!"
          
def teacher_screen_login():
    c1,c2 = st.columns(2,vertical_alignment="center",gap="large")
    style_base_layout2()
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="ctrl+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
    st.markdown("<h3>Login with password</h3>", unsafe_allow_html=True)
   
    st.space()
    st.space()


    teacher_username = st.text_input("Enter your username",placeholder='Anujapise')

    teacher_password = st.text_input("Enter your password",type='password',placeholder='Enter your password')

    st.divider()

    btncl1 , btncl2 = st.columns(2)
    with btncl1:
        if st.button('Login',icon=':material/passkey:',shortcut="ctrl+enter",type='secondary',width='stretch'):
           if login_teacher(teacher_username,teacher_password):
                st.toast("Welcome Back!")
                import time
                time.sleep(1)
                st.rerun()
           else:
                st.error("Invalide username and password combo")

    with btncl2:
        if st.button('Register Instead',icon=':material/passkey:',shortcut="ctrl+ tab",width='stretch',type='primary'):
            st.session_state.teacher_login_type = 'register'
    footer_dashboard()
    
def teacher_screen_register():
    c1,c2 = st.columns(2,vertical_alignment="center",gap="large")
    style_base_layout2()
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home",type='secondary',key='loginbackbtn',shortcut="ctrl+backspace"):
            st.session_state['login_type'] = None
            st.rerun()
             
    st.markdown("<h3>Register your teacher profile</h3>", unsafe_allow_html=True)
    st.space()
    st.space()
    teacher_username = st.text_input("Enter your username",placeholder='Anujapise')
    teacher_name = st.text_input("Enter your name",placeholder='Anuja Pise')
    teacher_password = st.text_input("Enter your password",type='password',placeholder='Enter your password')
    teacher_pass_confirm = st.text_input("Confirm your password",type='password',placeholder='Confirm your password')
    st.divider()
    btncl1 , btncl2 = st.columns(2)
    with btncl1:
            if st.button('Register Now',icon=':material/passkey:',type='secondary',width='stretch'):
                 success , message = register_teacher(teacher_username,teacher_name,teacher_password,teacher_pass_confirm)
                 if success:
                      st.success(message)
                      import time
                      time.sleep(2)
                      st.session_state.teacher_login_type = 'login'
                      st.rerun()
                 else:
                      st.error(message)
    with btncl2:
            if st.button('Login Instead',icon=':material/passkey:',width='stretch',type='primary'):
                st.session_state.teacher_login_type = 'login'        
    footer_dashboard()