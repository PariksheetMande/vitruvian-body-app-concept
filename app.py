import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Symmetriq | Ideal Body Proportions Calculator", layout="centered")

# --- Sidebar Inputs ---
st.sidebar.header("Your Measurements")
page = st.sidebar.radio("Select Page", ["Calculator", "Vision & Roadmap"])

if page == "Calculator":
    st.title("Symmetriq")
    st.subheader("Ideal Body Proportions Calculator")
    st.markdown("""
    Enter your body measurements to calculate your ideal physique targets based on golden ratio and anthropometric models.
    """)

    height = st.sidebar.number_input("Height (in inches)", min_value=50.0, max_value=90.0, value=70.0)
    wrist = st.sidebar.number_input("Wrist Circumference (in)", min_value=4.0, max_value=10.0, value=5.5)
    ankle = st.sidebar.number_input("Ankle Circumference (in)", min_value=5.0, max_value=12.0, value=7.5)
    waist = st.sidebar.number_input("Waist Circumference (in)", min_value=20.0, max_value=50.0, value=29.0)
    shoulders_input = st.sidebar.number_input("Current Shoulder Circumference (in) (optional)", min_value=0.0, max_value=70.0, value=0.0)

    # --- Calculations ---
    shoulder_ideal = round(waist * 1.618, 2)
    chest_ideal = round(wrist * 6.5, 2)
    arm_ideal = round(wrist * 2.5, 2)
    forearm_ideal = round(wrist * 2.0, 2)
    thigh_ideal = round(ankle * 2.0, 2)
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

    st.markdown("---")
    st.caption("Symmetriq is a physique symmetry calculator based on natural frame-based ideals. For educational and fitness guidance use only.")

elif page == "Vision & Roadmap":
    st.title("Symmetriq")
    st.subheader("Vision")
    st.markdown("""
    Symmetriq is a supplementary tool for bodybuilders and fitness enthusiasts.

    It is inspired by Leonardo Da Vinci’s *Vitruvian Man* and based on the golden ratio and modern anthropometric science (i.e., bone structure and proportional symmetry).

    Our goal is to promote a **naturally attainable, aesthetically pleasing physique** — one that aligns with your unique genetic structure rather than a generalized or unrealistic ideal. Symmetriq aims to:
    
    - Provide clarity in aesthetic training goals
    - Promote body neutrality and discourage body dysmorphia
    - Reinforce that **perfection is personal**
    """)

    st.subheader("Future Scope & Improvements")
    st.markdown("""
    1. **Camera-based Measurements**: Use a smartphone camera to auto-detect and measure body dimensions.
    2. **AI-Generated Plans**: Integrate with AI tools to provide personalized workout and nutrition plans based on your schedule, intensity preferences, and physical structure.
    3. **Product Partnerships**: Promote verified nutrition and training products through sponsorships to help fund development.
    4. **Habit Education**: Offer structured content on healthy workout practices, timing, burnout avoidance, and the dangers of PEDs and steroids.
    5. **Injury Prevention & Recovery**: Include expert-designed warmups, joint health routines, and corrective exercises.
    """)

    st.markdown("---")
    st.caption("Symmetriq is evolving. This roadmap outlines our future as we build a trusted, educational tool for aesthetic fitness.")
