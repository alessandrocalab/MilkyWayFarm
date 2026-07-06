SET SQLBLANKLINES ON 
--senza interpreta male le righe vuote

--Eliminazione schema precedente

@drop_all.sql


--Sezione: DDL


--Sezione: 0_tmp

@DDL/0_tmp/1_giorni_temp.sql

--Sezione: 1_prodotto

@DDL/1_prodotto/3_unita_di_misura.sql
@DDL/1_prodotto/1_tipo_prodotto.sql
@DDL/1_prodotto/2_sostanza.sql

--Sezione: 2_struttura

@DDL/2_struttura/1_struttura.sql
@DDL/2_struttura/2_blocco_animale.sql
@DDL/2_struttura/3_cella_idroponica.sql
@DDL/2_struttura/4_tipo_sensore.sql
@DDL/2_struttura/5_sensore.sql
@DDL/2_struttura/6_registrazione_sensore.sql

--Sezione: 3_animale

@DDL/3_animale/1_tipo_animale.sql
@DDL/3_animale/2_animale.sql
@DDL/3_animale/3_stadio_crescita.sql
@DDL/3_animale/4_dieta_animale.sql
@DDL/3_animale/5_visita_veterinaria.sql
@DDL/3_animale/6_prescrizione_animale.sql
@DDL/3_animale/7_produzione_animale.sql

--Sezione: 4_agricoltura

@DDL/4_agricoltura/1_modalita_coltivazione.sql
@DDL/4_agricoltura/2_tipo_coltura.sql
@DDL/4_agricoltura/3_ciclo_coltivazione.sql
@DDL/4_agricoltura/4_produzione_agricola.sql
@DDL/4_agricoltura/5_semi_missione.sql

--Sezione: 5_associazioni

@DDL/5_associazioni/1_stadio_crescita_prevede_dieta.sql
@DDL/5_associazioni/2_dieta_comprende_prodotto.sql
@DDL/5_associazioni/3_prodotto_contiene_sostanza.sql
@DDL/5_associazioni/4_stadio_crescita_intollerante_sostanza.sql
@DDL/5_associazioni/5_blocco_ammette_tipo_animale.sql
@DDL/5_associazioni/6_prodotto_da_stadio_crescita.sql
@DDL/5_associazioni/7_animale_allocato_blocco.sql
@DDL/5_associazioni/8_cella_idr_rispetta_mod_colt.sql
@DDL/5_associazioni/9_tipo_colt_accetta_mod_colt.sql
@DDL/5_associazioni/10_tipo_coltura_tipo_prodotto.sql
@DDL/5_associazioni/11_ciclo_colt_utilizza_semi_missione.sql
@DDL/5_associazioni/12_ciclo_colt_utilizza_produzione_agricola.sql
@DDL/5_associazioni/13_blocco_animale_contiene_sensore.sql
@DDL/5_associazioni/14_cella_idr_contiene_sensore.sql

--Sezione: DML


--Sezione: 1_prodotto

@DML/1_prodotto/3_unita_di_misura.sql
@DML/1_prodotto/1_tipo_prodotto.sql
@DML/1_prodotto/2_sostanza.sql

--Sezione: 2_struttura

@DML/2_struttura/1_struttura.sql
@DML/2_struttura/2_blocco_animale.sql
@DML/2_struttura/3_cella_idroponica.sql
@DML/2_struttura/4_tipo_sensore.sql
@DML/2_struttura/5_sensore.sql
@DML/2_struttura/6_registrazione_sensore.sql

--Sezione: 3_animale

@DML/3_animale/1_tipo_animale.sql
@DML/3_animale/2_animale.sql
@DML/3_animale/3_stadio_crescita.sql
@DML/3_animale/4_dieta_animale.sql
@DML/3_animale/5_visita_veterinaria.sql
@DML/3_animale/6_prescrizione_animale.sql
@DML/3_animale/7_produzione_animale.sql

--Sezione: 4_agricoltura

@DML/4_agricoltura/1_modalita_coltivazione.sql
@DML/4_agricoltura/2_tipo_coltura.sql
@DML/4_agricoltura/3_ciclo_coltivazione.sql
@DML/4_agricoltura/4_produzione_agricola.sql
@DML/4_agricoltura/5_semi_missione.sql

--Sezione: 5_associazioni

@DML/5_associazioni/1_stadio_crescita_prevede_dieta.sql
@DML/5_associazioni/2_dieta_comprende_prodotto.sql
@DML/5_associazioni/3_prodotto_contiene_sostanza.sql
@DML/5_associazioni/4_stadio_crescita_intollerante_sostanza.sql
@DML/5_associazioni/5_blocco_ammette_tipo_animale.sql
@DML/5_associazioni/6_prodotto_da_stadio_crescita.sql
@DML/5_associazioni/7_animale_allocato_blocco.sql
@DML/5_associazioni/8_cella_idr_rispetta_mod_colt.sql
@DML/5_associazioni/9_tipo_colt_accetta_mod_colt.sql
@DML/5_associazioni/10_tipo_coltura_tipo_prodotto.sql
@DML/5_associazioni/11_ciclo_colt_utilizza_semi_missione.sql
@DML/5_associazioni/12_ciclo_colt_utilizza_produzione_agricola.sql
@DML/5_associazioni/13_blocco_animale_contiene_sensore.sql
@DML/5_associazioni/14_cella_idr_contiene_sensore.sql

--Sezione: VISTA

@VISTA/1_semi_missione_utilizzati.sql
@VISTA/2_semi_misisone_disponibili.sql
@VISTA/3_semi_produzione_agricola_utilizzati.sql
@VISTA/4_semi_produzione_agricola_disponibili.sql
@VISTA/5_semi_disponibili.sql
@VISTA/6_allocazioni_sensori.sql
@VISTA/7_elementi_produttivi.sql
@VISTA/8_verifica_produzione_animale.sql
@VISTA/9_consumi_ciclo_coltivazione.sql
@VISTA/10_verifica_produzione_agricola.sql

--Sezione: TRIGGER


--Sezione: 1_prodotto

@TRIGGER/1_prodotto/1_tipo_prodotto.sql

--Sezione: 2_struttura

@TRIGGER/2_struttura/1_struttura.sql
@TRIGGER/2_struttura/2_blocco_animale.sql
@TRIGGER/2_struttura/3_cella_idroponica.sql
@TRIGGER/2_struttura/6_registrazione_sensore.sql

--Sezione: 3_animale

@TRIGGER/3_animale/2_animale.sql
@TRIGGER/3_animale/5_visita_veterinaria.sql
@TRIGGER/3_animale/7_produzione_animale.sql

--Sezione: 4_agricoltura

@TRIGGER/4_agricoltura/3_ciclo_coltivazione.sql
@TRIGGER/4_agricoltura/4_produzione_agricola.sql

--Sezione: 5_associazioni

@TRIGGER/5_associazioni/1_stadio_crescita_prevede_dieta.sql
@TRIGGER/5_associazioni/2_dieta_comprende_prodotto.sql
@TRIGGER/5_associazioni/5_blocco_ammette_tipo_animale.sql
@TRIGGER/5_associazioni/7_animale_allocato_blocco.sql
@TRIGGER/5_associazioni/11_ciclo_colt_utilizza_semi_missione.sql
@TRIGGER/5_associazioni/12_ciclo_colt_utilizza_produzione_agricola.sql
@TRIGGER/5_associazioni/13_blocco_animale_contiene_sensore.sql
@TRIGGER/5_associazioni/14_cella_idr_contiene_sensore.sql


COMMIT;
