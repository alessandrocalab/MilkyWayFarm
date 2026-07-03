CREATE TRIGGER TRG_PRODOTTO_EDIBILE
BEFORE INSERT OR UPDATE ON TIPO_PRODOTTO
FOR EACH ROW

BEGIN 
    IF :NEW.IS_EDIBILE=1 THEN
        IF :NEW.FIBRE IS NULL
            OR :NEW.PROTEINE IS NULL 
            OR :NEW.GRASSI IS NULL
            OR :NEW.CARBOIDRATI IS NULL 
            THEN 

                RAISE_APPLICATION_ERROR(
                    -20001,
                    'Un prodotto edibile deve avere tutti i valori nutrizionali'
                );
            
            END IF;
        
    ELSE
        IF :NEW.FIBRE IS NOT NULL 
            OR :NEW.PROTEINE IS NOT NULL 
            OR :NEW.GRASSI IS NOT NULL
            OR :NEW.CARBOIDRATI IS NOT NULL 
            THEN 
            
                RAISE_APPLICATION_ERROR(
                    -20001,
                    'Un prodotto NON edibile non può avere valori nutrizionali'
                );

            END IF;
        END IF;
    END;
