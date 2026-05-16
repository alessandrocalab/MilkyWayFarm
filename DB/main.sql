SET SQLBLANKLINES ON --senza interpreta male le righe vuote

--Eliminazione schema precedente

@drop_all.sql


--Sezione: 1_prodotto

@DDL/1_prodotto/1_tipo_prodotto.sql
@DDL/1_prodotto/2_sostanza.sql
@DDL/1_prodotto/3_modalita_conservazione.sql

--Sezione: 2_struttura

@DDL/2_struttura/1_struttura.sql
@DDL/2_struttura/2_area_st.sql
@DDL/2_struttura/3_blocco_animale.sql
@DDL/2_struttura/4_scaffale.sql
@DDL/2_struttura/5_serbatoio.sql
@DDL/2_struttura/6_tipo_sensore.sql
@DDL/2_struttura/7_sensore.sql
@DDL/2_struttura/8_registrazione_sensore.sql

--Sezione: 3_animale

@DDL/3_animale/1_tipo_animale.sql
@DDL/3_animale/2_animale.sql
@DDL/3_animale/3_stadio_crescita.sql
@DDL/3_animale/4_nome_animale.sql
@DDL/3_animale/5_tipo_vaccino.sql
@DDL/3_animale/6_vaccinazione.sql
@DDL/3_animale/7_visita_veterinaria.sql
@DDL/3_animale/8_prescrizione_animale.sql
@DDL/3_animale/9_produzione_animale.sql

--Sezione: 9_associazioni

@DDL/9_associazioni/1_stadio_crescita_prevede_dieta.sql
@DDL/9_associazioni/2_dieta_comprende_prodotto.sql
@DDL/9_associazioni/3_prodotto_contiene_sostanza.sql
@DDL/9_associazioni/4_stadio_crescita_intollerante_sostanza.sql
@DDL/9_associazioni/5_animale_allergico_sostanza.sql
@DDL/9_associazioni/6_animale_prevede_dieta_speciale.sql
@DDL/9_associazioni/7_prodotto_da_stadio_crescita.sql
@DDL/9_associazioni/8_prodotto_prevede_mod_cons.sql
@DDL/9_associazioni/9_animale_allocato_blocco.sql


COMMIT;