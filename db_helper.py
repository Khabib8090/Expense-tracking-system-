import mysql.connector
from contextlib import contextmanager
from backendd.logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False): # parameter false hai default || agar kisi ne pass karaya to dekho aage
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Loot",
        database="expense_manager"
    )  
    
    cursor = connection.cursor(dictionary=True)
    
    yield cursor
    if commit:
        connection.commit()   # used when insert , delete , update 
    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

         
def fetch_expense_for_date(expense_date):
    logger.info(f"Fetch_expenses_for_date {expense_date}")
    with  get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s",(expense_date,)) # %s Taking as a string 
        expenses = cursor.fetchall()
        return expenses
        # for expense in expenses:
        #     print(expense)

def insert_expenses_data(expense_date,amount,category,notes):
    logger.info(f"Insert_expenses_date are :{expense_date} ,amount :{amount} ,category :{category} ,notes :{notes}")
    with get_db_cursor(commit=True)as cursor:            # YAHA PAR COMMIT PASS KARAYA HAI 
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes))   
        
def delete_expenses_data(expense_date):
    logger.info(f"Delete expenses for date :{expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date=%s",(expense_date,))

def fetch_expenses_sumuary(start_date,end_date):
    logger.info(f"fetch_expenses Sumary for star_date :{start_date} & End date {end_date} ")
    with get_db_cursor()as cursor:        
        cursor.execute("""SELECT category , SUM(amount) as total 
                        FROM expenses where expense_date 
                        BETWEEN %s AND %s
                        GROUP BY category""",(start_date,end_date))  
        
        data =cursor.fetchall()
        return data
    

def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
        return data

if __name__ =="__main__":
    expense=fetch_expense_for_date("2024-08-01")
    print(expense)
    # insert_expenses_data("2024-08-25",49,"Starter","Nugets")
   
    sumary=fetch_expenses_sumuary("2024-08-01","2024-08-25")
    for Data in sumary:
        print(Data)
    print(fetch_monthly_expense_summary())



