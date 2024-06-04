import streamlit as st
import pandas as pd
import numpy as np
import math
from pathlib import Path
import random
import streamlit as st
import random

# Function to calculate carbon footprint
def calculate_carbon_footprint(data):
    emission_factors = {
        "Electricity (kWh)": 0.0003,
        "Transportation (miles)": 0.0004,
        "Waste (tons)": 0.001
    }
    total_emission = sum(data[key] * factor for key, factor in emission_factors.items())
    return total_emission
#Function to set goals
def set_goals():
    st.header("Set Goals")
    goal = st.text_input("Enter your goal for carbon footprint reduction (e.g., Reduce Emissions by 20% in 3 months)")
    if st.button("Set Goal"):
        st.session_state.goal = goal
        st.success("Goal set successfully")

# Function to generate a report using st.bar_chart
def generate_report(data):
    categories = list(data.keys())
    values = list(data.values())
    chart_data = {"Categories": categories, "Values": values}
    st.bar_chart(chart_data)

# Function to handle event cards
def event_cards():
    st.header("Event Cards")
    positive_events = [
        "Green Commute Challenge: Track carpool or bike rides for a week to earn Energy Savings tokens.",
        "Implement Office Recycling Program: Earn Recycling Points.",
        "Fix Leaks to Save Water: Earn Water Conservation Tokens.",
        "Switch to LED Bulbs: Earn Energy Savings tokens.",
        "Install Solar Panels: Earn Energy Savings tokens.",
        "Participate in Earth Day Activities: Earn Recycling Points.",
        "Community Clean-Up: Earn Recycling Points.",
        "Host a Sustainability Workshop: Earn Energy Savings tokens.",
        "Implement a No-Plastic Policy: Earn Recycling Points.",
        "Start a Composting Program: Earn Recycling Points."
    ]
    negative_events = [
        "Unexpected Outage: Office building experiences a power outage. Emissions increase slightly this week. Lose 1 Energy Savings token.",
        "Increased Business Travel: Additional business trips increase your carbon footprint. Lose 1 token.",
        "High Energy Consumption: Equipment left on overnight increases energy use. Lose 1 Energy Savings token.",
        "Paper Wastage: Excessive paper usage increases waste. Lose 1 Recycling Point.",
        "Water Leak: Unnoticed water leak increases consumption. Lose 1 Water Conservation Token.",
        "Overheating: Poor insulation increases energy use for cooling. Lose 1 Energy Savings token.",
        "Improper Waste Disposal: Lose 1 Recycling Point.",
        "Excessive Printing: Lose 1 Recycling Point.",
        "Neglected Maintenance: Lose 1 Energy Savings token.",
        "Wasteful Water Usage: Lose 1 Water Conservation Token."
    ]

    if st.button("Draw Event Card"):
        event_type = st.radio("Select Event Type", ["Positive", "Negative"])
        if event_type == "Positive":
            event = positive_events[st.session_state.positive_event_idx % len(positive_events)]
            st.session_state.positive_event_idx += 1
            st.session_state.tokens[event.split(":")[1].split(" ")[2]] += 1
        else:
            event = negative_events[st.session_state.negative_event_idx % len(negative_events)]
            st.session_state.negative_event_idx += 1
            st.session_state.tokens[event.split(":")[1].split(" ")[2]] -= 1
        st.write(event)



# Function to display and purchase badges
def display_badges():
    st.header("Badges")
    badges = {
        "Eco Warrior": {"Energy Savings tokens": 10, "Recycling Points": 10, "Water Conservation Tokens": 10},
        "Sustainability Champion": {"Energy Savings tokens": 20, "Recycling Points": 20, "Water Conservation Tokens": 20},
        "Green Guru": {"Energy Savings tokens": 30, "Recycling Points": 30, "Water Conservation Tokens": 30}
    }
    for badge, cost in badges.items():
        st.write(f"{badge} - Cost: {cost}")
        if st.button(f"Purchase {badge}"):
            if all(st.session_state.tokens[token] >= cost[token] for token in cost):
                for token in cost:
                    st.session_state.tokens[token] -= cost[token]
                st.session_state.badges.append(badge)
                st.success(f"Purchased {badge}")
            else:
                st.error(f"Not enough tokens to purchase {badge}")

