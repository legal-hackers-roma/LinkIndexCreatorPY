# LinkIndexCreatorPy

Linguaggio: Python

## Descrizione

Si tratta di un semplice tool per creare un **indice ipertestuale degli atti e dei documenti di un fascicolo**

Il Programma provvede a:

- individuare i file contenuti in una cartella (che dovrà essere indicata come paramentro del comando di start);
- verificare che si tratti di file permessi;
- creare un indice ipertestuale in HTML;
- convertire l'indice in formato PDF (funzionalità da testare)

## Installazione

1. Clonare il repository
2. Creare un ambiente virtuale con `python -m venv v_env`
3. avviare l'ambiente virtuale
4. installare le dipendenze contenute nel file `requirements.txt` e anche Pango (per weasyprint)
3. Digitare ``python3 index.py "[path-to-folder]" "[nome-cognome-avvocato]"`` (es. ``python3 "/Users/Tizio/Documents/TEST_CARTELLA" "Mario Rossi"``)
