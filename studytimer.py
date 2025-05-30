import streamlit as st
import time

st.set_page_config(page_title="منبه الدراسة - Pomodoro", page_icon="📚", layout="centered")
st.title("📚 منبه الدراسة - Pomodoro")

st.markdown("""
<style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("---")

# مدخلات الوقت
col1, col2 = st.columns(2)
study_hours = col1.number_input("كم مدة الدراسة؟ (بالساعات)", min_value=0, max_value=12, step=1)
study_minutes = col2.number_input("كم مدة الدراسة؟ (بالدقائق)", min_value=0, max_value=59, step=1)

col3, col4 = st.columns(2)
break_hours = col3.number_input("كم مدة البريك؟ (بالساعات)", min_value=0, max_value=3, step=1)
break_minutes = col4.number_input("كم مدة البريك؟ (بالدقائق)", min_value=0, max_value=59, step=1)

total_study_min = study_hours * 60 + study_minutes
total_break_min = break_hours * 60 + break_minutes

def countdown(minutes, label):
    with st.empty():
        total_secs = minutes * 60
        for sec in range(total_secs, -1, -1):
            mins, secs = divmod(sec, 60)
            timer_str = f"{mins:02d}:{secs:02d}"
            st.subheader(f"⏳ {label}: {timer_str}")
            time.sleep(1)

if st.button("🚀 ابدأ الجلسة"):
    if total_study_min == 0:
        st.error("مدة الدراسة يجب أن تكون أكثر من صفر!")
    else:
        countdown(total_study_min, "الدراسة")
        if total_break_min > 0:
            countdown(total_break_min, "البريك")
        st.success("🎉 انتهت الجلسة! ممتاز 👏")
