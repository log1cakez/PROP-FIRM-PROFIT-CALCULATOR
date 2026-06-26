import streamlit as st
import requests

# -----------------------------
# Configuration
# -----------------------------
st.set_page_config(
    page_title="MIDAS Prop Firm Profit Calculator",
    page_icon="💰",
    layout="centered"
)

PROFIT_SPLIT = 0.80

# -----------------------------
# Exchange Rate
# -----------------------------
@st.cache_data(ttl=3600)
def get_usd_php():
    try:
        response = requests.get(
            "https://open.er-api.com/v6/latest/USD",
            timeout=5
        )

        data = response.json()

        if data["result"] == "success":
            return data["rates"]["PHP"]

    except:
        pass

    return 60.0


usd_php = get_usd_php()

# -----------------------------
# Title
# -----------------------------
st.title("MIDAS Prop Firm Profit Calculator")
st.caption("Automatically uses the latest USD → PHP exchange rate.")

# -----------------------------
# Inputs
# -----------------------------
accounts = {
    "$5,000": 5000,
    "$10,000": 10000,
    "$25,000": 25000,
    "$50,000": 50000,
    "$100,000": 100000,
    "$200,000": 200000
}

account_name = st.selectbox(
    "Funded Account",
    list(accounts.keys())
)

account = accounts[account_name]

risk_reward = st.number_input(
    "Risk Reward (R)",
    min_value=0.0,
    value=60.0,
    step=1.0
)

risk = st.number_input(
    "Risk Per Trade (%)",
    min_value=0.0,
    value=0.5,
    step=0.1
)

profit_split = st.slider(
    "Profit Split",
    50,
    100,
    80
) / 100

# -----------------------------
# Calculation
# -----------------------------
profit_percent = risk_reward * risk
gross_profit = account * (profit_percent / 100)
take_home = gross_profit * profit_split
php = take_home * usd_php

# -----------------------------
# Results
# -----------------------------
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Profit %", f"{profit_percent:.2f}%")
    st.metric("Gross Profit", f"${gross_profit:,.2f}")

with col2:
    st.metric("After Profit Split", f"${take_home:,.2f}")
    st.metric("PHP Value", f"₱{php:,.2f}")

st.divider()

st.subheader("Calculation")

st.code(
f"""
{risk_reward}R × {risk}% Risk = {profit_percent:.2f}%

{profit_percent:.2f}% × ${account:,.0f}
= ${gross_profit:,.2f}

${gross_profit:,.2f} × {profit_split*100:.0f}% Profit Split
= ${take_home:,.2f}

${take_home:,.2f} × {usd_php:.2f}
= ₱{php:,.2f}
"""
)

st.info(f"Current USD/PHP Rate: {usd_php:.4f}")