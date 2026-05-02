import streamlit as st
from src.database.config import supabase
import time
from src.database.db import create_attendance


def show_attendance_result(df, logs):
    st.write('Please review attendance before confirming.')
    st.dataframe(df, hide_index=True, width='stretch')

    col1, col2 = st.columns(2)

    with col1:
        if st.button('Discard', width='stretch'):
            st.session_state.voice_attendance_results = None
            st.session_state.attendance_images = []
            st.rerun()

    with col2:
        if st.button('Confirm & Save', width='stretch', type='primary'):
            try:
                # Fix: ensure student_id and subject_id are strings (UUIDs)
                cleaned_logs = []
                for log in logs:
                    cleaned_logs.append({
                        'student_id': str(log['student_id']),
                        'subject_id': str(log['subject_id']),
                        'timestamp': log['timestamp'],
                        'is_present': bool(log['is_present'])
                    })
                create_attendance(cleaned_logs)
                st.toast("Attendance saved!")
                st.session_state.attendance_images = []
                st.session_state.voice_attendance_results = None
                st.rerun()
            except Exception as e:
                st.error(f'Sync Failed: {e}')  # Show actual error


@st.dialog("Attendance Report")
def attendance_result_dialog(df, logs):
    show_attendance_result(df, logs)