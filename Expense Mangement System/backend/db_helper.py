import mysql.connector
from contextlib import contextmanager
import os
from dotenv import load_dotenv
from logging_setup import setup_logger

load_dotenv()

db_config = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME", "expense_manager")
}

logger = setup_logger('db_helper')

@contextmanager
def connect_db(commit=False):
    """Context manager for a MySQL connection and dictionary cursor, with optional commit."""
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True) # o/p list of dict
        yield cursor
        if commit:
            connection.commit()
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def fetch_expenses_for_date(expense_date):
    """Fetch expenses for a specific date."""
    with connect_db() as cursor:
        cursor.execute('select * from expenses where expense_date = %s', (expense_date,))
        result = cursor.fetchall()
        logger.debug(f"Fetched {len(result)} expenses for date: {expense_date}")
        return result

def insert_expense(expense_date, amount, category, notes):
    """Insert a new expense into the db."""
    with connect_db(commit=True) as cursor:
        cursor.execute(
            'insert into expenses (expense_date,amount,category,notes) values (%s,%s,%s,%s)',
            (expense_date, amount, category, notes)
        )
        logger.info(f"Inserted expense | Date: {expense_date}, Amount: {amount}, Category: {category}, Notes: {notes}")

def delete_expenses_for_date(expense_date):
    """Delete expenses for a given date."""
    with connect_db(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date = %s", (expense_date,))
        deleted_count = cursor.rowcount
        logger.info(f"Deleted {deleted_count} expenses for date {expense_date}")
        return deleted_count

def fetch_expense_summary(start_date, end_date):
    """Fetch summarized expenses grouped by category for a date range."""
    with connect_db() as cursor:
        cursor.execute(
            '''select category,sum(amount) as total from expenses where expense_date 
            between %s and %s group by 1 order by 2 desc''', (start_date, end_date)
        )
        result = cursor.fetchall()
        logger.debug(f"Fetched expense summary for {start_date} to {end_date}: {len(result)} categories")
        return result

def fetch_expense_months():
    """Fetches total expenses grouped by month."""
    with connect_db() as cursor:
        cursor.execute(
            '''select month(expense_date) month_num,date_format(expense_date,'%b') months,
               sum(amount) total from expenses group by 1,2 order by 3 desc'''
        )
        result = cursor.fetchall()
        logger.debug(f"Fetched monthly expenses: {len(result)} months")
        return result

if __name__ == "__main__":
    try:
        expense_date = "2024-08-01"
        expenses = fetch_expenses_for_date(expense_date)
        print(f"Expenses on {expense_date}: {expenses}")

        insert_expense("2024-03-21", 50, "Food", "Lunch")

        deleted_count = delete_expenses_for_date("2024-03-21")
        print(f"Deleted {deleted_count} records.")

        summary = fetch_expense_summary("2024-08-01", "2024-08-03")
        for record in summary:
            print(record)

        monthly_expenses = fetch_expense_months()
        print("Monthly Expense Breakdown:", monthly_expenses)

    except Exception as e:
        print(f"Unexpected error occurred: {e}.")