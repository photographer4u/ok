import streamlit as st
import pandas as pd
import math
from pathlib import Path
def calculate_carbon_footprint(data):
    # Constants for emission factors (in kg CO2 equivalent per unit)
    emission_factors = {
        "Electricity (kWh)": 0.5,  # Placeholder value for electricity emission factor
        "Transportation (miles)": 0.2,  # Placeholder value for transportation emission factor
        "Waste (tons)": 0.1  # Placeholder value for waste emission factor
    }
    
    # Calculate total emission for each activity and sum them up
    total_emission = sum(data.get(key, 0) * factor for key, factor in emission_factors.items())
    return total_emission

def main():
    st.title("Emission Calculator")
    
    st.write("Enter data for different activities contributing to carbon emissions:")
    data = {}
    data["Electricity (kWh)"] = st.number_input("Electricity", min_value=0.0, step=0.1)
    data["Transportation (miles)"] = st.number_input("Transportation", min_value=0.0, step=0.1)
    data["Waste (tons)"] = st.number_input("Waste", min_value=0.0, step=0.1)

    if st.button("Calculate Carbon Footprint"):
        total_emission = calculate_carbon_footprint(data)
        st.success(f"Total Carbon Footprint: {total_emission} kg CO2 equivalent")

if __name__ == "__main__":
    main()
