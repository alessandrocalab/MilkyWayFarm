# Vincoli dinamici e scelta greedy sulla recenza

## Contesto

Nel database MilkyWayFarm alcune entita strutturali occupano fisicamente una parte della superficie disponibile all'interno di una struttura.

In particolare:

- un blocco animale occupa una certa `SUPERFICIE_MQ`;
- una cella idroponica occupa una certa `SUPERFICIE_MQ`;
- una struttura ha una superficie totale massima, indicata da `STRUTTURA.SUPERFICIE_MQ`;
- ogni blocco o cella ha una data di montaggio e una eventuale data di smontaggio.

Il problema da controllare e che la somma delle superfici occupate da blocchi animali e celle idroponiche attivi nello stesso periodo non superi mai la superficie totale della struttura.

## Problema generale

Il controllo completo della superficie sarebbe un vincolo temporale complesso.

Se fosse possibile inserire liberamente elementi strutturali con qualunque data di montaggio, anche retroattiva, ogni nuovo inserimento potrebbe modificare la validita di configurazioni gia registrate.

Ad esempio, se nel database sono gia presenti elementi montati nel 2026, l'inserimento successivo di un blocco animale con data di montaggio nel 2025 obbligherebbe il sistema a ricontrollare tutta la storia successiva della struttura. Questo renderebbe il vincolo piu difficile da implementare e da verificare, perche la correttezza non dipenderebbe solo dalla data del nuovo elemento, ma da tutti gli intervalli temporali che si sovrappongono.

## Scelta progettuale

Per semplificare il modello e mantenere il controllo piu chiaro, il progetto adotta una scelta greedy basata sulla recenza degli eventi strutturali.

La regola e:

```text
In una stessa struttura non e possibile inserire un nuovo blocco animale o una nuova cella idroponica con data di montaggio precedente alla data di montaggio piu recente gia registrata per quella struttura.
```

In questo modo gli eventi strutturali vengono registrati in ordine cronologico crescente.

## Perche e una scelta greedy

La scelta e greedy perche il sistema valuta la correttezza del nuovo inserimento rispetto allo stato piu recente gia registrato, senza ricalcolare tutte le possibili configurazioni storiche.

Quando viene inserito un nuovo elemento, il database controlla:

- qual e la data di montaggio piu recente gia presente nella stessa struttura;
- se la nuova data di montaggio e precedente a quella data;
- se la superficie disponibile alla nuova data e sufficiente.

Se la nuova data e piu vecchia dell'ultima registrata, l'inserimento viene rifiutato. Il sistema quindi non consente inserimenti retroattivi che potrebbero invalidare configurazioni successive.

Questa strategia non cerca di riorganizzare l'intera sequenza degli eventi, ma accetta solo il prossimo evento strutturale se e compatibile con lo stato corrente della struttura.

## Motivazione della scelta

La scelta greedy e motivata da tre esigenze.

Prima di tutto, riduce la complessita del controllo. Il database non deve riesaminare tutta la storia della struttura ogni volta che viene aggiunto un blocco o una cella.

In secondo luogo, rende piu semplice garantire la coerenza operativa. In un contesto ESA, gli eventi strutturali possono essere considerati registrazioni certificate: una volta registrata una modifica, non e ammesso inserire successivamente un evento precedente che alteri la sequenza storica.

Infine, rende piu comprensibile il vincolo dinamico. Il controllo puo essere spiegato come una politica operativa: le modifiche fisiche alla struttura vengono registrate nell'ordine in cui avvengono, evitando retrodatazioni.

## Applicazione al blocco animale

Nel trigger relativo a `BLOCCO_ANIMALE`, il controllo della recenza verifica che la nuova `DATA_MONTAGGIO` non sia precedente all'ultima data di montaggio registrata nella stessa struttura per un blocco animale o per una cella idroponica.

Se il vincolo non e rispettato, il trigger solleva un errore applicativo.

Il codice errore previsto nel glossario e:

```text
-20005 -- Inserimento di un elemento strutturale con data di montaggio precedente all'ultimo elemento inserito nella stessa struttura
```

## Controllo della superficie

Dopo aver imposto l'ordine cronologico degli inserimenti, il controllo della superficie diventa piu semplice.

Il sistema deve verificare la superficie occupata dagli elementi attivi alla data di montaggio del nuovo elemento:

- blocchi animali gia montati e non ancora smontati;
- celle idroponiche gia montate e non ancora smontate.

La superficie disponibile viene calcolata come:

```text
superficie disponibile =
superficie totale della struttura
- superficie dei blocchi animali attivi
- superficie delle celle idroponiche attive
```

Se la superficie del nuovo blocco animale supera la superficie disponibile, l'inserimento viene rifiutato.

## Assunzione tecnica

In questa documentazione il vincolo viene descritto dal punto di vista progettuale e concettuale.

Si assume quindi che il controllo venga valutato come vincolo dinamico del sistema. Eventuali dettagli tecnici specifici dell'ambiente Oracle, come le limitazioni dei trigger row-level quando leggono la stessa tabella che li attiva, sono considerati aspetti implementativi separati dalla scelta progettuale descritta.

## Vantaggi e limiti

Il vantaggio principale della scelta greedy e la semplicita: il vincolo e facile da spiegare, da testare e da collegare a una politica operativa realistica.

Il limite principale e che il sistema non permette inserimenti retroattivi. Questo significa che eventuali correzioni storiche dovrebbero essere gestite con procedure amministrative dedicate, non con il normale inserimento operativo.

Per il progetto d'esame questa scelta e accettabile perche rende esplicito il compromesso tra fedelta temporale completa e semplicita del vincolo dinamico.
