# --- SUMMARY PAGE ---
elif page == "Summary":

    st.header("📊 Expense Summary")

    if st.session_state.transactions:

        df = pd.DataFrame(st.session_state.transactions)

        total_income = df[df["type"] == "Income"]["amount"].sum()

        total_expense = df[df["type"] == "Expense"]["amount"].sum()

        balance = total_income - total_expense

        st.success(f"Total Income: ₹ {total_income:.2f}")

        st.error(f"Total Expenses: ₹ {total_expense:.2f}")

        st.info(f"Remaining Balance: ₹ {balance:.2f}")

        expense_df = df[df["type"] == "Expense"]

        if not expense_df.empty:

            category_summary = (
                expense_df.groupby("category")["amount"]
                .sum()
            )

            st.subheader("Category-wise Spending")

            st.bar_chart(category_summary)

    else:
        st.info("No transactions available.")