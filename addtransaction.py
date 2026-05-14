elif page == "Add Transaction":
    st.header("➕ Add New Transaction")
    
    tab1, tab2 = st.tabs(["Income", "Expense"])
    
    with tab1:
        st.subheader("Add Income Details") [cite: 17]
        inc_source = st.text_input("Income Source (e.g., Salary, Freelance)") [cite: 18]
        inc_amount = st.number_input("Amount", min_value=0.0, step=100.0, key="inc_amt") [cite: 19]
        inc_date = st.date_input("Date", date.today(), key="inc_date") [cite: 20]
        inc_desc = st.text_area("Description", key="inc_desc") [cite: 21]
        
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

    with tab2:
        st.subheader("Add Expense Details") [cite: 25]
        # Categories defined in documentation [cite: 31]
        exp_cat = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Education", "Medical", "Others"]) [cite: 26]
        exp_amount = st.number_input("Amount", min_value=0.0, step=10.0, key="exp_amt") [cite: 27]
        exp_date = st.date_input("Date", date.today(), key="exp_date") [cite: 28]
        exp_desc = st.text_area("Description", key="exp_desc") [cite: 29]
        
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