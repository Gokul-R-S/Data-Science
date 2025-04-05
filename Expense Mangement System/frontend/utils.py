import requests
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
API_URL = os.getenv("API_URL")

def fetch_data(url, params=None, data_type="data", default_empty={}):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json() # data = list[dict]
            return data if data else default_empty
        else:
            st.error(f"❌ **Failed to load {data_type}**: Server returned `{response.status_code}`") # server side error
            st.markdown(
                f"🔍 **Error Details:**\n"
                f"```{response.json().get('error', 'No additional details provided.')}```",
                unsafe_allow_html=True
            )
            return None

    except requests.exceptions.RequestException as e:
        st.error("🌐 **Unable to connect to the server**. Please check your internet or try again later.")
        st.markdown(
            f"🔍 **Details:**\n"
            f"```{str(e)}```",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"⚠️ **Unexpected error while loading {data_type}**.")
        st.markdown(
            f"🔍 **Details:**\n"
            f"```{str(e)}```",
            unsafe_allow_html=True
        )

    return None
