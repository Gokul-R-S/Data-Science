import streamlit as st
from datetime import date
import pandas as pd
from utils import fetch_data, API_URL

def analytics_category_tab():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input('Start Date', date(2024, 8, 1))
    with col2:
        end_date = st.date_input('End Date', date(2024, 8, 5))

    if start_date > end_date:
        st.error("❌ **Start Date cannot be after End Date.**")
        return

    if st.button('Get Analytics'):
        params = {
            "start_date": start_date.strftime('%Y-%m-%d'),
            "end_date": end_date.strftime('%Y-%m-%d')
        }

        data = fetch_data(
            f'{API_URL}/analytics',
            params=params,
            data_type="analytics data",
            default_empty={}
        )

        if data is None:
            return

        if not data:
            st.info("ℹ️ **No data available for this date range.**")
            return

        try:
            df_data = {
                'Category': list(data.keys()),
                'Total': [data[category_key]['total'] for category_key in data],
                'Percentage': [data[category_key]['percentage'] for category_key in data]
            }
            df = pd.DataFrame(df_data)

            st.markdown("### **Expense Breakdown By Category**",unsafe_allow_html=True)

            st.bar_chart(data=df.set_index('Category')['Percentage'], use_container_width=True)

            df['Total'] = df['Total'].map('{:.2f}'.format)
            df['Percentage'] = df['Percentage'].map('{:.2f}'.format)
            st.table(df)

        except (KeyError, TypeError) as e:
            st.error("❌ **Error processing analytics data:** Invalid format or missing keys.")
            st.markdown(f"```{str(e)}```", unsafe_allow_html=True)

        except Exception as e:
            st.error("❌ **Unexpected error while rendering analytics.**")
            st.markdown(f"```{str(e)}```", unsafe_allow_html=True)