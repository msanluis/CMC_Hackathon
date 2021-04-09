import snowflake.connector as sf
from config import config
import matplotlib.pyplot as plt
import pandas as pd

# Connection String
conn = sf.connect(
    user=config.username,
    password=config.password,
    account=config.account
)

def test_connection(connect, query):
    cursor = connect.cursor()
    cursor.execute(query)
    cursor.close()

'''
try:
    sql = """
    SELECT * FROM "MI_XPRESSCLOUD"."XPRESSFEED"."SPGSCOREVALUE"
    LIMIT 5;
    """
    test_connection(conn, sql)
    cursor = conn.cursor()
    cursor.execute(sql)
    for line in cursor:
        print(line)
except Exception as e:
    print(e)
'''

try:
    sql = """
        SELECT * FROM "MI_XPRESSCLOUD"."XPRESSFEED"."CIQEXCHANGERATE";
        """
    df = pd.read_sql(sql, conn)
    testplot = df.iloc[1:3]
    plt.plot(testplot["PRICEDATE"],testplot["PRICECLOSE"])
    plt.show()

except Exception as e:
    print(e)