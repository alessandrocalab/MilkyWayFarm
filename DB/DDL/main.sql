SET SQLBLANKLINES ON 
--senza interpreta male le righe vuote

--Eliminazione schema precedente

@../drop_all.sql


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
@2_struttura/6_tipo_sensore.sql
@2_struttura/7_sensore.sql
@2_struttura/8_registrazione_sensore.sql
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
@4_agricoltura/4_produzione_agricola.sql

--Sezione: 5_missione.sql

@5_missione.sql/1_missione_rifornimento.sql
@5_missione.sql/2_prodotto_missione.sql

--Sezione: 6_associazioni

@6_associazioni/1_stadio_crescita_prevede_dieta.sql
@6_associazioni/2_dieta_comprende_prodotto.sql
@6_associazioni/3_prodotto_contiene_sostanza.sql
@6_associazioni/4_stadio_crescita_intollerante_sostanza.sql
@6_associazioni/5_animale_allergico_sostanza.sql
@6_associazioni/7_prodotto_da_stadio_crescita.sql
@6_associazioni/8_prodotto_prevede_mod_cons.sql
@6_associazioni/9_animale_allocato_blocco.sql
@6_associazioni/10_cella_idr_rispetta_mod_colt.sql
@6_associazioni/11_tipo_colt_accetta_mod_colt.sql
@6_associazioni/12_tipo_coltura_tipo_prodotto.SQL
@6_associazioni/13_scaffale_rispetta_mod_cons.sql
@6_associazioni/14_serb_rispetta_mod_cons.sql
@6_associazioni/15_produzione_agricola_alloc_serb.sql
@6_associazioni/16_produzione_agricola_alloc_scaff.sql
@6_associazioni/17_produzione_animale_allocazione_serb.sql
@6_associazioni/18_produzione_animale_alloc_scaff.sql
@6_associazioni/19_prodotto_missione_alloc_serb.sql
@6_associazioni/20_prodotto_missione_alloc_scaff.sql
@6_associazioni/21_dealloc_prod_ciclo_colt_serb.sql
@6_associazioni/22_dealloc_prod_ciclo_colt_scaff.sql
@6_associazioni/23_dealloc_prod_blocco_animale_serb.sql
@6_associazioni/24_dealloc_prod_blocco_animale_scaff.sql


COMMIT;