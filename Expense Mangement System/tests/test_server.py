from fastapi.testclient import TestClient
from backend.server import app

client = TestClient(app)

def test_add_expense_success(mocker):
    """Test adding expenses successfully."""
    mocker.patch("db_helper.fetch_expenses_for_date", return_value=[])
    mocker.patch("db_helper.insert_expense")
    mocker.patch("db_helper.delete_expenses_for_date")

    expenses = [{"amount": 20.0, "category": "Transport", "notes": "Bus fare"}]
    response = client.post("/expenses/2024-08-15", json=expenses)

    assert response.status_code == 200
    assert response.json()["message"] == "Processed 1 out of 1 expenses successfully"


def test_get_analytics_success(mocker):
    """Test fetching analytics for a given date range."""
    mocker.patch("db_helper.fetch_expense_summary", return_value=[{"category": "Food", "total": 20}])

    response = client.get("/analytics/?start_date=2024-08-01&end_date=2024-08-31")

    assert response.status_code == 200
    assert response.json() == {"Food": {"total": 20, "percentage": 100.0}}


def test_get_months_summary_failure(mocker):
    """Test error handling when fetching monthly summary fails."""
    mocker.patch("db_helper.fetch_expense_months", side_effect=Exception("DB error"))

    response = client.get("/months/")

    assert response.status_code == 500
    assert response.json()["message"] == "Failed to fetch monthly summary"























