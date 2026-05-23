import os
import sys
import datetime
import hashlib
from pprint import pformat


# =========================
# TROVA ROOT PROGETTO
# =========================

PROJECT_ROOT = os.getcwd()

while os.path.basename(PROJECT_ROOT) != "MilkWayFarm":
    parent = os.path.dirname(PROJECT_ROOT)

    if parent == PROJECT_ROOT:
        raise RuntimeError("Cartella MilkWayFarm non trovata risalendo dal path corrente")

    os.chdir("..")
    PROJECT_ROOT = os.getcwd()

sys.path.append(PROJECT_ROOT)


# =========================
# IMPORT DATA GETTER
# =========================

from python.data_getter.animali import get_animali
from python.data_getter.stadio_crescita_puo_produrre import get_stadio_crescita_puo_produrre
from python.data_getter.stadio_crescita import get_stadio_crescita
from python.data_getter.animale_allocato_blocco_animale import get_animale_allocato_blocco


# =========================
# UTILITY BASE
# =========================

def normalizza_records(data):
    """
    Se il getter ritorna una lista di dict, la lascia uguale.
    Se ritorna un dict indicizzato, usa i valori.
    """
    if isinstance(data, dict):
        return list(data.values())

    return list(data)


def pulisci_stringa(value):
    if value is None:
        return None

    return str(value).strip()


def to_date(value):
    if value is None:
        return None

    if isinstance(value, datetime.datetime):
        return value.date()

    if isinstance(value, datetime.date):
        return value

    raise TypeError(f"Tipo data non gestito: {type(value)} -> {value}")


def date_to_sql(data):
    return f"DATE '{data.strftime('%Y-%m-%d')}'"


def quote_sql(value):
    return f"'{pulisci_stringa(value)}'"


def random_stabile(min_value, max_value, *keys):
    """
    Genera un valore pseudo-casuale stabile.
    Stesse chiavi = stesso risultato.
    Utile per rigenerare sempre gli stessi dati.
    """
    raw = "|".join(str(k) for k in keys)
    digest = hashlib.sha256(raw.encode("utf-8")).hexdigest()
    numero = int(digest[:12], 16)
    frazione = numero / float(0xFFFFFFFFFFFF)

    return min_value + (max_value - min_value) * frazione


# =========================
# DATE ANIMALI
# =========================

def min_data_ingresso(data_animali):
    min_data = datetime.date.today()

    for animale in data_animali:
        data_ingresso = to_date(animale["DATA_INGRESSO"])

        if data_ingresso < min_data:
            min_data = data_ingresso

    return min_data


def animale_presente_in_data(animale, data_corrente):
    data_ingresso = to_date(animale["DATA_INGRESSO"])
    data_uscita = to_date(animale["DATA_USCITA"])

    return data_ingresso <= data_corrente and (
        data_uscita is None or data_corrente <= data_uscita
    )


def get_animali_presenti(data_corrente, data_animali):
    presenti = []

    for animale in data_animali:
        if animale_presente_in_data(animale, data_corrente):
            presenti.append(animale)

    return presenti


def is_giorno_uscita(animale, data_corrente):
    data_uscita = to_date(animale["DATA_USCITA"])
    return data_uscita is not None and data_uscita == data_corrente


# =========================
# STADIO CRESCITA
# =========================

def eta_mesi_animale(animale, data_corrente):
    anno_nascita = int(animale["ANNO_NASCITA"])
    mese_nascita = int(animale["MESE_NASCITA"])

    return (data_corrente.year - anno_nascita) * 12 + (data_corrente.month - mese_nascita)


def get_stadio_attuale(animale, data_corrente, data_stadio_crescita):
    tipo_animale = pulisci_stringa(animale["NOME_TIPO_ANIMALE"])
    eta_mesi = eta_mesi_animale(animale, data_corrente)

    stadi_validi = []

    for stadio in data_stadio_crescita:
        if pulisci_stringa(stadio["NOME_TIPO_ANIMALE"]) != tipo_animale:
            continue

        eta_minima = int(stadio["ETA_MINIMA_MESI"])

        if eta_minima <= eta_mesi:
            stadi_validi.append(stadio)

    if not stadi_validi:
        return None

    return max(stadi_validi, key=lambda s: int(s["ETA_MINIMA_MESI"]))


# =========================
# ALLOCAZIONE
# =========================

def get_data_deallocazione(allocazione):
    if "DATA_DEALLOCAZIONE" in allocazione:
        return to_date(allocazione["DATA_DEALLOCAZIONE"])

    if "DATA_DEALLOCAIONE" in allocazione:
        return to_date(allocazione["DATA_DEALLOCAIONE"])

    return None


