#!/usr/bin/env python3
from pathlib import Path
import argparse
import shutil


def is_probably_text_file(path: Path) -> bool:
    """
    Evita di modificare file binari tipo immagini, pdf, zip, ecc.
    """
    try:
        with open(path, "rb") as f:
            chunk = f.read(2048)
        chunk.decode("utf-8")
        return True
    except UnicodeDecodeError:
        return False
    except Exception:
        return False


def modifica_file(path: Path, backup: bool = True) -> bool:
    """
    Ritorna True se il file è stato modificato.
    """
    if not path.is_file():
        return False

    if not is_probably_text_file(path):
        return False

    try:
        testo = path.read_text(encoding="utf-8")
    except Exception:
        return False

    nuovo_testo = testo.replace("VARCHAR2(30)", "VARCHAR(60)")
    nuovo_testo = nuovo_testo.replace("VARCHAR2(60)", "VARCHAR(60)")

    if nuovo_testo == testo:
        return False

    if backup:
        backup_path = path.with_suffix(path.suffix + ".bak")
        shutil.copy2(path, backup_path)

    path.write_text(nuovo_testo, encoding="utf-8")
    return True


def modifica_cartella(root_path: str, backup: bool = True):
    root = Path(root_path).expanduser().resolve()

    if not root.exists():
        raise FileNotFoundError(f"La cartella non esiste: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Il path non è una cartella: {root}")

    modificati = 0
    controllati = 0

    for file_path in root.rglob("*"):
        if file_path.is_file():
            controllati += 1

            if modifica_file(file_path, backup=backup):
                modificati += 1
                print(f"Modificato: {file_path}")

    print()
    print(f"File controllati: {controllati}")
    print(f"File modificati: {modificati}")


def main():
    parser = argparse.ArgumentParser(
        description="Sostituisce VARCHAR2(30) e VARCHAR2(60) con VARCHAR(60) in tutti i file di una cartella."
    )

    parser.add_argument(
        "cartella",
        help="Path della cartella da modificare"
    )

    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Non creare file .bak di backup"
    )

    args = parser.parse_args()

    modifica_cartella(
        args.cartella,
        backup=not args.no_backup
    )


if __name__ == "__main__":
    main()