SET SQLBLANKLINES ON 
--senza interpreta male le righe vuote


--Sezione: 1_prodotto

@1_prodotto/3_unita_di_misura.sql
@1_prodotto/1_tipo_prodotto.sql
@1_prodotto/2_sostanza.sql

--Sezione: 2_struttura

@2_struttura/1_struttura.sql
@2_struttura/2_blocco_animale.sql
@2_struttura/3_cella_idroponica.sql
@2_struttura/4_tipo_sensore.sql
@2_struttura/5_sensore.sql
@2_struttura/6_registrazione_sensore.sql

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
@4_agricoltura/2_tipo_coltura.sql
@4_agricoltura/3_ciclo_coltivazione.sql
@4_agricoltura/4_produzione_agricola.sql
@4_agricoltura/5_semi_missione.sql

--Sezione: 5_associazioni

@5_associazioni/1_stadio_crescita_prevede_dieta.sql
@5_associazioni/2_dieta_comprende_prodotto.sql
@5_associazioni/3_prodotto_contiene_sostanza.sql
@5_associazioni/4_stadio_crescita_intollerante_sostanza.sql
@5_associazioni/5_blocco_ammette_tipo_animale.sql
@5_associazioni/6_prodotto_da_stadio_crescita.sql
@5_associazioni/7_animale_allocato_blocco.sql
@5_associazioni/8_cella_idr_rispetta_mod_colt.sql
@5_associazioni/9_tipo_colt_accetta_mod_colt.sql
@5_associazioni/10_tipo_coltura_tipo_prodotto.sql
@5_associazioni/13_tipo_coltura_usa_semi_di_tipo.sql
@5_associazioni/14_blocco_animale_contiene_sensore.sql
@5_associazioni/15_cella_idr_contiene_sensore.sql


COMMIT;
