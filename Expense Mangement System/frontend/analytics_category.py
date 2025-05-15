import streamlit as st
from datetime import date
import pandas as pd
from utils import fetch_data, API_URL
from backend.logging_setup import setup_frontend_logger

analytics_logger = setup_frontend_logger('analytics_category')

def analytics_category_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start Date', date(2024, 8, 1))
    with col2:
        end_date = st.date_input('End Date', date(2024, 8, 5))

    if st.button('Get Analytics'):
        if start_date > end_date:
            st.error("❌ **Start Date cannot be after End Date.**")
            return

        params = {
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d')
        }

        analytics_logger.info(f"Fetching analytics for date range: {params['start_date']} to {params['end_date']}.")

        data = fetch_data(
            f'{API_URL}/analytics',
            params=params,
            data_type="analytics data"
        )

        if data is None:
            return

        if not data:
            st.info("ℹ️ **No data available for this date range.**")
            analytics_logger.info(f"No analytics data available for the range: {params['start_date']} to {params['end_date']}.")
            return

        try:
            df_data = {
                'Category': list(data.keys()),
                'Total': [data[category_key]['total'] for category_key in data],
                'Percentage': [data[category_key]['percentage'] for category_key in data]
            }
            df = pd.DataFrame(df_data)

            st.markdown("### **Expense Breakdown By Category**", unsafe_allow_html=True)

            st.bar_chart(data=df.set_index('Category')['Percentage'], use_container_width=True)

            df['Total'] = df['Total'].map('{:.2f}'.format)
            df['Percentage'] = df['Percentage'].map('{:.2f}'.format)
            st.table(df)

            analytics_logger.info("Category analytics successfully rendered on the dashboard.")

        except Exception as e:
            st.error("❌ **Unexpected error while rendering analytics.**")
            analytics_logger.error(
				f"Error rendering analytics data | Start Date: {start_date}, End Date: {end_date} | Exception: {e}"
			)

if __name__ == "__main__":
    analytics_category_tab()