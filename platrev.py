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
