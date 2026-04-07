import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("✈️ Flight Dataset - Exploratory Data Analysis")
df = pd.read_csv("flights.csv")


# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("flights.csv")
    df['DATE'] = pd.to_datetime(df[['YEAR', 'MONTH', 'DAY']], errors='coerce')
    return df

df = load_data()
st.success("Data loaded successfully!")

# --- Show basic info ---
st.subheader("📊 Dataset Overview")
st.write(df.head())

st.markdown("**Shape:**")
st.write(df.shape)

st.markdown("**Column Data Types:**")
st.write(df.dtypes)

# --- Missing Values ---
st.subheader("❗ Missing Values")
missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)
st.write(missing)


# --- Average Delay by Airline ---
st.subheader("🛫 Average Arrival Delay by Airline")
airline_delay = df.groupby('AIRLINE')['ARRIVAL_DELAY'].mean().sort_values()
fig2, ax2 = plt.subplots(figsize=(10,5))
airline_delay.plot(kind='bar', ax=ax2)
ax2.set_ylabel("Avg Arrival Delay (minutes)")
st.pyplot(fig2)

# --- Daily Flight Count ---
st.subheader("📅 Flights per Day")
flights_per_day = df.groupby('DATE').size()
fig3, ax3 = plt.subplots(figsize=(12, 4))
flights_per_day.plot(ax=ax3)
ax3.set_title("Number of Flights per Day")
ax3.set_ylabel("Number of Flights")
st.pyplot(fig3)

# --- Delay Causes ---
st.subheader("🔍 Delay Cause Analysis")
delay_cols = ['AIR_SYSTEM_DELAY', 'SECURITY_DELAY', 'AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY', 'WEATHER_DELAY']
avg_delays = df[delay_cols].mean().sort_values()
fig4, ax4 = plt.subplots()
avg_delays.plot(kind='barh', ax=ax4)
ax4.set_title("Average Delay Time by Cause (minutes)")
st.pyplot(fig4)


# --- Flight Cancellation Breakdown ---
st.subheader("🚫 Cancellation Analysis")
counts = df['CANCELLED'].value_counts()
labels = ['Not Cancelled', 'Cancelled']
percents = counts / counts.sum() * 100

# Show text
for l, p in zip(labels, percents): st.write(f"**{l}**: {p:.2f}%")

# Show pie chart
fig6, ax6 = plt.subplots()
ax6.pie(counts, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#66b3ff', '#ff6666'])
ax6.axis('equal')
st.pyplot(fig6)

