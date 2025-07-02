import streamlit as st

# --- Title and Introduction ---
st.set_page_config(page_title="Symmetriq | Ideal Body Proportions Calculator", layout="centered")
st.title("Symmetriq")
st.subheader("Ideal Body Proportions Calculator")
st.markdown("""
Enter your body measurements to calculate your ideal physique targets based on golden ratio and anthropometric models.
""")

# --- Input Form ---
st.sidebar.header("Your Measurements")
height = st.sidebar.number_input("Height (in inches)", min_value=50.0, max_value=90.0, value=70.0)
wrist = st.sidebar.number_input("Wrist Circumference (in)", min_value=4.0, max_value=10.0, value=5.5)
ankle = st.sidebar.number_input("Ankle Circumference (in)", min_value=5.0, max_value=12.0, value=7.5)
waist = st.sidebar.number_input("Waist Circumference (in)", min_value=20.0, max_value=50.0, value=29.0)
shoulders_input = st.sidebar.number_input("Current Shoulder Circumference (in) (optional)", min_value=30.0, max_value=70.0, value=0.0)

# --- Calculations ---
shoulder_ideal = round(waist * 1.618, 2)
chest_ideal = round(wrist * 6.5, 2)
arm_ideal = round(wrist * 2.5, 2)
forearm_ideal = round(wrist * 2.0, 2)
thigh_ideal = round(ankle * 2.0, 2)  # adjusted for average proportion
calf_ideal = round(ankle * 1.9, 2)

shoulder_ratio = round(shoulders_input / waist, 2) if shoulders_input > 0 else None

# --- Results Section ---
st.markdown("## Ideal Measurements")
st.markdown("Based on your inputs, here are your target proportions:")

st.table({
    "Body Part": ["Shoulders", "Chest", "Arms", "Forearms", "Thighs", "Calves"],
    "Ideal Measurement (in)": [
        shoulder_ideal,
        chest_ideal,
        arm_ideal,
        forearm_ideal,
        thigh_ideal,
        calf_ideal
    ]
})

if shoulder_ratio:
    st.markdown("## Current V-Taper Ratio")
    st.write(f"Shoulder to Waist Ratio: {shoulder_ratio} (Target: 1.618)")
    if shoulder_ratio < 1.618:
        diff = round(shoulder_ideal - shoulders_input, 2)
        st.info(f"You may need to add approximately {diff} inches to your shoulders to achieve the ideal V-taper.")
    else:
        st.success("You have achieved or exceeded the golden ratio V-taper.")

# --- Footer ---
st.markdown("---")
st.caption("Symmetriq is a physique symmetry calculator based on natural frame-based ideals. For educational and fitness guidance use only.")