def get_allocazione_corrente(animale, data_corrente, data_allocazioni):
    etichetta = pulisci_stringa(animale["ETICHETTA"])

    for allocazione in data_allocazioni:
        if pulisci_stringa(allocazione["ETICHETTA_ANIMALE"]) != etichetta:
            continue

        data_allocazione = to_date(allocazione["DATA_ALLOCAZIONE"])
        data_deallocazione = get_data_deallocazione(allocazione)

        if data_allocazione <= data_corrente and (
            data_deallocazione is None or data_corrente <= data_deallocazione
        ):
            return allocazione

    return None


# =========================
# PRODOTTI POSSIBILI
# =========================

def get_prodotti_possibili(animale, stadio_attuale, data_stadio_crescita_puo_produrre):
    tipo_animale = pulisci_stringa(animale["NOME_TIPO_ANIMALE"])
    nome_stadio = pulisci_stringa(stadio_attuale["NOME_STADIO_CRESCITA"])

    prodotti = []

    for record in data_stadio_crescita_puo_produrre:
        if (
            pulisci_stringa(record["NOME_TIPO_ANIMALE"]) == tipo_animale
            and pulisci_stringa(record["NOME_STADIO_CRESCITA"]) == nome_stadio
        ):
            prodotti.append(record)

    return prodotti


# =========================
# QUANTITÀ PRODUZIONE
# =========================

def calcola_quantita(animale, nome_prodotto, data_corrente):
    etichetta = pulisci_stringa(animale["ETICHETTA"])
    prodotto = pulisci_stringa(nome_prodotto)

    key_base = (
        etichetta,
        prodotto,
        data_corrente.isoformat()
    )

    # Prodotti non giornalieri: solo al giorno di uscita.
    prodotti_macellazione = [
        "Carne bovina",
        "Carne caprina",
        "Carne ovina",
        "Carne suina",
        "Carne di pollo",
        "Carne di tacchino",
        "Carne di coniglio",
        "Pelle bovina"
    ]

    if prodotto in prodotti_macellazione:
        if not is_giorno_uscita(animale, data_corrente):
            return 0.00

    # Lana: evento trimestrale.
    if prodotto == "Lana ovina":
        if not (data_corrente.day == 1 and data_corrente.month in [3, 6, 9, 12]):
            return 0.00

    # Piume: evento mensile.
    if prodotto == "Piume di pollame":
        if data_corrente.day != 1:
            return 0.00

    # Produzioni giornaliere / periodiche.
    if prodotto == "Latte bovino":
        return round(random_stabile(16.00, 28.00, *key_base), 2)

    if prodotto == "Latte caprino":
        return round(random_stabile(1.50, 3.50, *key_base), 2)

    if prodotto == "Latte ovino":
        return round(random_stabile(0.80, 2.00, *key_base), 2)

    if prodotto == "Uova di gallina":
        return round(random_stabile(0.70, 1.00, *key_base), 2)

    if prodotto == "Letame bovino":
        return round(random_stabile(18.00, 35.00, *key_base), 2)

    if prodotto == "Letame ovino":
        return round(random_stabile(1.00, 2.50, *key_base), 2)

    if prodotto == "Letame suino":
        return round(random_stabile(2.00, 5.00, *key_base), 2)

    if prodotto == "Pollina":
        return round(random_stabile(0.05, 0.18, *key_base), 2)

    if prodotto == "Lana ovina":
        return round(random_stabile(0.80, 1.80, *key_base), 2)

    if prodotto == "Piume di pollame":
        return round(random_stabile(0.02, 0.08, *key_base), 2)

    # Prodotti da uscita/macellazione.
    if prodotto == "Carne bovina":
        return round(random_stabile(350.00, 550.00, *key_base), 2)

    if prodotto == "Pelle bovina":
        return round(random_stabile(25.00, 45.00, *key_base), 2)

    if prodotto == "Carne caprina":
        return round(random_stabile(18.00, 30.00, *key_base), 2)

    if prodotto == "Carne ovina":
        return round(random_stabile(20.00, 35.00, *key_base), 2)

    if prodotto == "Carne suina":
        return round(random_stabile(70.00, 110.00, *key_base), 2)

    if prodotto == "Carne di pollo":
        return round(random_stabile(1.50, 3.00, *key_base), 2)

    if prodotto == "Carne di tacchino":
        return round(random_stabile(6.00, 12.00, *key_base), 2)

    if prodotto == "Carne di coniglio":
        return round(random_stabile(1.20, 2.50, *key_base), 2)

    return 0.00


# =========================
# SALVATAGGIO FILE PY
# =========================

