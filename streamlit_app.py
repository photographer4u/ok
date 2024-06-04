import streamlit as st
import pandas as pd
import numpy as np
import math
from pathlib import Path
import random

# Placeholder function for carbon footprint calculation
def calculate_carbon_footprint(data):
    emission_factors = {
        "Electricity (kWh)": 0.5,
        "Transportation (miles)": 0.2,
        "Waste (tons)": 0.1
    }
    total_emission = sum(data.get(key, 0) * factor for key, factor in emission_factors.items())
    return total_emission

# Placeholder function for setting goals
def set_goals(goals):
    st.write("Goals set successfully!")

# Placeholder function for generating report
def generate_report(data):
    st.write("### Carbon Footprint by Activity")
    st.bar_chart(data)

# Function to simulate event cards
def event_cards():
    st.write("### Event Cards")
    positive_events = [
        "Green Commute Challenge: Track carpool or bike rides for a week to earn 1 Energy Savings token.",
        "Office Recycling Initiative: Set up a recycling program to earn 1 Recycling Point.",
        "Water Conservation Effort: Implement water-saving measures to earn 1 Water Conservation token."
    ]
    negative_events = [
        "Unexpected Outage: Office building experiences a power outage. Lose 1 Energy Savings token.",
        "Waste Overflow: Office produces excess waste this week. Lose 1 Recycling Point.",
        "Water Leak: Office experiences a water leak. Lose 1 Water Conservation token."
    ]
    
    selected_positive_event = random.choice(positive_events)
    selected_negative_event = random.choice(negative_events)
    
    st.write(f"Positive Event: {selected_positive_event}")
    if st.button("Complete Positive Event"):
        if "Energy Savings" in selected_positive_event:
            st.session_state.energy_savings += 1
        elif "Recycling" in selected_positive_event:
            st.session_state.recycling_points += 1
        elif "Water Conservation" in selected_positive_event:
            st.session_state.water_conservation += 1

    st.write(f"Negative Event: {selected_negative_event}")
    if st.button("Complete Negative Event"):
        if "Energy Savings" in selected_negative_event:
            st.session_state.energy_savings = max(0, st.session_state.energy_savings - 1)
        elif "Recycling" in selected_negative_event:
            st.session_state.recycling_points = max(0, st.session_state.recycling_points - 1)
        elif "Water Conservation" in selected_negative_event:
            st.session_state.water_conservation = max(0, st.session_state.water_conservation - 1)
        st.session_state.player_tokens += 1

# Function to handle resource tokens
def resource_tokens():
    st.write("### Resource Tokens")
    st.write(f"Energy Savings Tokens: {st.session_state.energy_savings}")
    st.write(f"Recycling Points: {st.session_state.recycling_points}")
    st.write(f"Water Conservation Tokens: {st.session_state.water_conservation}")

# Function for challenges and rewards
def challenges_and_rewards():
    st.write("### Challenges & Rewards")
    daily_challenge = st.checkbox("Daily Challenge: Reduce energy consumption by 5%")
    thematic_challenge = st.checkbox("Thematic Challenge: Plant a tree for Earth Day")
    rewards = 0
    if daily_challenge:
        st.success("Daily Challenge completed! Earned 1 Energy Savings Token.")
        st.session_state.energy_savings += 1
    if thematic_challenge:
        st.success("Thematic Challenge completed! Earned 1 Recycling Point.")
        st.session_state.recycling_points += 1

# Function to handle badges and rewards
def badges_and_rewards():
    st.write("### Badges & Rewards")
    badges = ["Energy Saver Badge", "Recycling Hero Badge", "Water Conservation Champion Badge"]
    selected_badge = st.selectbox("Select a Badge to Purchase:", badges)
    if st.button("Purchase Badge"):
        if selected_badge == "Energy Saver Badge" and st.session_state.energy_savings >= 5:
            st.session_state.energy_savings -= 5
            st.session_state.player_tokens += 10
            st.success("Purchased Energy Saver Badge! Gained 10 Player Tokens.")
        elif selected_badge == "Recycling Hero Badge" and st.session_state.recycling_points >= 5:
            st.session_state.recycling_points -= 5
            st.session_state.player_tokens += 10
            st.success("Purchased Recycling Hero Badge! Gained 10 Player Tokens.")
        elif selected_badge == "Water Conservation Champion Badge" and st.session_state.water_conservation >= 5:
            st.session_state.water_conservation -= 5
            st.session_state.player_tokens += 10
            st.success("Purchased Water Conservation Champion Badge! Gained 10 Player Tokens.")
        else:
            st.error("Not enough tokens to purchase this badge.")

# Function for player tokens
def player_tokens():
    st.write("### Player Tokens")
    st.write(f"Player Tokens: {st.session_state.player_tokens}")

# Function for goal cards
def goal_cards():
    st.write("### Goal Cards")
    goals = ["Reduce Emissions by 20% in 3 months.", "Achieve Zero Waste in the office kitchen by next quarter."]
    selected_goal = st.selectbox("Select a Goal Card:", goals)
    if st.button("Complete Goal"):
        if selected_goal == "Reduce Emissions by 20% in 3 months.":
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Reduce Emissions by 20%! Reduced Player Tokens by 10.")
        elif selected_goal == "Achieve Zero Waste in the office kitchen by next quarter.":
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Achieve Zero Waste! Reduced Player Tokens by 10.")

def main():
    if 'energy_savings' not in st.session_state:
        st.session_state.energy_savings = 0
    if 'recycling_points' not in st.session_state:
        st.session_state.recycling_points = 0
    if 'water_conservation' not in st.session_state:
        st.session_state.water_conservation = 0
    if 'player_tokens' not in st.session_state:
        st.session_state.player_tokens = 50
    
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

    st.write("## Game Elements")
    event_cards()
    resource_tokens()
    challenges_and_rewards()
    badges_and_rewards()
    player_tokens()
    goal_cards()

if __name__ == "__main__":
    main()
