import streamlit as st
import json
import os

# ฟังก์ชันโหลด JSON แบบกัน error
def load_json(filepath, default_data):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        st.warning(f"ไม่พบไฟล์: {filepath} → ใช้ค่า default")
        return default_data

# default data กันพัง
default_lessons = {
    "Move Tool": {
        "description": "ใช้สำหรับย้าย object",
        "steps": [
            {"title": "Step 1", "content": "เลือก object"},
            {"title": "Step 2", "content": "กด MV"}
        ]
    }
}

default_quiz = [
    {
        "question": "Move ใช้คำสั่งอะไร?",
        "options": ["MV", "CO", "AL"],
        "answer": "MV"
    }
]

# โหลดไฟล์ (ปลอดภัย)
lessons = load_json("data/lessons.json", default_lessons)
quiz_data = load_json("data/quiz.json", default_quiz)

# UI
st.title("🏗️ Revit Learning Hub")

menu = st.sidebar.selectbox("เมนู", ["Lessons", "Quiz"])

if menu == "Lessons":
    topic = st.selectbox("เลือกหัวข้อ", list(lessons.keys()))
    st.header(topic)

    for step in lessons[topic]["steps"]:
        st.subheader(step["title"])
        st.write(step["content"])

elif menu == "Quiz":
    for q in quiz_data:
        st.write(q["question"])
import streamlit as st
import json
import os

st.set_page_config(page_title="Revit Learning Hub", layout="wide")

# -----------------------
# Load Data
# -----------------------
def load_json(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return default

lessons = load_json("data/lessons.json", {})

# -----------------------
# UI Header
# -----------------------
st.markdown("""
    <h1 style='text-align: center;'>🏗️ Revit Learning Hub</h1>
""", unsafe_allow_html=True)

# -----------------------
# Select Topic
# -----------------------
topic = st.selectbox("📚 เลือกหัวข้อ", list(lessons.keys()))

lesson = lessons[topic]
steps = lesson["steps"]

# -----------------------
# Session State
# -----------------------
if "step" not in st.session_state:
    st.session_state.step = 0

# -----------------------
# Progress Bar
# -----------------------
progress = (st.session_state.step + 1) / len(steps)
st.progress(progress)

# -----------------------
# Show Step
# -----------------------
step = steps[st.session_state.step]

st.markdown(f"## {step['title']}")
st.write(step["content"])

# Highlight shortcut
if "MV" in step["content"]:
    st.info("⌨️ Shortcut: MV")

# Image
if step.get("image"):
    st.image(step["image"])

# Video
if step.get("video"):
    st.video(step["video"])

# -----------------------
# Navigation Buttons
# -----------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("⬅️ Previous") and st.session_state.step > 0:
        st.session_state.step -= 1

with col2:
    if st.button("Next ➡️") and st.session_state.step < len(steps) - 1:
        st.session_state.step += 1
