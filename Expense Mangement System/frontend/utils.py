import os
import sys

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import requests
import streamlit as st
from dotenv import load_dotenv
from backend import logging_setup

load_dotenv()
API_URL = os.getenv("API_URL")

frontend_logger = logging_setup.setup_frontend_logger('utils')

def fetch_data(url, params=None, data_type="data"):
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            try:
                data = response.json()  # data = list[dict]
                if data is None:
                    st.warning("⚠️ Unexpected: Server returned empty data.")
                    frontend_logger.warning(f"Null received for {data_type} from {url}")
                    return None
                return data
            except ValueError as ve:
                st.error("🛑 An unexpected error occurred while processing data. Please try again.") # Malformed JSON response
                raw_text = response.text
                frontend_logger.error(
                    f"Failed to parse server response as JSON for {data_type} from {url}. Raw Response: {raw_text}, Exception: {str(ve)}"
                )
                return None
        else:
            st.error(f"❌ Could not retrieve {data_type}: Server returned `{response.status_code}`."
                     f" Please try again later.") # server side error
            frontend_logger.error(
                f"Failed to load {data_type} from {url}. HTTP Status: {response.status_code}, "
                f"Error Details: {response.json().get('error', 'No additional details provided.')}"
            )
            return None

    except requests.exceptions.RequestException as e:  # client-side error
        st.error("🌐 **Unable to connect to the server**. Please check your connection and try again.")
        frontend_logger.error(f"Request exception while fetching {data_type} from {url}. Exception: {str(e)}")

    except Exception as e:
        st.error("⚠️ An unexpected error occurred. Please try again later.")
        frontend_logger.error(f"Unexpected error while fetching {data_type} from {url}. Exception: {str(e)}")

    return None