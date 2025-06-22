import streamlit as st
from datetime import date
import requests
from utils import fetch_data, API_URL
from backend.logging_setup import setup_frontend_logger

frontend_logger = setup_frontend_logger('add_update')

def add_update_tab():
    selected_date = st.date_input('Enter Date', date(2024, 8, 1),
                                  label_visibility='collapsed', key="expense_date_input")
    selected_date_str = selected_date.strftime('%Y-%m-%d')

    frontend_logger.info(f"Fetching existing expenses for date: {selected_date_str}")
    existing_expenses = fetch_data(
        f'{API_URL}/expenses/{selected_date_str}',
        data_type="expenses"
    )

    if existing_expenses is None:
        return

    categories = ["Select Category", "Rent", "Food", "Shopping", "Entertainment", "Other"]
    category_formatted = {
        "Select Category": "— Select Category —",
        "Rent": "🏠 Rent",
        "Food": "🍽️ Food",
        "Shopping": "🛍️ Shopping",
        "Entertainment": "🎮 Entertainment",
        "Other": "📌 Other"
    }

    # Prepare form data for pre-filling
    form_data = []
    for i in range(5):
        if i < len(existing_expenses):
            amount = existing_expenses[i]['amount']
            category = existing_expenses[i]['category'] if existing_expenses[i]['category'] in categories else "Select Category"
            notes = existing_expenses[i]['notes'] if existing_expenses[i]['notes'] is not None else ""  # NO not null constraint - mysql
        else:
            amount = None
            category = "Select Category"
            notes = ""
        form_data.append({'amount': amount, 'category': category, 'notes': notes})

    with st.form(key='expense_form'):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('**Amount**')
        with col2:
            st.markdown('**Category**')
        with col3:
            st.markdown('**Notes**')

        expenses = []
        for i in range(5):
            with col1:
                amount_input = st.number_input(
                    label='Amount', min_value=0.0, step=1.0,
                    value=form_data[i]['amount'],
                    key=f'amount_{i}_{selected_date_str}',
                    label_visibility='collapsed',
                    placeholder="Enter amount"
                )
            with col2:
                category_input = st.selectbox(
                    label='Category', options=categories,
                    format_func=lambda x: category_formatted[x],
                    index=categories.index(form_data[i]['category']),
                    key=f'category_{i}_{selected_date_str}',
                    label_visibility='collapsed'
                )
            with col3:
                notes_input = st.text_input(
                    label='Notes', value=form_data[i]['notes'],
                    key=f'notes_{i}_{selected_date_str}',
                    label_visibility='collapsed',
                    placeholder="Add notes"
                )

            expenses.append({
                'amount': amount_input,  # float
                'category': category_input,
                'notes': notes_input
            })

        submit_button = st.form_submit_button("💾 Save Expenses")
        if submit_button:
            frontend_logger.info(f"Form submitted with expenses: {expenses}")

            # Filter expenses with valid amount and category
            valid_expenses = [
                exp for exp in expenses if (exp['amount'] or 0) > 0 and exp['category'] != "Select Category"
            ]

            # Checking for partially filled entries (excluding valid ones)
            partially_filled = [
                exp for exp in expenses
                if exp not in valid_expenses and (exp['amount'] or exp['category'] != "Select Category" or exp['notes'].strip())
            ]

            if partially_filled:
                st.warning("⚠️ Some entries are incomplete. Please ensure each expense has an amount, "
                           "a valid category, and optionally notes before submitting.")
                return

            if not existing_expenses and not valid_expenses:
                st.error("🚨 **No valid expenses provided!** Please add at least one valid expense to proceed.")
                return

            # Send the request to the backend
            try:
                response = requests.post(f'{API_URL}/expenses/{selected_date_str}', json=valid_expenses) # valid_expenses list[dict]
                if response.status_code == 200:
                    response_data = response.json()

                    # Display the success message from the backend
                    st.success(f"✅ {response_data.get('message')}")
                    frontend_logger.info(f"Expenses updated successfully for date: {selected_date_str}")

                    # Display any errors (invalid inserts skipped by the backend)
                    errors = response_data.get('errors', [])  # errors -> list none
                    if errors:
                        for error in errors:
                            st.warning(f"⚠️ {error}")
                else:
                    error_message = response.json().get("message", "Unknown error")
                    error_details = response.json().get("errors", "No additional details.")
                    st.error(
                        f'❌ Failed to update expenses: Server returned {response.status_code} - {error_message}. '
                        f'Details: {error_details}'
                    )
                    frontend_logger.error(
                        f"Failed to update expenses for {selected_date_str}: {response.status_code} - {error_message}. "
                        f"Details: {error_details}"
                    )

            except requests.exceptions.RequestException as e:
                st.error(f'❌ Failed to connect to the server: {e}')
                frontend_logger.error(f"Request exception while updating expenses for {selected_date_str}: {str(e)}")

            except Exception as e:
                st.error(f"⚠️ **An unexpected error occurred**.")
                frontend_logger.error(f"Unexpected error while updating expenses for {selected_date_str}: {str(e)}")

if __name__ == "__main__":
    add_update_tab()
