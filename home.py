import streamlit as st
import pandas as pd
from datetime import date

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Personal Expense Tracker", layout="wide")

# --- DATA INITIALIZATION ---
# Using session_state to ensure data persists during the session [cite: 65, 66]
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

# --- SIDEBAR NAVIGATION [cite: 53, 54] ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Add Transaction", "View Transactions", "Summary"])