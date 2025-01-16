############################################################## Dizionario libriBiblioteca ###########################################################################
libriBiblioteca = {
    "titolo0": {"autore": "autore0", "annoPubblicazione": "2000", "disponibile": False },
    "titolo1": {"autore": "autore1", "annoPubblicazione": "2001", "disponibile": True },
    "titolo2": {"autore": "autore2", "annoPubblicazione": "2002", "disponibile": False },
    "titolo3": {"autore": "autore3", "annoPubblicazione": "2003", "disponibile": True },
    "titolo4": {"autore": "autore4", "annoPubblicazione": "2004", "disponibile": True },
    "titolo5": {"autore": "autore5", "annoPubblicazione": "2005", "disponibile": True },
    "titolo6": {"autore": "autore6", "annoPubblicazione": "2006", "disponibile": True },
    "titolo7": {"autore": "autore7", "annoPubblicazione": "2007", "disponibile": False },
    "titolo8": {"autore": "autore8", "annoPubblicazione": "2008", "disponibile": False },
    "titolo9": {"autore": "autore9", "annoPubblicazione": "2009", "disponibile": False },
    "titolo10": {"autore": "autore10", "annoPubblicazione": "2010", "disponibile": False },
}
################################################################ Dizionario utentiBiblioteca #########################################################################


# Funzione Aggiungi libro  
def aggiungiLibro(titolo, autore, anno):
    for libro in libriBiblioteca:
        if libro == titolo:
            return ("Libro già presente")
        else:
            libriBiblioteca[titolo] = {"autore": autore , "annoPubblicazione": anno , "disponibile": True}
            return ("Libro aggiunto")

# Funzione rimuovi libro
def rimuoviLibro(titolo):
    if titolo in libriBiblioteca:
        del libriBiblioteca[titolo]
        return ("Libro rimosso")
    else:
        return ("Libro non trovato")
  
# Funzione cerca libro
def cercaLibro(titolo):   
    for libro in libriBiblioteca:
        if libro == titolo:
            autore = libriBiblioteca[libro]["autore"]
            annoPubblicazione = libriBiblioteca[libro]["annoPubblicazione"]
            disponibile = libriBiblioteca[libro]["disponibile"]
            if disponibile == True:
                disponibile = "Si"
            else:
                disponibile = "No"
            return "\nLibro trovato!!\n\nAutore: " + autore + "\nAnno di pubblicazione: " + annoPubblicazione + "\nDisponibile: " + str(disponibile)
    return ("Libro non trovato!!")

# Funzione prendere in prestito un libro
def prendiInPrestito(titolo):
    if titolo in libriBiblioteca:
        if libriBiblioteca[titolo]["disponibile"] == True:
            libriBiblioteca[titolo]["disponibile"] = False
            return ("Libro prenotato")
        else:
            return ("Libro non disponibile")

# Funzione restituire un libro
def restituisciLibro(titolo):
    if titolo in libriBiblioteca:
        if libriBiblioteca[titolo]["disponibile"] == False:
            libriBiblioteca[titolo]["disponibile"] = True
            return ("Libro restituito")
        else:
            return ("Libro già disponibile")
