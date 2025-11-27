import streamlit as st
import pandas as pd
st.set_page_config(page_title="Khata Book Dashboard", page_icon="📒", layout="wide")
if 'khata' not in st.session_state:
    st.session_state['khata'] = {}
def calculate_balance(transactions):
    """Calculates balance from a list of transactions."""
    total_gave = sum(amount for t, amount in transactions if t == "gave")
    total_got = sum(amount for t, amount in transactions if t == "got")
    return total_gave, total_got, total_gave - total_got
st.sidebar.title("📒 Desi Khata Book")
menu = st.sidebar.radio(
    "Menu", 
    ["Dashboard", "Add Customer", "New Transaction", "View Ledger", "Reset Data"]
)
if menu == "Dashboard":
    st.title("📊 Financial Overview")
    
    if not st.session_state['khata']:
        st.info("No customers found. Go to 'Add Customer' to start.")
    else:
        # Calculate Aggregates
        grand_total_gave = 0
        grand_total_got = 0
        summary_data = []
         for name, transactions in st.session_state['khata'].items():
            given, got, balance = calculate_balance(transactions)
            grand_total_gave += given
            grand_total_got += got
            if balance > 0:
                status = f"You will get ₹{balance}"
            elif balance < 0:
                status = f"You have to pay ₹{abs(balance)}"
            else:
                status = "Settled 😮‍💨"
             summary_data.append({
                "Customer": name,
                "Total Given (Udhaar)": given,
                "Total Received (Jama)": got,
                "Net Balance": balance,
                "Status": status
            })
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Given (Market)", f"₹{grand_total_gave}")
        col2.metric("Total Received", f"₹{grand_total_got}")
        net_market = grand_total_gave - grand_total_got
        col3.metric("Net Market Balance", f"₹{net_market}", delta_color="normal")

        st.markdown("---")
        st.subheader("Customer Balances")
        df_summary = pd.DataFrame(summary_data)
        st.dataframe(df_summary, use_container_width=True)
elif menu == "Add Customer":
    st.title("👤 Add New Customer")
    
    with st.form("add_customer_form"):
        new_name = st.text_input("Customer Name").strip()
        submitted = st.form_submit_button("Add Customer")
        
        if submitted:
            if new_name:
                if new_name in st.session_state['khata']:
                    st.error("Customer already exists!")
                else:
                    st.session_state['khata'][new_name] = []
                    st.success(f"{new_name} added successfully!")
            else:
                st.warning("Please enter a valid name.")
elif menu == "New Transaction":
    st.title("💸 Record Transaction")
    
    if not st.session_state['khata']:
        st.warning("No customers available. Please add a customer first.")
    else:
        customer_list = list(st.session_state['khata'].keys())
        
        with st.container():
            col1, col2 = st.columns(2)
            
            with col1:
                selected_customer = st.selectbox("Select Customer", customer_list)
            
            with col2:
                trans_type = st.radio("Transaction Type", ["Give Money (Udhaar)", "Got Money (Jama)"])
            
            amount = st.number_input("Enter Amount", min_value=1, step=10)
            
            if st.button("Save Transaction"):
                type_key = "gave" if "Give" in trans_type else "got"
                st.session_state['khata'][selected_customer].append((type_key, amount))
                st.success("Transaction recorded successfully! ✅")
elif menu == "View Ledger":
    st.title("📖 Detailed Khata")
    
    if not st.session_state['khata']:
        st.info("Khata is empty.")
    else:
        customer_list = list(st.session_state['khata'].keys())
        selected_view = st.selectbox("Filter by Customer", ["All"] + customer_list)
        
        all_records = []
        for name, transactions in st.session_state['khata'].items():
            if selected_view == "All" or selected_view == name:
                for t_type, amount in transactions:
                    all_records.append({
                        "Customer": name,
                        "Type": "Given (Udhaar)" if t_type == "gave" else "Received (Jama)",
                        "Amount": amount,
                        "Flow": "Out ->" if t_type == "gave" else "In <-"
                    })
        
        if all_records:
            df = pd.DataFrame(all_records)
            
            # Styling: Color code the rows
            def color_transaction(val):
                color = '#ffcccb' if val == "Given (Udhaar)" else '#90ee90'
                return f'background-color: {color}'

            st.dataframe(df, use_container_width=True)
        else:
            st.info("No transactions found for this selection.")

# --- PAGE: RESET ---
elif menu == "Reset Data":
    st.title("⚠️ Reset Khata")
    st.write("This will delete all customers and transactions.")
    
    if st.button("Delete Everything", type="primary"):
        st.session_state['khata'] = {}
        st.success("Khata has been cleared.")
        st.rerun()




