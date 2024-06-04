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

# Function to handle event cards
def event_cards():
    st.header("Event Cards")
    positive_events = [
        "Green Commute Challenge: Track carpool or bike rides for a week to earn Energy Savings tokens.",
        "Implement Office Recycling Program: Earn Recycling Points.",
        "Fix Leaks to Save Water: Earn Water Conservation Tokens."
    ]
    negative_events = [
        "Unexpected Outage: Office building experiences a power outage. Emissions increase slightly this week. Lose 1 Energy Savings token.",
        "Increased Business Travel: Additional business trips increase your carbon footprint. Lose 1 token.",
        "High Energy Consumption: Equipment left on overnight increases energy use. Lose 1 Energy Savings token."
    ]

    if st.button("Draw Event Card"):
        event_type = st.radio("Select Event Type", ["Positive", "Negative"])
        if event_type == "Positive":
            event = positive_events[st.session_state.positive_event_idx % len(positive_events)]
            st.session_state.positive_event_idx += 1
        else:
            event = negative_events[st.session_state.negative_event_idx % len(negative_events)]
            st.session_state.negative_event_idx += 1
        st.write(event)
        if "Green Commute Challenge" in event or "Implement Office Recycling Program" in event or "Fix Leaks to Save Water" in event:
            if st.button("Complete Positive Event"):
                st.session_state.energy_savings += 1
                st.success("Completed Positive Event! Gained 1 Energy Savings token.")
        else:
            if st.button("Complete Negative Event"):
                st.session_state.energy_savings = max(0, st.session_state.energy_savings - 1)
                st.warning("Completed Negative Event. Lost 1 Energy Savings token.")

# Function to handle resource tokens
def resource_tokens():
    st.header("Resource Tokens")
    st.write(f"Energy Savings: {st.session_state.energy_savings}")
    st.write(f"Recycling Points: {st.session_state.recycling_points}")
    st.write(f"Water Conservation Tokens: {st.session_state.water_conservation}")

# Function to handle challenges and rewards
def challenges_and_rewards():
    st.header("Challenges & Rewards")
    challenges = [
        "Daily Goal: Reduce energy consumption by 5%.",
        "Weekly Goal: Participate in a carpool or bike to work.",
        "Monthly Goal: Organize a recycling drive at the office."
    ]
    if st.button("Start Challenge"):
        challenge = challenges[st.session_state.challenge_idx % len(challenges)]
        st.session_state.challenge_idx += 1
        st.write(challenge)
        if st.button("Complete Challenge"):
            st.session_state.energy_savings += 2
            st.success("Completed Challenge! Gained 2 Energy Savings tokens.")

# Function to handle badges and rewards
def badges_and_rewards():
    st.header("Badges & Rewards")
    badges = {
        "Energy Saver Badge": 5,
        "Recycling Champion Badge": 5,
        "Water Conservation Badge": 5
    }
    for badge, price in badges.items():
        st.write(f"{badge} - {price} tokens")
        if st.button(f"Purchase {badge}"):
            if st.session_state.energy_savings >= price:
                st.session_state.energy_savings -= price
                st.session_state.player_tokens += 10
                st.success(f"Purchased {badge}! Player Tokens increased by 10.")
            else:
                st.warning("Not enough tokens to purchase this badge.")

# Function to handle player tokens
def player_tokens():
    st.header("Player Tokens")
    st.write(f"Player Tokens: {st.session_state.player_tokens}")

# Function to handle goal cards
def goal_cards():
    st.header("Goal Cards")
    goals = [
        "Reduce Emissions by 20% in 3 months.",
        "Achieve Zero Waste in the office kitchen by next quarter.",
        "Switch to Renewable Energy Sources",
        "Organize a Sustainability Workshop",
        "Achieve Paperless Office Status",
        "Reduce Business Travel Emissions by 10%"
    ]
    selected_goal = st.selectbox("Select a Goal to Complete", goals)
    if st.button("Complete Goal"):
        if "Reduce Emissions by 20%" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Reduce Emissions by 20%! Reduced Player Tokens by 10.")
        elif "Achieve Zero Waste" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Achieve Zero Waste! Reduced Player Tokens by 10.")
        elif "Switch to Renewable Energy Sources" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Switch to Renewable Energy Sources! Reduced Player Tokens by 10.")
        elif "Organize a Sustainability Workshop" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Organize a Sustainability Workshop! Reduced Player Tokens by 10.")
        elif "Achieve Paperless Office Status" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Achieve Paperless Office Status! Reduced Player Tokens by 10.")
        elif "Reduce Business Travel Emissions" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Reduce Business Travel Emissions by 10%! Reduced Player Tokens by 10.")

# Initialize session state
if "player_tokens" not in st.session_state:
    st.session_state.player_tokens = 50
if "energy_savings" not in st.session_state:
    st.session_state.energy_savings = 0
if "recycling_points" not in st.session_state:
    st.session_state.recycling_points = 0
if "water_conservation" not in st.session_state:
    st.session_state.water_conservation = 0
if "positive_event_idx" not in st.session_state:
    st.session_state.positive_event_idx = 0
if "negative_event_idx" not in st.session_state:
    st.session_state.negative_event_idx = 0
if "challenge_idx" not in st.session_state:
    st.session_state.challenge_idx = 0

# Streamlit app layout
def main():
    st.title("Digital Carbon Footprint Tracker")
    
    # Carbon Footprint Calculator
    st.header("Carbon Footprint Calculator")
    electricity = st.number_input("Electricity (kWh)", min_value=0, value=0)
    transportation = st.number_input("Transportation (miles)", min_value=0, value=0)
    waste = st.number_input("Waste (tons)", min_value=0, value=0)
    data = {"Electricity (kWh)": electricity, "Transportation (miles)": transportation, "Waste (tons)": waste}
    
    if st.button("Calculate Carbon Footprint"):
        total_emission = calculate_carbon_footprint(data)
        st.write(f"Total Carbon Footprint: {total_emission:.2f} tons CO2")
    
    # Event Cards
    event_cards()
    
    # Resource Tokens
    resource_tokens()
    
    # Challenges & Rewards
    challenges_and_rewards()
    
    # Badges & Rewards
    badges_and_rewards()
    
    # Player Tokens
    player_tokens()
    
    # Goal Cards
    goal_cards()
    
    # Generate Report
    st.header("Generate Report")
    if st.button("Generate Report"):
        generate_report(data)
    
    # Set Goals
    st.header("Set Goals")
    goals = st.text_input("Enter your goals:")
    if st.button("Set Goals"):
        set_goals(goals)

if __name__ == "__main__":
    main()
