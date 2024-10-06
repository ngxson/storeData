def est_adn(string):
    for c in string:
        if c != "A" and c != "T" and c != "C" and c != "G":
            return 0
    return 1


#print(est_adn("AGTCTTTX"))

def demander_adn():
    adn = input("Entrez ADN: ")
    if est_adn(adn):
        print("Longueur: " + str(len(adn)))
        return adn
    else:
        return demander_adn()


print(demander_adn())
