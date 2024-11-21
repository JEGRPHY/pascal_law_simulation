import streamlit as st
import numpy as np
from utils.physics import calculate_pressure
from utils.visualization import render_3d_model
from streamlit_lottie import st_lottie
import json

# Function to load Lottie animations
def load_lottie(file_path):
    """
    Load a Lottie animation from a JSON file.
    :param file_path: Path to the Lottie JSON file.
    :return: Loaded Lottie animation.
    """
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error(f"Lottie animation not found: {file_path}")
        return None

# Title
st.title("Pascal's Law Simulation")

# Sidebar inputs
st.sidebar.header("Input Parameters")
radius = st.sidebar.slider("Radius (m)", min_value=0.1, max_value=1.0, step=0.01)
force = st.sidebar.slider("Applied Force (N)", min_value=1, max_value=1000, step=1)
animal = st.sidebar.selectbox("Select Animal", ["Elephant", "Cat", "Dog"])
mass_dict = {"Elephant": 5000, "Cat": 5, "Dog": 10}
mass = mass_dict[animal]

# Calculate pressure
area = np.pi * radius**2
pressure = calculate_pressure(force, area)

# Display results
st.subheader("Results")
st.write(f"**Selected Animal:** {animal} (Mass: {mass} kg)")
st.write(f"**Cross-sectional Area:** {area:.2f} m²")
st.write(f"**Pressure:** {pressure:.2f} Pa")

# Render 3D model
st.subheader("Visualization")
render_3d_model(animal)

# Add a Lottie animation
st.subheader("Animation")
lottie_animation = load_lottie("assets/lottie/animation.json")
if lottie_animation:
    st_lottie(lottie_animation, height=300)

# Footer
st.markdown("---")
st.markdown("Developed by [Your Name or Organization]")
