from python.connection.getConnection import get_connection

#ETICHETTA, DATA_USCITA, ETICHETTA_GENITORE, SESSO, MESE_NASCITA, ANNO_NASCITA, DATA_INGRESSO, NOME_TIPO_ANIMALE


def get_animali():
    conn=get_connection()
    cur=conn.cursor()

    cur.execute("SELECT * FROM ANIMALE")

    colonne = [col[0] for col in cur.description]

    data=[]

    for riga in cur.fetchall():
        animale = dict(zip(colonne, riga))
        data.append(animale)

    
    cur.close()
    conn.close()

    return data