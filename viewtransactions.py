elif page == "View Transactions":
    st.header("📜 Transaction History")
    
    if st.session_state.transactions:
        df = pd.DataFrame(st.session_state.transactions)
        # Reordering columns for better display [cite: 36]
        df = df[["type", "category", "amount", "date", "description"]]
        st.table(df) [cite: 35]
    else:
        st.info("No transactions recorded yet.")