def salva_liste_py(
    path_file,
    DATA_PRODUZIONE,
    NUMERO_BLOCCO,
    NOME_STRUTTURA,
    CODICE_AREA,
    NOME_PRODOTTO,
    QUANTITA
):
    with open(path_file, "w", encoding="utf-8") as f:
        f.write("# FILE GENERATO AUTOMATICAMENTE\n")
        f.write("# DATA_PRODUZIONE, NUMERO_BLOCCO, NOME_STRUTTURA, CODICE_AREA, NOME_PRODOTTO, QUANTITA\n\n")

        f.write("DATA_PRODUZIONE = ")
        f.write(pformat(DATA_PRODUZIONE, width=160))
        f.write("\n\n")

        f.write("NUMERO_BLOCCO = ")
        f.write(pformat(NUMERO_BLOCCO, width=160))
        f.write("\n\n")

        f.write("NOME_STRUTTURA = ")
        f.write(pformat(NOME_STRUTTURA, width=160))
        f.write("\n\n")

        f.write("CODICE_AREA = ")
        f.write(pformat(CODICE_AREA, width=160))
        f.write("\n\n")

        f.write("NOME_PRODOTTO = ")
        f.write(pformat(NOME_PRODOTTO, width=160))
        f.write("\n\n")

        f.write("QUANTITA = ")
        f.write(pformat(QUANTITA, width=160))
        f.write("\n\n")


# =========================
# GENERAZIONE LISTE
# =========================

def genera_liste_produzione():
    data_animali = normalizza_records(get_animali())
    data_stadio_crescita_puo_produrre = normalizza_records(get_stadio_crescita_puo_produrre())
    data_stadio_crescita = normalizza_records(get_stadio_crescita())
    data_allocazioni = normalizza_records(get_animale_allocato_blocco())

    DATA_INIZIO = min_data_ingresso(data_animali)
    DATA_FINE = datetime.date.today()

    produzioni_aggregate = {}

    data_corrente = DATA_INIZIO

    while data_corrente <= DATA_FINE:
        animali_presenti = get_animali_presenti(data_corrente, data_animali)

        for animale in animali_presenti:
            allocazione = get_allocazione_corrente(
                animale,
                data_corrente,
                data_allocazioni
            )

            if allocazione is None:
                continue

            stadio_attuale = get_stadio_attuale(
                animale,
                data_corrente,
                data_stadio_crescita
            )

            if stadio_attuale is None:
                continue

            prodotti_possibili = get_prodotti_possibili(
                animale,
                stadio_attuale,
                data_stadio_crescita_puo_produrre
            )

            for prodotto_record in prodotti_possibili:
                nome_prodotto = pulisci_stringa(prodotto_record["NOME_PRODOTTO"])

                quantita = calcola_quantita(
                    animale,
                    nome_prodotto,
                    data_corrente
                )

                if quantita <= 0:
                    continue

                numero_blocco = pulisci_stringa(allocazione["NUMERO_BLOCCO"])
                nome_struttura = pulisci_stringa(allocazione["NOME_STRUTTURA"])
                codice_area = pulisci_stringa(allocazione["CODICE_AREA"])

                key = (
                    data_corrente,
                    numero_blocco,
                    nome_struttura,
                    codice_area,
                    nome_prodotto
                )

                produzioni_aggregate[key] = produzioni_aggregate.get(key, 0.00) + quantita

        data_corrente += datetime.timedelta(days=1)

    DATA_PRODUZIONE = []
    NUMERO_BLOCCO = []
    NOME_STRUTTURA = []
    CODICE_AREA = []
    NOME_PRODOTTO = []
    QUANTITA = []

    for key in sorted(produzioni_aggregate.keys()):
        data_produzione, numero_blocco, nome_struttura, codice_area, nome_prodotto = key
        quantita = round(produzioni_aggregate[key], 2)

        DATA_PRODUZIONE.append(date_to_sql(data_produzione))
        NUMERO_BLOCCO.append(quote_sql(numero_blocco))
        NOME_STRUTTURA.append(quote_sql(nome_struttura))
        CODICE_AREA.append(quote_sql(codice_area))
        NOME_PRODOTTO.append(quote_sql(nome_prodotto))
        QUANTITA.append(quantita)

    return {
        "DATA_PRODUZIONE": DATA_PRODUZIONE,
        "NUMERO_BLOCCO": NUMERO_BLOCCO,
        "NOME_STRUTTURA": NOME_STRUTTURA,
        "CODICE_AREA": CODICE_AREA,
        "NOME_PRODOTTO": NOME_PRODOTTO,
        "QUANTITA": QUANTITA
    }


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    liste = genera_liste_produzione()

    output_file = os.path.join(
        PROJECT_ROOT,
        "python",
        "generated_data",
        "produzione_animale_liste.py"
    )

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    salva_liste_py(
        output_file,
        liste["DATA_PRODUZIONE"],
        liste["NUMERO_BLOCCO"],
        liste["NOME_STRUTTURA"],
        liste["CODICE_AREA"],
        liste["NOME_PRODOTTO"],
        liste["QUANTITA"]
    )

    print("Produzioni generate:", len(liste["DATA_PRODUZIONE"]))
    print("File salvato in:", output_file)