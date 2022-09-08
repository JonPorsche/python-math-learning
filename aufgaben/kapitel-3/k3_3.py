kredit = int(input("Kreditbetrag: "))
m_rate = int(input("Monatliche Rate: "))
zinssatz = float(input("Zinssatz in %: ")) / 100


def tilgungsVerlauf(kredit, m_rate, zinssatz):
    while kredit > 0:
        print(round(kredit, 2), " €")
        zinsen = kredit * zinssatz
        kredit = kredit + zinsen - m_rate


tilgungsVerlauf(kredit, m_rate, zinssatz)
