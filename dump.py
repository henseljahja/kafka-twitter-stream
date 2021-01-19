import mysql.connector as mysql
import pandas as pd

db = mysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = "<your topic_name>"
)

cursor = db.cursor()

#query select dan insert
select = "select ids ,tweet ,date from steam"

#mengambil text
dataBase = cursor.execute(select)
records = cursor.fetchall()
dfData = pd.DataFrame(records)

dfData.to_csv("<your file name>.csv", header=["User_ID", "Steam", "Timestamp"], index=False)