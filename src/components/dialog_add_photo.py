import streamlit as st 
from src.database.db import enroll_student_to_subject 
from src.database.config import supabase 
from PIL import Image 
import time


@st.dialog("Capture or upload photos")
def add_photos_dialog():

    st.write("Add classroom photo to scan for attendance")

    if 'photo_tab' not in st.session_state:
        st.session_state.photo_tab = 'camera'

    col1, col2 = st.columns(2)

    with col1:
        type_camera = "primary" if st.session_state.photo_tab == "camera" else 'tertiary'
        if st.button('camera', type = type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    
    with col2:
        type_upload = "primary" if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('upload photos', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    
    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input("Take Snapshot", key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast("Photo Captured")
            st.rerun()


    if st.session_state.photo_tab == 'upload':
        uploaded_files = st.file_uploader("Choose image files", type=['jpg', 'png', 'jpeg'], accespt_mutiple_files=True, key='dialog_upload')

        if uploaded_files:
            for f in uploaded_files:
                st.session_state.attendance_images.append(Image.open(f))

            st.toast("Photo Uploaded Successfully")
            st.rerun()

    st.divider()