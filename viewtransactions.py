# --- VIEW TRANSACTIONS PAGE ---
elif page == "View Transactions":

    st.header("📜 Transaction History")

    if st.session_state.transactions:

        df = pd.DataFrame(st.session_state.transactions)

        df = df[
            ["type", "category", "amount", "date", "description"]
        ]

        st.table(df)

    else:
        st.info("No transactions recorded yet.")