# Function to handle player tokens
def player_tokens():
    st.header("Player Tokens")
    st.write(f"Player Tokens: {st.session_state.player_tokens}")

# Function to handle resource tokens
def resource_tokens():
    st.header("Resource Tokens")
    st.write(st.session_state.tokens)

# Function to handle goal cards
def goal_cards():
    st.header("Goal Cards")
    goals = [
        "Reduce Emissions by 20% in 3 months.",
        "Achieve Zero Waste in the office kitchen by next quarter.",
        "Reduce Energy Consumption by 10% this year.",
        "Implement a Paperless Office by next year.",
        "Achieve Water Savings of 15% in 6 months.",
        "Cut Down Business Travel Emissions by 25% in 1 year.",
        "Start a Green Building Certification Process.",
        "Achieve 50% Recycling Rate in the Office.",
        "Implement a Rainwater Harvesting System.",
        "Reduce Single-Use Plastics by 80% in 6 months."
    ]

    if st.button("Draw Goal Card"):
        goal = goals[st.session_state.goal_idx % len(goals)]
        st.session_state.goal_idx += 1
        st.session_state.goals.append(goal)
        st.write(goal)

# Function to handle challenges and rewards
def challenges_and_rewards():
    st.header("Challenges & Rewards")
    challenges = [
        "Reduce energy consumption by 5% this week.",
        "Implement a recycling program in the office.",
        "Conduct a water audit and reduce wastage."
    ]

    if st.button("Draw Challenge"):
        challenge = challenges[st.session_state.challenge_idx % len(challenges)]
        st.session_state.challenge_idx += 1
        st.write(challenge)

    st.header("Rewards")
    for badge in st.session_state.badges:
        st.write(f"Badge: {badge}")

# Main function to run the Streamlit app
def main():
    st.title("Digital Carbon Footprint Tracker")

    if "data" not in st.session_state:
        st.session_state.data = {
            "Electricity (kWh)": 0,
            "Transportation (miles)": 0,
            "Waste (tons)": 0
        }
    if "positive_event_idx" not in st.session_state:
        st.session_state.positive_event_idx = 0
    if "negative_event_idx" not in st.session_state:
        st.session_state.negative_event_idx = 0
    if "goal_idx" not in st.session_state:
        st.session_state.goal_idx = 0
    if "challenge_idx" not in st.session_state:
        st.session_state.challenge_idx = 0
    if "player_tokens" not in st.session_state:
        st.session_state.player_tokens = 50
    if "tokens" not in st.session_state:
        st.session_state.tokens = {
            "Energy Savings tokens": 0,
            "Recycling Points": 0,
            "Water Conservation Tokens": 0
        }
    if "badges" not in st.session_state:
        st.session_state.badges = []
    if "goals" not in st.session_state:
        st.session_state.goals = []

    st.sidebar.header("Input Data")
    st.session_state.data["Electricity (kWh)"] = st.sidebar.number_input("Electricity (kWh)", min_value=0, value=st.session_state.data["Electricity (kWh)"])
    st.session_state.data["Transportation (miles)"] = st.sidebar.number_input("Transportation (miles)", min_value=0, value=st.session_state.data["Transportation (miles)"])
    st.session_state.data["Waste (tons)"] = st.sidebar.number_input("Waste (tons)", min_value=0, value=st.session_state.data["Waste (tons)"])

    total_emission = calculate_carbon_footprint(st.session_state.data)
    st.write(f"Total Carbon Footprint: {total_emission} tons of CO2")

    generate_report(st.session_state.data)

    set_goals()
    generate_report(st.session_state.data)
    event_cards()
    goal_cards()
    challenges_and_rewards()
    resource_tokens()
    player_tokens()
    display_badges()

if __name__ == "__main__":
    main()
