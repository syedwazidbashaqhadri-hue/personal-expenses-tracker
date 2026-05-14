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
# --- HOME PAGE ---
if page == "Home":
    st.title("💰 Personal Expense Tracker") # This adds the title you were missing!
    st.markdown("""
    ### Welcome to your financial companion!
    This application helps you **record income and expenses**, track your history, and understand your spending habits with ease.
    """)
# --- ADD TRANSACTION PAGE ---
if page == "Add Transaction":

    st.header("➕ Add New Transaction")

    tab1, tab2 = st.tabs(["Income", "Expense"])

    # ---------- INCOME TAB ----------
    with tab1:

        st.subheader("Add Income Details")

        inc_source = st.text_input(
            "Income Source (e.g., Salary, Freelance)"
        )

        inc_amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=100.0,
            key="inc_amt"
        )

        inc_date = st.date_input(
            "Date",
            date.today(),
            key="inc_date"
        )

        inc_desc = st.text_area(
            "Description",
            key="inc_desc"
        )

        if st.button("Save Income"):

            if inc_source and inc_amount > 0:

                new_income = {
                    "type": "Income",
                    "category": inc_source,
                    "amount": inc_amount,
                    "date": str(inc_date),
                    "description": inc_desc
                }

                st.session_state.transactions.append(new_income)

                st.success(f"Income from {inc_source} added!")

            else:
                st.warning("Please provide a source and amount.")

    # ---------- EXPENSE TAB ----------
    with tab2:

        st.subheader("Add Expense Details")

        exp_cat = st.selectbox(
            "Category",
            ["Food", "Travel", "Shopping",
             "Bills", "Education", "Medical", "Others"]
        )

        exp_amount = st.number_input(
            "Amount",
            min_value=0.0,
            step=10.0,
            key="exp_amt"
        )

        exp_date = st.date_input(
            "Date",
            date.today(),
            key="exp_date"
        )

        exp_desc = st.text_area(
            "Description",
            key="exp_desc"
        )

        if st.button("Save Expense"):

            if exp_amount > 0:

                new_expense = {
                    "type": "Expense",
                    "category": exp_cat,
                    "amount": exp_amount,
                    "date": str(exp_date),
                    "description": exp_desc
                }

                st.session_state.transactions.append(new_expense)

                st.success(f"Expense for {exp_cat} added!")

            else:
                st.warning("Please enter a valid amount.")

    # ---------- TRANSACTION ANALYSIS ----------
    st.markdown("---")
    st.subheader("📊 Financial Overview")

    if st.session_state.transactions:

        df = pd.DataFrame(st.session_state.transactions)

        # View all transactions
        st.write("### 📜 All Transactions")
        st.dataframe(df)

        # Calculate totals
        total_income = df[df["type"] == "Income"]["amount"].sum()
        total_expense = df[df["type"] == "Expense"]["amount"].sum()

        # Remaining balance
        balance = total_income - total_expense

        # Display summary
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("💵 Total Income", f"₹ {total_income:.2f}")

        with col2:
            st.metric("💸 Total Expenses", f"₹ {total_expense:.2f}")

        with col3:
            st.metric("🏦 Remaining Balance", f"₹ {balance:.2f}")

        # Category-wise spending
        st.write("### 📂 Category-wise Spending")

        expense_df = df[df["type"] == "Expense"]

        if not expense_df.empty:

            category_summary = (
                expense_df.groupby("category")["amount"]
                .sum()
                .reset_index()
            )

            st.table(category_summary)

            # Optional chart
            st.bar_chart(
                category_summary.set_index("category")
            )

        else:
            st.info("No expense data available.")

    else:
        st.info("No transactions recorded yet.")