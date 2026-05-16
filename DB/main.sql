-- MAIN DATABASE AGRICOLTURA

PROMPT ================================
PROMPT DROP TABELLE
PROMPT ================================

@0_drop/drop_all.sql


PROMPT ================================
PROMPT CREAZIONE TABELLE - DDL
PROMPT ================================

@1_DDL/1_base.sql
@1_DDL/2_animali.sql
@1_DDL/9_associazioni.sql


PROMPT ================================
PROMPT POPOLAMENTO TABELLE - DML
PROMPT ================================

COMMIT;

PROMPT ================================
PROMPT DATABASE CREATO E POPOLATO
PROMPT ================================