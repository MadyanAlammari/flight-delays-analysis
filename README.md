# ✈️ Flight Delays Analysis & Interactive Dashboard

An exploratory data analysis (EDA) project on **5.8M+ U.S. domestic flight records** from 2015. Built an interactive **Streamlit web application** to visualize delay patterns, cancellation rates, and airline performance — plus a **Power BI dashboard** for business-level insights.

---

## 📊 Key Insights

- Identified the airlines with the highest and lowest average arrival delays
- Analyzed the top causes of delays: Late Aircraft, Airline, Air System, Weather, Security
- Visualized daily flight volume trends across the year
- Measured cancellation rates by airline and reason

---

## 📸 Power BI Dashboard

A 4-page interactive Power BI dashboard covering:
- **Overview** — Executive summary with KPIs (14 airlines, 322 airports, 5.82M flights)
- **Delay Analysis** — Delay breakdown by airline, cause, day, and time of day
- **Deep Insights** — Weather delay trends, cancellation reasons, and tail number analysis
- **Route & Airport Performance** — Most used routes, most delayed routes, and geographic map

📄 [View Dashboard PDF](Flight_Delays_Dashboard.pdf)

---

## 🗂️ Dataset

📥 **Download the dataset here:**  
[2015 Flight Delays and Cancellations — Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays)

Place all CSV files in the **root project folder** before running.

| File | Description |
|------|-------------|
| `flights.csv` | 5.8M+ flight records with delay and cancellation info |
| `airlines.csv` | Airline codes and names |
| `airports.csv` | Airport codes and locations |

---

## 🖥️ Streamlit App Features

- **Dataset Overview** — shape, column types, sample rows
- **Missing Values Analysis** — identify and visualize null values
- **Average Delay by Airline** — bar chart comparison across all carriers
- **Daily Flight Count** — time-series of flights per day throughout 2015
- **Delay Cause Breakdown** — horizontal bar chart of avg delay by cause type
- **Cancellation Analysis** — pie chart of cancelled vs non-cancelled flights with percentages

---

## 🚀 How to Run

### Step 1 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Download the dataset
Download from [Kaggle](https://www.kaggle.com/datasets/usdot/flight-delays) and place `flights.csv`, `airlines.csv`, `airports.csv` in the project root.

### Step 3 — Launch the Streamlit app
```bash
streamlit run Flight.py
```

---

## 📦 Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3 |
| Data Processing | Pandas |
| Visualization | Matplotlib, Seaborn |
| Dashboard | Streamlit |
| BI Reporting | Power BI |

---

## 📁 Project Structure

```
flight-delays-analysis/
│
├── Flight.py                       # Streamlit EDA app
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── Flight_Delays_Dashboard.pdf     # Power BI dashboard export
│
└── data/                           # Place Kaggle CSV files here
    ├── flights.csv
    ├── airlines.csv
    └── airports.csv
```

---

## 👤 Author

**Madyan Alammari**  
Computer Science — King Abdulaziz University  
📧 Madyan3172001@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/madyan-alammari-73852a170)  
🐙 [GitHub](https://github.com/MadyanAlammari)
