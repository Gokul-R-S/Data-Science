from fastapi import FastAPI
from datetime import date
import db_helper
from typing import List,Dict
from pydantic import BaseModel
from logging_setup import setup_logger
from fastapi.responses import JSONResponse

app = FastAPI()

logger = setup_logger('api_server')

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class Months(BaseModel):
    month_num: int
    months: str
    total: float

class CategoryAnalytics(BaseModel):
    total: float
    percentage: float


@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    """Fetches expenses for a given date from the database."""
    logger.info(f"Fetching expenses for date: {expense_date}")
    try:
        expenses = db_helper.fetch_expenses_for_date(expense_date)
        return expenses
    except Exception as e:
        logger.error(f"Failed to fetch expenses for {expense_date}: {e}")
        return JSONResponse(content={"message": "Failed to fetch expenses", "error": str(e)}, status_code=500)


@app.post('/expenses/{expense_date}')
def add_or_update_expense(expense_date: date, expenses: List[Expense]):
    """Adds or updates expenses for a given date. If no expenses are provided and existing ones exist, they are deleted."""
    logger.info(f"Adding/Updating expenses for date: {expense_date}, Count: {len(expenses)}")

    existing_expenses = db_helper.fetch_expenses_for_date(expense_date)

    # If an empty list is received as payload but expenses exist in db, performs deletion
    if not expenses and existing_expenses:
        logger.info(f"No expenses provided for date {expense_date}, deleting existing expenses")
        try:
            db_helper.delete_expenses_for_date(expense_date)
            return {"message": f"Expenses cleared successfully for date {expense_date}"}
        except Exception as e:
            logger.error(f"Failed to delete expenses for date {expense_date}: {e}")
            return JSONResponse(content={"message": "Failed to clear expenses", "errors": str(e)}, status_code=500)

    # Proceeded with delete and insert if there is data in expenses
    try:
        db_helper.delete_expenses_for_date(expense_date)
    except Exception as e:
        logger.error(f"Failed to delete expenses for date {expense_date}: {e}")
        return JSONResponse(content={"message": "Failed to process expenses", "errors": str(e)}, status_code=500)

    errors = []
    success_count = 0
    for exp in expenses:
        try:
            db_helper.insert_expense(expense_date, exp.amount, exp.category, exp.notes)
            success_count += 1
        except Exception as e:
            logger.error(f"Failed to insert expense for date {expense_date}: {e}")
            errors.append(f"Insert failed for amount {exp.amount}: {e}") # errors list

    logger.debug(f"Successfully processed {success_count} expenses for date: {expense_date}")

    # Response fetched in the frontend
    response = {
        "message": f"Processed {success_count} out of {len(expenses)} expenses successfully",
        "errors": errors if errors else None }
    return response


@app.get("/analytics/", response_model=Dict[str, CategoryAnalytics])
def get_analytics(start_date: date, end_date: date):
    """Fetches expense analytics for a given date range, calculating total expenses and category-wise breakdown."""
    logger.info(f"Fetching analytics for date range: {start_date} to {end_date}")
    try:
        data = db_helper.fetch_expense_summary(start_date, end_date)  # data = list[dict]

        total = sum(row["total"] for row in data)
        breakdown = {}
        for row in data:
            percentage = (row['total'] / total) * 100 if total else 0
            breakdown[row['category']] = {'total': row['total'], 'percentage': round(percentage, 2)}

        logger.debug(f"Analytics breakdown: {breakdown}")
        return breakdown
    except Exception as e:
        logger.error(f"Failed to fetch analytics: {e}")
        return JSONResponse(content={"message": "Failed to fetch data in the given date range", "error": str(e)}, status_code=500)


@app.get("/months/", response_model=List[Months])
def get_months_summary():
    """Fetches a summary of monthly expenses, returning total expenses grouped by month."""
    logger.info("Fetching monthly expense summary")
    try:
        data = db_helper.fetch_expense_months()  # data = list[dict]
        logger.debug(f"Monthly summary: {data}")
        return data
    except Exception as e:
        logger.error(f"Failed to fetch monthly summary: {e}")
        return JSONResponse(content={"message": "Failed to fetch monthly summary", "error": str(e)}, status_code=500)

