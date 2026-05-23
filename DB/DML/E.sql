SET SQLBLANKLINES ON 
--senza interpreta male le righe vuote


--Sezione: 1_prodotto

@1_prodotto/1_tipo_prodotto.sql
@1_prodotto/2_sostanza.sql
@1_prodotto/3_modalita_conservazione.sql

--Sezione: 2_struttura

@2_struttura/1_struttura.sql
@2_struttura/2_area_st.sql
@2_struttura/3_blocco_animale.sql
@2_struttura/4_scaffale.sql
@2_struttura/5_serbatoio.sql
@2_struttura/9_cella_idroponica.sql

--Sezione: 3_animale

@3_animale/1_tipo_animale.sql
@3_animale/2_animale.sql
@3_animale/3_stadio_crescita.sql
@3_animale/4_dieta_animale.sql
@3_animale/5_tipo_vaccino.sql
@3_animale/6_vaccinazione.sql
@3_animale/7_visita_veterinaria.sql
@3_animale/8_prescrizione_animale.sql
@3_animale/9_produzione_animale.sql

--Sezione: 4_agricoltura

@4_agricoltura/1_modalita_coltivazione.sql
@4_agricoltura/2_tipo_coltura.SQL
@4_agricoltura/3_ciclo_coltivazione.sql
@4_agricoltura/5_produzione_agricola.sql

--Sezione: 6_associazioni

@6_associazioni/7_prodotto_da_stadio_crescita.sql
@6_associazioni/9_animale_allocato_blocco.sql


COMMIT;