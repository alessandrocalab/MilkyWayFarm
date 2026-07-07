BEGIN
    FOR j IN (
        SELECT job_name
        FROM user_scheduler_jobs
    ) LOOP
        DBMS_SCHEDULER.DROP_JOB(j.job_name, TRUE);
    END LOOP;

    FOR tr IN (
        SELECT trigger_name
        FROM user_triggers
    ) LOOP
        EXECUTE IMMEDIATE 'DROP TRIGGER "' || tr.trigger_name || '"';
    END LOOP;

    FOR v IN (
        SELECT view_name
        FROM user_views
    ) LOOP
        EXECUTE IMMEDIATE 'DROP VIEW "' || v.view_name || '"';
    END LOOP;

    FOR p IN (
        SELECT object_name
        FROM user_procedures
        WHERE object_type='PROCEDURE'
    ) LOOP
        EXECUTE IMMEDIATE 'DROP PROCEDURE "' || p.object_name || '"';
    END LOOP;

    FOR t IN (
        SELECT table_name
        FROM user_tables
    ) LOOP
        EXECUTE IMMEDIATE 'DROP TABLE "' || t.table_name || '" CASCADE CONSTRAINTS PURGE';
    END LOOP;
END;
/

COMMIT;
