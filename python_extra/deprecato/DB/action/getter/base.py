#tutorial SQL injection:

from python.connection.getConnection import get_connection

def get_data_base(query):
    conn=get_connection()
    cur=conn.cursor()

    cur.execute(query)


    colonne = [col[0] for col in cur.description]

    data=[]

    for riga in cur.fetchall():
        tuple = dict(zip(colonne, riga))
        data.append(tuple)

    
    cur.close()
    conn.close()

    return data

