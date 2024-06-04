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
        "Water Conservation Effort: Implement water-saving measures to earn 1 Water Conservation token.",
        "Paperless Office Week: Go paperless for a week and earn 1 Recycling Point.",
        "Energy Audit: Conduct an energy audit and earn 1 Energy Savings token.",
        "Green Workshop: Attend a workshop on sustainability to earn 1 Recycling Point.",
        "Community Cleanup: Participate in a community cleanup event to earn 1 Recycling Point.",
        "Plant a Tree: Plant a tree to earn 1 Water Conservation token.",
        "Eco-friendly Commute: Switch to eco-friendly commute options for a week to earn 1 Energy Savings token."
    ]
    negative_events = [
        "Unexpected Outage: Office building experiences a power outage. Lose 1 Energy Savings token.",
        "Waste Overflow: Office produces excess waste this week. Lose 1 Recycling Point.",
        "Water Leak: Office experiences a water leak. Lose 1 Water Conservation token.",
        "Increased Printing: Office printing increases significantly. Lose 1 Recycling Point.",
        "Energy Spike: Unexpected energy usage spike. Lose 1 Energy Savings token.",
        "Missed Recycling: Missed recycling pickup. Lose 1 Recycling Point.",
        "Extra Travel: Increased business travel. Lose 1 Energy Savings token.",
        "Food Waste: Increased food waste in the office. Lose 1 Water Conservation token.",
        "Resource Overuse: Excessive use of office supplies. Lose 1 Recycling Point."
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
    weekly_challenge = st.checkbox("Weekly Challenge: Reduce office waste by 10%")
    monthly_challenge = st.checkbox("Monthly Challenge: Conduct a sustainability workshop")
    rewards = 0
    if daily_challenge:
        st.success("Daily Challenge completed! Earned 1 Energy Savings Token.")
        st.session_state.energy_savings += 1
    if thematic_challenge:
        st.success("Thematic Challenge completed! Earned 1 Recycling Point.")
        st.session_state.recycling_points += 1
    if weekly_challenge:
        st.success("Weekly Challenge completed! Earned 1 Water Conservation Token.")
        st.session_state.water_conservation += 1
    if monthly_challenge:
        st.success("Monthly Challenge completed! Earned 1 Recycling Point.")
        st.session_state.recycling_points += 1

# Function to handle badges and rewards
def badges_and_rewards():
    st.write("### Badges & Rewards")
    badges = [
        ("Energy Saver Badge", 5),
        ("Recycling Hero Badge", 5),
        ("Water Conservation Champion Badge", 5),
        ("Sustainability Leader Badge", 10),
        ("Green Office Advocate Badge", 8)
    ]
    selected_badge = st.selectbox("Select a Badge to Purchase:", [f"{badge[0]} - {badge[1]} Tokens" for badge in badges])
    if st.button("Purchase Badge"):
        badge_name, badge_cost = next(badge for badge in badges if badge[0] in selected_badge)
        if "Energy" in badge_name and st.session_state.energy_savings >= badge_cost:
            st.session_state.energy_savings -= badge_cost
            st.session_state.player_tokens += badge_cost * 2
            st.success(f"Purchased {badge_name}! Gained {badge_cost * 2} Player Tokens.")
        elif "Recycling" in badge_name and st.session_state.recycling_points >= badge_cost:
            st.session_state.recycling_points -= badge_cost
            st.session_state.player_tokens += badge_cost * 2
            st.success(f"Purchased {badge_name}! Gained {badge_cost * 2} Player Tokens.")
        elif "Water" in badge_name and st.session_state.water_conservation >= badge_cost:
            st.session_state.water_conservation -= badge_cost
            st.session_state.player_tokens += badge_cost * 2
            st.success(f"Purchased {badge_name}! Gained {badge_cost * 2} Player Tokens.")
        elif "Sustainability Leader" in badge_name and (
            st.session_state.energy_savings >= badge_cost or 
            st.session_state.recycling_points >= badge_cost or 
            st.session_state.water_conservation >= badge_cost
        ):
            max_tokens = max(st.session_state.energy_savings, st.session_state.recycling_points, st.session_state.water_conservation)
            if max_tokens == st.session_state.energy_savings:
                st.session_state.energy_savings -= badge_cost
            elif max_tokens == st.session_state.recycling_points:
                st.session_state.recycling_points -= badge_cost
            else:
                st.session_state.water_conservation -= badge_cost
            st.session_state.player_tokens += badge_cost * 2
            st.success(f"Purchased {badge_name}! Gained {badge_cost * 2} Player Tokens.")
        else:
            st.error("Not enough tokens to purchase this badge.")

# Function for player tokens
def player_tokens():
    st.write("### Player Tokens")
    st.write(f"Player Tokens: {st.session_state.player_tokens}")

# Function for goal cards
def goal_cards():
    st.write("### Goal Cards")
    goals = [
        "Reduce Emissions by 20% in 3 months.",
        "Achieve Zero Waste in the office kitchen by next quarter.",
        "Reduce Office Energy Consumption by 15% in 6 months.",
        "Implement a Comprehensive Recycling Program in 4 months.",
        "Switch to Renewable Energy Sources by year-end.",
        "Organize a Sustainability Workshop within the next 2 months.",
        "Achieve Paperless Office Status by end of the quarter.",
        "Reduce Business Travel Emissions by 10% in 3 months."
    ]
    selected_goal = st.selectbox("Select a Goal Card:", goals)
    if st.button("Complete Goal"):
        if "Reduce Emissions by 20%" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Reduce Emissions by 20%! Reduced Player Tokens by 10.")
        elif "Achieve Zero Waste" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Achieve Zero Waste! Reduced Player Tokens by 10.")
        elif "Reduce Office Energy Consumption" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Reduce Office Energy Consumption! Reduced Player Tokens by 10.")
        elif "Implement a Comprehensive Recycling Program" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state.player_tokens - 10)
            st.success("Completed Goal: Implement a Comprehensive Recycling Program! Reduced Player Tokens by 10.")
        elif "Switch to Renewable Energy Sources" in selected_goal:
            st.session_state.player_tokens = max(0, st.session_state st.success("Completed Goal: Switch to Renewable Energy Sources! Reduced Player Tokens by 10.")
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
