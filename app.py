import streamlit as st
import numpy as np
from utils.physics import calculate_pressure
from utils.visualization import render_3d_model

# Title
st.title("Pascal's Law Simulation")

# Sidebar inputs
radius = st.sidebar.slider("Radius (m)", min_value=0.1, max_value=1.0, step=0.01)
force = st.sidebar.slider("Applied Force (N)", min_value=1, max_value=1000, step=1)
animal = st.sidebar.selectbox("Select Animal", ["Elephant", "Cat", "Dog"])
mass_dict = {"Elephant": 5000, "Cat": 5, "Dog": 10}

# Calculate pressure
area = np.pi * radius**2
pressure = calculate_pressure(force, area)

# Display results
st.write(f"Animal: {animal}, Mass: {mass_dict[animal]} kg")
st.write(f"Pressure: {pressure:.2f} Pa")

# Render 3D model
render_3d_model(animal)

# Lottie animation placeholder
st.markdown("#### (Optional) Add animations here for visual flair!")
