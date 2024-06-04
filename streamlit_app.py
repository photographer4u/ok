import streamlit as st
import pandas as pd
import numpy as np
import math
from pathlib import Path
import random
import streamlit as st
import random

# Placeholder function for carbon footprint calculation
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

# Placeholder function for setting goals
def set_goals(goals):
    # Placeholder function to simulate setting goals
    st.write("Goals set successfully!")

# Placeholder function for generating report
def generate_report(data):
    # Generate bar chart for carbon footprint by activity
    st.write("### Carbon Footprint by Activity")
    st.bar_chart(data)

# Placeholder function for game elements
def play_game():
    st.write("### Play Game")
    st.write("Welcome to the Digital Carbon Footprint Game!")
    st.write("Here are some game elements to get you started:")
    
    # Event Cards
    st.write("#### Event Cards:")
    event_cards = [
        "Green Commute Challenge: Track carpool or bike rides for a week to earn Energy Savings tokens.",
        "Unexpected Outage: Office building experiences a power outage. Emissions increase slightly this week. Lose 1 Energy Savings token."
    ]
    selected_event_card = st.selectbox("Select an Event Card:", event_cards)

    # Resource Tokens
    st.write("#### Resource Tokens:")
    energy_savings_tokens = st.slider("Energy Savings Tokens:", min_value=0, max_value=10, value=0)
    recycling_points = st.slider("Recycling Points:", min_value=0, max_value=10, value=0)
    water_conservation_tokens = st.slider("Water Conservation Tokens:", min_value=0, max_value=10, value=0)

    # Challenges & Rewards
    st.write("#### Challenges & Rewards:")
    daily_challenge = st.checkbox("Daily Challenge: Reduce energy consumption by 5%")
    if daily_challenge:
        st.success("Congratulations! You completed the Daily Challenge.")
        st.write("Earned 1 Energy Savings Token.")
        energy_savings_tokens += 1

    # Player Tokens
    st.write("#### Player Tokens:")
    total_tokens = energy_savings_tokens + recycling_points + water_conservation_tokens
    st.write(f"Total Tokens: {total_tokens}")

    # Goal Cards
    st.write("#### Goal Cards:")
    goals = [
        "Reduce Emissions by 20% in 3 months.",
        "Achieve Zero Waste in the office kitchen by next quarter."
    ]
    selected_goal = st.selectbox("Select a Goal Card:", goals)

def main():
    st.title("Digital Carbon Footprint Tracker")
    
    st.write("Enter data for different activities contributing to carbon emissions:")
    data = {}
    data["Electricity (kWh)"] = st.number_input("Electricity (kWh)", min_value=0.0, step=0.1)
    data["Transportation (miles)"] = st.number_input("Transportation (miles)", min_value=0.0, step=0.1)
    data["Waste (tons)"] = st.number_input("Waste (tons)", min_value=0.0, step=0.1)

    if st.button("Calculate Carbon Footprint"):
        total_emission = calculate_carbon_footprint(data)
        st.success(f"Total Carbon Footprint: {total_emission} kg CO2 equivalent")

    st.write("### Set Goals")
    goals = {}
    goals["Reduce Electricity Consumption (%)"] = st.number_input("Reduce Electricity Consumption (%)", min_value=0.0, step=0.1)
    goals["Reduce Transportation Emissions (%)"] = st.number_input("Reduce Transportation Emissions (%)", min_value=0.0, step=0.1)
    goals["Reduce Waste Generation (%)"] = st.number_input("Reduce Waste Generation (%)", min_value=0.0, step=0.1)
    if st.button("Set Goals"):
        set_goals(goals)

    st.write("### Generate Report")
    if st.button("Generate Report"):
        generate_report(data)

    play_game()

if __name__ == "__main__":
    main()

