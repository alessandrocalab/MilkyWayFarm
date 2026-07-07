SET SQLBLANKLINES ON 
--senza interpreta male le righe vuote


--Sezione: 2_struttura

@2_struttura/1_allocazioni_sensori.sql
@2_struttura/2_elementi_produttivi.sql
@2_struttura/3_anomalia_sensore.sql

--Sezione: 3_animale

@3_animale/1_verifica_produzione_animale.sql
@3_animale/2_produzione_animale_totale.sql

--Sezione: 4_agricoltura

@4_agricoltura/1_semi_missione_utilizzati.sql
@4_agricoltura/2_semi_misisone_disponibili.sql
@4_agricoltura/3_semi_produzione_agricola_utilizzati.sql
@4_agricoltura/4_semi_produzione_agricola_disponibili.sql
@4_agricoltura/5_semi_disponibili.sql
@4_agricoltura/6_consumi_ciclo_coltivazione.sql
@4_agricoltura/7_verifica_produzione_agricola.sql
@4_agricoltura/8_consumi_ciclo_coltivazione_2.sql
@4_agricoltura/9_produzione_agricola_totale.sql


COMMIT;
