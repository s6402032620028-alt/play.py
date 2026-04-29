import streamlit as st
import json

# โหลดข้อมูล
with open("data/lessons.json", "r") as f:
    lessons = json.load(f)

with open("data/quiz.json", "r") as f:
    quiz_data = json.load(f)

st.set_page_config(page_title="Revit Learning Hub", layout="wide")

st.title("🏗️ Revit Learning Hub")
st.write("เรียนรู้การใช้งาน Revit แบบ Interactive")

# Sidebar
menu = st.sidebar.selectbox("เลือกเมนู", ["📚 Lessons", "🧪 Quiz", "🔍 Search"])

# -------------------------
# 📚 Lessons Section
# -------------------------
if menu == "📚 Lessons":
    topic = st.selectbox("เลือกหัวข้อ", list(lessons.keys()))

    st.header(topic)
    st.write(lessons[topic]["description"])

    for step in lessons[topic]["steps"]:
        st.subheader(step["title"])
        st.write(step["content"])

        if step.get("image"):
            st.image(step["image"])

        if step.get("video"):
            st.video(step["video"])

# -------------------------
# 🧪 Quiz Section
# -------------------------
elif menu == "🧪 Quiz":
    score = 0

    for i, q in enumerate(quiz_data):
        st.subheader(f"Q{i+1}: {q['question']}")
        answer = st.radio("เลือกคำตอบ", q["options"], key=i)

        if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
            if answer == q["answer"]:
                st.success("ถูกต้อง!")
                score += 1
            else:
                st.error(f"ผิด! คำตอบคือ {q['answer']}")

# -------------------------
# 🔍 Search Section
# -------------------------
elif menu == "🔍 Search":
    keyword = st.text_input("ค้นหาเครื่องมือ")

    if keyword:
        for topic, content in lessons.items():
            if keyword.lower() in topic.lower():
                st.write(f"🔹 {topic}")
