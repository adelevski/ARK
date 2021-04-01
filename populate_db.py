import config
import alpaca_trade_api as tradeapi
import psycopg2

connection = psycopg2.connect(host=config.DB_HOST, database=config.DB_NAME, user=config.DB_USER, password=config.DB_PASS)

cursor = connection.cursor()

cursor.execute("SELECT * FROM stock")

print(cursor.fetchall())

