import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger=setup_logger('db_helper')

@contextmanager
def connect_db(commit=False):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Raj@1234",
        database="expense_manager" )

    cursor=connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with connect_db() as cursor:
        cursor.execute('select * from expenses where expense_date = %s',(expense_date,))
        expenses=cursor.fetchall()
        return expenses

def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert_expense called with date:{expense_date}, amount:{amount}, category:{category}, notes:{notes}")
    with connect_db(commit=True) as cursor:
        cursor.execute('insert into expenses (expense_date,amount,category,notes) values (%s,%s,%s,%s)',
                       (expense_date,amount,category,notes) )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with connect_db(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date = %s", (expense_date,))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch_expense_summary called with start_date:{start_date},end_date:{end_date} ")
    with connect_db() as cursor:
        cursor.execute('''select category,sum(amount) as total from expenses where expense_date 
        between %s and %s group by 1 order by 2 desc''',(start_date,end_date))
        expenses=cursor.fetchall()
        return expenses

def fetch_expense_months():
    logger.info('fetch_expense_months called')
    with connect_db() as cursor:
        cursor.execute('''select month(expense_date) month_num,date_format(expense_date,'%b') months,
        sum(amount) total from expenses group by 1,2 order by 3 desc''')
        expenses=cursor.fetchall()
        return expenses

if __name__=='__main__':
    # exp=fetch_expenses_for_date('2024-09-30')
    # print(exp)
    # #insert_expense('2025-2-4',5000,'food','whey protein')
    # #delete_expenses_for_date('2025-2-4')
    # data=fetch_expense_summary('2024-08-01' , '2024-08-05')
    # for row in data:
    #     print(row)
    exp=fetch_expense_months()
    #print(exp)
