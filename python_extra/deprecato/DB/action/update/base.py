
from python.connection.getConnection import get_connection

def update_base(query):
    conn=get_connection()
    cur=conn.cursor()

    cur.execute(query)

    conn.commit()

    cur.close()
    conn.close()

