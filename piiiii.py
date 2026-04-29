import streamlit as st
import numpy as np

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Shallow Foundation Calculator",
    page_icon="🏗️",
    layout="centered"
)

# -------------------------------
# Title
# -------------------------------
st.title("🏗️ Shallow Foundation Bearing Capacity")
st.markdown("### Terzaghi Method")

st.divider()

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📥 Input Parameters")

col1, col2 = st.columns(2)

with col1:
    B = st.number_input("Width B (m)", min_value=0.1, value=1.0)
    L = st.number_input("Length L (m)", min_value=0.1, value=1.0)
    D = st.number_input("Depth D (m)", min_value=0.1, value=1.0)

with col2:
    c = st.number_input("Cohesion c (kPa)", min_value=0.0, value=0.0)
    phi = st.number_input("Friction angle φ (degree)", min_value=0.0, value=30.0)
    gamma = st.number_input("Unit weight γ (kN/m³)", min_value=0.0, value=18.0)
    FS = st.number_input("Factor of Safety (FS)", min_value=1.0, value=3.0)

st.divider()

# -------------------------------
# Function for Nc, Nq, Ngamma
# -------------------------------
def bearing_factors(phi):
    phi_rad = np.radians(phi)

    if phi == 0:
        Nc = 5.7
        Nq = 1.0
        Ngamma = 0.0
    else:
        Nq = np.exp(np.pi * np.tan(phi_rad)) * (np.tan(np.radians(45 + phi/2))**2)
        Nc = (Nq - 1) / np.tan(phi_rad)
        Ngamma = 2 * (Nq + 1) * np.tan(phi_rad)

    return Nc, Nq, Ngamma

# -------------------------------
# Buttons
# -------------------------------
col_btn1, col_btn2 = st.columns(2)

calculate = col_btn1.button("🔍 Calculate")
clear = col_btn2.button("🧹 Clear")

# -------------------------------
# Clear Function
# -------------------------------
if clear:
    st.rerun()

# -------------------------------
# Calculation
# -------------------------------
if calculate:

    Nc, Nq, Ngamma = bearing_factors(phi)

    qult = (c * Nc) + (gamma * D * Nq) + (0.5 * gamma * B * Ngamma)
    qall = qult / FS

    st.subheader("📤 Results")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Ultimate Bearing Capacity (q_ult)", f"{qult:.2f} kPa")

    with col2:
        st.metric("Allowable Bearing Capacity (q_all)", f"{qall:.2f} kPa")

    st.success("✅ Calculation Complete")

# -------------------------------
# Footer
# -------------------------------
st.divider()
st.caption("Developed for Civil Engineers | Terzaghi Bearing Capacity Theory")
