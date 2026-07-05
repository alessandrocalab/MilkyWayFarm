SET SQLBLANKLINES ON 
--senza interpreta male le righe vuote


--Sezione: 1_prodotto

@1_prodotto/1_tipo_prodotto.sql

--Sezione: 2_struttura

@2_struttura/1_struttura.sql
@2_struttura/2_blocco_animale.sql
@2_struttura/3_cella_idroponica.sql
@2_struttura/6_registrazione_sensore.sql

--Sezione: 3_animale

@3_animale/2_animale.sql
@3_animale/5_visita_veterinaria.sql
@3_animale/7_produzione_animale.sql

--Sezione: 4_agricoltura

@4_agricoltura/3_ciclo_coltivazione.sql
@4_agricoltura/4_produzione_agricola.sql

--Sezione: 5_associazioni

@5_associazioni/1_stadio_crescita_prevede_dieta.sql
@5_associazioni/2_dieta_comprende_prodotto.sql
@5_associazioni/5_blocco_ammette_tipo_animale.sql
@5_associazioni/7_animale_allocato_blocco.sql
@5_associazioni/11_ciclo_colt_utilizza_semi_missione.sql
@5_associazioni/12_ciclo_colt_utilizza_produzione_agricola.sql
@5_associazioni/13_blocco_animale_contiene_sensore.sql
@5_associazioni/14_cella_idr_contiene_sensore.sql


COMMIT;
