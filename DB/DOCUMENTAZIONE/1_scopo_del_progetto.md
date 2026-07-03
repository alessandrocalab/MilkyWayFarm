# Scopo del progetto

## Titolo

**MilkyWayFarm: sistema informativo per la gestione di una biofarm bioregenerativa in ambiente spaziale controllato**

## Contesto

MilkyWayFarm nasce come prototipo di base di dati per una biofarm sperimentale commissionata dall'ESA, pensata per supportare studi su missioni spaziali di lunga durata, basi lunari, basi marziane o habitat analoghi terrestri.

In un ambiente extraterrestre il rifornimento costante dalla Terra e costoso, lento e rischioso. Per questo motivo una missione di lunga durata deve valutare sistemi capaci di produrre cibo, biomassa, fertilizzanti biologici e dati ambientali in modo controllato. Il database non rappresenta quindi una semplice fattoria, ma un sistema produttivo chiuso o semi-chiuso in cui ogni risorsa deve essere tracciata.

## Obiettivo generale

L'obiettivo del progetto e progettare e implementare una base di dati in grado di gestire le informazioni operative e sperimentali di una biofarm spaziale. Il sistema permette di registrare strutture, celle idroponiche, blocchi animali, sensori, colture, animali, prodotti, sostanze, diete, visite veterinarie, cicli di coltivazione e produzioni.

Il database deve consentire di rispondere a domande come:

- quali colture sono attive in una determinata cella idroponica;
- quali semi sono disponibili per avviare nuovi cicli;
- quali prodotti agricoli o animali sono stati ottenuti;
- quali animali sono presenti in ciascun blocco;
- quali sensori sono installati e quali valori ambientali registrano;
- quali risorse sono state consumate o prodotte nel tempo;
- quali vincoli biologici, sanitari e ambientali devono essere rispettati.

## Utilita per l'ESA

Per l'ESA un sistema di questo tipo puo essere utile come supporto alla progettazione di sistemi bioregenerativi per missioni di lunga durata. In particolare, la base di dati permette di:

- **monitorare l'autosufficienza alimentare**, verificando quanta produzione agricola e animale puo essere ottenuta nel tempo;
- **ottimizzare risorse critiche**, come semi, acqua, energia, soluzione nutritiva e fertilizzanti biologici;
- **garantire tracciabilita**, collegando ogni produzione al ciclo, agli input usati e all'ambiente in cui e stata generata;
- **controllare il benessere biologico**, registrando visite veterinarie, prescrizioni, vaccinazioni e compatibilita tra animali, blocchi e stadi di crescita;
- **valutare le condizioni ambientali**, tramite sensori di temperatura, umidita ed energia;
- **supportare decisioni operative**, ad esempio scegliere quali colture avviare, quali semi utilizzare o quando intervenire su un ambiente fuori range.

## Perche serve una gestione dati accurata

In una biofarm spaziale ogni errore puo compromettere la continuita produttiva. Se i semi terminano, una filiera agricola si interrompe. Se una cella idroponica ospita due cicli sovrapposti, le produzioni diventano incoerenti. Se un animale e allocato in due blocchi nello stesso momento, i dati sanitari e produttivi perdono affidabilita. Se una produzione viene registrata prima del ciclo che l'ha generata, la tracciabilita scientifica non e piu valida.

La gestione dei dati e quindi centrale per:

- preservare coerenza e affidabilita delle informazioni;
- ridurre sprechi di risorse;
- mantenere la tracciabilita dei processi;
- supportare audit scientifici e tecnici;
- confrontare strategie produttive diverse;
- preparare dati utili a sistemi di controllo automatico.

## Confine del progetto

Il progetto si concentra sulla progettazione e implementazione della base di dati. La parte di simulazione presente negli script PL/SQL e da considerarsi un supporto al collaudo e alla generazione di dati dimostrativi, non il nucleo concettuale del sistema.

Il nucleo del progetto e costituito da:

- schema relazionale;
- vincoli di integrita statici;
- dati di popolamento;
- query operative;
- procedure PL/SQL di supporto;
- future viste, utenti, privilegi, trigger e scheduler.

## Sintesi

MilkyWayFarm puo essere presentato come un sistema informativo sperimentale per la gestione di una biofarm ESA, finalizzato allo studio di autosufficienza, tracciabilita, produzione biologica e controllo ambientale in scenari spaziali di lunga durata.
