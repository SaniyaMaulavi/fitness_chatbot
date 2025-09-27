import streamlit as st
import random

# -----------------------------
# Diet & Exercise Tips
# -----------------------------
diet_tips = [
    {"Keyword": "breakfast", "Tip": "Oats with milk and fruits"},
    {"Keyword": "lunch", "Tip": "Grilled chicken with salad"},
    {"Keyword": "dinner", "Tip": "Soup and steamed vegetables"},
    {"Keyword": "snack", "Tip": "Nuts and fruits"},
]

exercise_tips = [
    {"Keyword": "cardio", "Exercise": "Jogging for 30 minutes"},
    {"Keyword": "strength", "Exercise": "Push-ups 3 sets of 15 reps"},
    {"Keyword": "flexibility", "Exercise": "Yoga for 20 minutes"},
]

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Diet & Fitness Chatbot", page_icon="🍎", layout="wide")
st.markdown("<h1 style='text-align: center; color: darkgreen;'>🍎 Diet & Fitness Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Ask anything about your diet or exercise!</h4>", unsafe_allow_html=True)
st.write("---")

# User Input
user_input = st.text_input("Type your question here:")
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input("Your Age:", min_value=5, max_value=120, value=25)
with col2:
    weight = st.number_input("Your Weight (kg):", min_value=10, max_value=200, value=60)
with col3:
    goal = st.selectbox("Your Goal:", ["Maintain Weight", "Lose Weight", "Gain Muscle", "Stay Fit"])

# Personalized Notes
goal_notes = {
    "Lose Weight": "Try to keep portions small and focus on high-protein, low-calorie foods.",
    "Gain Muscle": "Include protein-rich meals and strength exercises.",
    "Maintain Weight": "Balanced diet and regular exercise will help maintain your weight.",
    "Stay Fit": "Stay active daily and eat a variety of healthy foods."
}

# Suggestion Logic
if st.button("Get Suggestions"):
    if user_input.strip() == "":
        st.warning("⚠️ Please type your question first!")
    else:
        user_input_lower = user_input.lower()

        diet_matches = [d['Tip'] for d in diet_tips if d['Keyword'].lower() in user_input_lower]
        exercise_matches = [e['Exercise'] for e in exercise_tips if e['Keyword'].lower() in user_input_lower]

        if diet_matches:
            st.markdown("<h3 style='color: darkblue;'>🍽️ Diet Suggestions</h3>", unsafe_allow_html=True)
            for tip in diet_matches:
                st.info(f"{tip}\nGoal Tip: {goal_notes[goal]}")

        if exercise_matches:
            st.markdown("<h3 style='color: darkred;'>🏋️ Exercise Suggestions</h3>", unsafe_allow_html=True)
            for ex in exercise_matches:
                st.success(f"{ex}\nGoal Tip: {goal_notes[goal]}")

        if not diet_matches and not exercise_matches:
            st.warning("⚠️ No exact match found. Here are some general tips:")
            st.write("- **Diet:** Eat a balanced mix of proteins, carbs, and vegetables.")
            st.write("- **Exercise:** Include at least 30 minutes of walking or light cardio daily.")
