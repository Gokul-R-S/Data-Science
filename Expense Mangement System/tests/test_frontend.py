from frontend.utils import fetch_data
from streamlit.testing.v1 import AppTest
from datetime import date


def test_fetch_data_success(mocker):
    """Test fetch_data from utils with 200 response and valid data."""
    # Mock requests.get to simulate a successful response
    mock_response = mocker.patch('requests.get').return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {'key': 'value'}

    data = fetch_data('http://example.com')
    assert data == {'key': 'value'}


def test_fetch_data_empty_response(mocker):
    """Test that fetch_data returns default_empty when API returns an empty response."""
    mock_response = mocker.patch('requests.get').return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {}  # Empty response

    data = fetch_data('http://example.com', default_empty={'default': True})
    assert data == {'default': True}  # Should return default_empty


def test_fetch_data_server_error(mocker):
    """Test that fetch_data handles HTTP errors (500 status)."""
    mock_error = mocker.patch('streamlit.error')
    mock_response = mocker.patch('requests.get').return_value
    mock_response.status_code = 500  # Simulate server error

    data = fetch_data('http://example.com', data_type='test data')

    mock_error.assert_called_with("❌ **Failed to load test data**: Server returned `500`")
    assert data is None  # Should return None on failure


def test_add_update_ui(mocker):
    """Test the add_update UI for date input, form validation, and submission."""
    mocker.patch("utils.fetch_data", return_value=[]) # since server not active it's mocked
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

    # Test form submission with sample data
    app.number_input[0].set_value(100.0)
    app.selectbox[0].set_value("Food")
    app.text_input[0].set_value("Lunch")
    app.button[0].click()  # Click the submit button
    app.run(timeout=10)
    assert not app.exception


def test_analytics_months_ui(mocker):
    """Test analytics_months UI loads without errors using mocked data."""
    mocker.patch("frontend.analytics_months.fetch_data", return_value=[
        {"month_num": 1, "months": "Jan", "total": 100},
        {"month_num": 2, "months": "Feb", "total": 200},
    ])
    app = AppTest.from_file("frontend/analytics_months.py").run(timeout=10)
    assert not app.exception  # Ensures UI loads correctly

