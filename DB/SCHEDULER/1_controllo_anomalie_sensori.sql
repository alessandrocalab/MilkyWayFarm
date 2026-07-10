--PERMETTE DI CONTROLLARE PERIODICAMENTE
--SE VI SONO REGISTRAZIONI ANOMALE DEI SENSORI

BEGIN
    DBMS_SCHEDULER.CREATE_JOB(
        JOB_NAME=>'JOB_CONTROLLO_ANOMALIE_SENSORI',
        JOB_TYPE=>'PLSQL_BLOCK',
        JOB_ACTION=>'BEGIN 
                    CONTROLLO_ANOMALIE_SENSORI(SYSDATE); 
                    END;',
                    
        START_DATE=>SYSTIMESTAMP,
        REPEAT_INTERVAL=>'FREQ=DAILY;
                        BYHOUR=0;
                        BYMINUTE=0;
                        BYSECOND=0',
        ENABLED=>TRUE,
        COMMENTS=>'Controllo giornaliero anomalie sensori'
    );
END;
/
