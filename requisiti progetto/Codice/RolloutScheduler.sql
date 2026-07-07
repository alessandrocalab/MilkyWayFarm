--%%%%%%% JOB CHE OGNI PRIMO DEL MESE CANCELLA TUTTI I RICEVIMENTI PRECEDENTI DI UN MESE
BEGIN
DBMS_SCHEDULER.CREATE_JOB (
   job_name			=>	'Rollout',
   job_type			=>	'PLSQL_BLOCK',
   job_action		=>	'BEGIN 
											DELETE FROM ricevimento 
											WHERE data_e_ora_i<SYSDATE-30;
										END;',
   start_date		=> TO_DATE('01-SET-2014','DD-MON-YYYY'),
   repeat_interval	=> 'FREQ=MONTHLY', 
   enabled			=>	TRUE,
   comments			=>	'Cancellazione dei dati vecchi');
END;

--%%%%%%% CANCELLAZIONE DEL JOB ROLLOUT 
BEGIN
DBMS_SCHEDULER.DROP_JOB ('Rollout');
END;