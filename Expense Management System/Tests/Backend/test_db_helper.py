from Backend import db_helper

def test_fetch_expenses_for_date_aug15():
    expense=db_helper.fetch_expenses_for_date('2024-08-15')

    assert len(expense)==1
    assert expense[0]['amount']==10.0
    assert expense[0]['category'] == "Shopping"
    assert expense[0]["notes"] == "Bought potatoes"

def test_fetch_expenses_for_date_invalid_date():
    expense = db_helper.fetch_expenses_for_date('9999-08-15')

    assert len(expense) == 0

def test_fetch_expense_summary_invalid_range():
    summary=db_helper.fetch_expense_summary('2099-5-20','2099-5-24')
    assert len(summary) ==0



