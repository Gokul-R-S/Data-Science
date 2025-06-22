from backend import db_helper
import pytest
import mysql.connector


def validate_expense_data(expense):
    assert isinstance(expense, dict)
    assert 'amount' in expense
    assert 'category' in expense
    assert isinstance(expense['amount'], float)
    assert isinstance(expense['category'], str)


def validate_summary_data(summary):
    assert isinstance(summary, list)
    for item in summary:
        assert isinstance(item, dict)
        assert 'category' in item
        assert 'total' in item
        assert isinstance(item['category'], str)
        assert isinstance(item['total'], float)


def test_fetch_expenses_for_date_scenarios():
    # Valid date with known data
    expense_aug15 = db_helper.fetch_expenses_for_date('2024-08-15')
    assert len(expense_aug15) == 2
    validate_expense_data(expense_aug15[0])
    assert expense_aug15[0]['amount'] == 10.0
    assert expense_aug15[0]['category'] == "Shopping"
    assert expense_aug15[0]["notes"] == "Bought potatoes"

    # Multiple expenses scenario
    expenses_sep01 = db_helper.fetch_expenses_for_date('2024-09-01')
    assert len(expenses_sep01) > 1
    for expense in expenses_sep01:
        validate_expense_data(expense)

    # Invalid far-future date
    expense_future = db_helper.fetch_expenses_for_date('2030-08-15')
    assert expense_future == []


def test_fetch_expense_summary_scenarios():
    # Valid range
    summary_month = db_helper.fetch_expense_summary('2024-08-01', '2024-08-31')
    validate_summary_data(summary_month)

    # Single day (matches Sep 4 data)
    summary_day = db_helper.fetch_expense_summary('2024-09-04', '2024-09-04')
    validate_summary_data(summary_day)
    assert len(summary_day) == 3
    assert sum(item['total'] for item in summary_day) == 235

    # Invalid future range
    summary_invalid = db_helper.fetch_expense_summary('2030-05-20', '2030-05-24')
    assert len(summary_invalid) == 0
    assert isinstance(summary_invalid, list)


def test_fetch_expense_months():
    # Fetching monthly expenses
    monthly_expenses = db_helper.fetch_expense_months()
    assert isinstance(monthly_expenses, list)
    assert len(monthly_expenses) > 0 # to chk if data available
    for month in monthly_expenses:
        assert 'month_num' in month
        assert 'months' in month
        assert 'total' in month
        assert isinstance(month['total'], float)
        assert isinstance(month['month_num'], int)
        assert isinstance(month['months'], str)


def test_database_connection_failure(mocker):
    """Test that database connection failures raise the expected errors and
       are not silently suppressed since errors are handled in server.py"""
    mocker.patch('mysql.connector.connect', side_effect=mysql.connector.Error("Connection failed"))

    with pytest.raises(mysql.connector.Error, match="Connection failed"):
        db_helper.fetch_expenses_for_date('2024-08-15')

    with pytest.raises(mysql.connector.Error, match="Connection failed"):
        db_helper.fetch_expense_summary('2024-08-01', '2024-08-31')

    with pytest.raises(mysql.connector.Error, match="Connection failed"):
        db_helper.fetch_expense_months()
