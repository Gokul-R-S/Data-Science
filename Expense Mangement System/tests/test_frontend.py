from frontend.utils import fetch_data
from streamlit.testing.v1 import AppTest
from datetime import date


def test_fetch_data_server_error(mocker):
    """Test that fetch_data handles HTTP errors (500 status)."""
    mock_error = mocker.patch('streamlit.error')
    mock_response = mocker.patch('requests.get').return_value
    mock_response.status_code = 500  # Simulate server error

    data = fetch_data('http://example.com', data_type='test data')

    mock_error.assert_called_with("❌ Could not retrieve test data: Server returned `500`. Please try again later.")
    assert data is None  # Should return None on failure


def test_analytics_months_ui(mocker):
    """Test analytics_months UI loads without errors using mocked data."""
    mock_response = mocker.patch('utils.requests.get').return_value
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"month_num": 1, "months": "Jan", "total": 100},
        {"month_num": 2, "months": "Feb", "total": 200},
    ]

    # patch st.error to assert no error messages are triggered
    mock_st_error = mocker.patch("streamlit.error")

    app = AppTest.from_file("frontend/analytics_months.py").run(timeout=10)

    # Verify the app ran without crashing
    assert not app.exception

    # Confirm that no error messages were shown in the UI
    mock_st_error.assert_not_called()


def test_add_update_ui(mocker):
    """Test successful submission of the add/update expense form with valid inputs and a mocked backend."""
    # Mock fetch_data to return no expenses initially
    mocker.patch("utils.fetch_data", return_value=[])

    # Mock requests.post to simulate a successful response
    mock_response = mocker.patch("requests.post").return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "message": "Processed 1 out of 1 expenses successfully",
        "errors": None
    }

    mock_success = mocker.patch('streamlit.success')
    mock_st_error = mocker.patch("streamlit.error")

    # Run the app
    app = AppTest.from_file("frontend/add_update.py").run(timeout=5)

    selected_date = date(2024, 8, 1)
    app.date_input[0].set_value(selected_date)
    assert app.date_input[0].value[0] == selected_date

    amount_inputs = app.number_input
    assert len(amount_inputs) == 5

    category_inputs = app.selectbox
    assert len(category_inputs) == 5

    notes_inputs = app.text_input
    assert len(notes_inputs) == 5

    # Fill one valid expense row
    app.number_input[0].set_value(100.0)
    app.selectbox[0].set_value("Food")
    app.text_input[0].set_value("Lunch")

    # Submit the form
    app.button[0].click()
    app.run(timeout=10)

    # Verify the app ran without crashing
    assert not app.exception
    # Confirm that no error messages were shown in the UI
    mock_st_error.assert_not_called()

    # Verify that the expected success message was displayed in UI
    mock_success.assert_called_with("✅ Processed 1 out of 1 expenses successfully")



