# streamlit dashboard
#importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load dataset
final_df = pd.read_csv('f1_simple_predictions.csv')

# ---------------------------
# Page setup
st.set_page_config(page_title="F1 Race Predictor", layout="wide")
st.title("🏎️ F1 Race Winner Predictor")
st.markdown("""
Select a track to see predicted driver finishes, fastest laps, qualifying positions, 
and win probabilities. You can also filter by constructor if desired.
""")

# ---------------------------
# Filter for most completed year of  drivers
current_year = 2024
current_df = final_df[final_df['year'] == current_year]

# ---------------------------
# Track selection dropdown
tracks = current_df['name_circuits'].unique()
selected_track = st.selectbox("Select Track", tracks)

# Filter for selected track
track_data = current_df[current_df['name_circuits'] == selected_track]

# ---------------------------
# constructor filter, if wanted
constructors = track_data['constructor_name'].unique()
selected_constructor = st.multiselect("Filter by Constructor (optional)", constructors)

if selected_constructor:
    track_data = track_data[track_data['constructor_name'].isin(selected_constructor)]

# ---------------------------
# Sort by win probability and get top 3
track_data = track_data.sort_values(by='win_probability', ascending=False)
top3 = track_data.head(3)

# ---------------------------
# Display top 3 drivers in columns
st.subheader(f"Top 3 Predicted Drivers at {selected_track}")

cols = st.columns(3)
for idx, (i, row) in enumerate(top3.iterrows()):
    driver_name = f"{row['forename']} {row['surname']}"
    constructor = row['constructor_name']
    qual = row['position_qualifying']
    fastest_lap = row['fastestLapTimeFormatted']
    win_prob = row['win_probability']

    cols[idx].markdown(f"### {'🏆 ' if idx==0 else ''}{driver_name}")
    cols[idx].markdown(f"**Constructor:** {constructor}")
    cols[idx].markdown(f"**Qualifying Position:** {qual}")
    cols[idx].markdown(f"**Fastest Lap:** {fastest_lap}")
    cols[idx].markdown(f"**Win Probability:** {win_prob:.2f}")

# ---------------------------
# Win probability bar chart
st.subheader("Win Probability Comparison")
plt.figure(figsize=(8, 3))
plt.barh(
    top3['forename'] + " " + top3['surname'],
    top3['win_probability'],
    color=['gold', 'silver', 'peru']
)
plt.xlabel("Win Probability")
plt.xlim(0, 1)
plt.gca().invert_yaxis()
st.pyplot(plt)

# ---------------------------
# Scatter plot: Fastest lap vs Qualifying
st.subheader("Qualifying vs Fastest Lap")
plt.figure(figsize=(8,5))

# Check if fastestLap is numeric
if pd.api.types.is_numeric_dtype(track_data['fastestLapTimeNumeric']):
    # Scatter plot colored by constructor
    constructors = track_data['constructor_name'].unique()
    colors = plt.cm.tab20.colors  # color palette

    for i, constructor in enumerate(constructors):
        subset = track_data[track_data['constructor_name'] == constructor]
        plt.scatter(
            subset['position_qualifying'],
            subset['fastestLapTimeNumeric'],
            s=100,
            color=colors[i % len(colors)],
            label=constructor,
            edgecolor='black'
        )
        # Add driver names as labels
        for _, row in subset.iterrows():
            plt.text(
                row['position_qualifying'] + 0.1, 
                row['fastestLapTimeNumeric'] + 0.01, 
                row['surname'],
                fontsize=8
            )

    plt.xlabel("Qualifying Position")
    plt.ylabel("Fastest Lap Time(in seconds)")
    plt.title(f"Qualifying vs Fastest Lap at {selected_track}")
    plt.gca().invert_xaxis()  # Lower qualifying numbers (front) on left
    plt.legend()
    st.pyplot(plt)
else:
    st.markdown("Fastest lap data is not numeric; scatter plot unavailable.")

# ---------------------------
# Feature Importance
st.subheader("Feature Importance")
# Example values; replace with actual model.feature_importances_ if desired
feature_importances = pd.Series([0.4, 0.6], index=['grid', 'position_qualifying']).sort_values()
plt.figure(figsize=(5,3))
feature_importances.plot(kind='barh', color='orange')
plt.xlabel("Importance")
plt.ylabel("Feature")
st.pyplot(plt)

# ---------------------------
# Footer
st.markdown("---")
st.markdown("⚡ Built with Streamlit | Data from Rohan Rao's Kaggle F1 World Championship Dataset")
