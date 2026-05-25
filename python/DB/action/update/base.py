
from python.connection.getConnection import get_connection

def update_base(query):
    conn=get_connection()
    cur=conn.cursor()

    cur.execute(query)


    cur.close()
    conn.close()

