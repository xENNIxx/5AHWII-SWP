from model import Mitarbeiter, Abteilungsleiter, Abteilung, Firma


def create_data():
    it_mitarbeiter = [
        Mitarbeiter("Max", "Mustermann", False),
        Mitarbeiter("Julia", "Mustermann", True),
        Mitarbeiter("Dirk", "Mohle", False),
        Mitarbeiter("Anna", "Mohle", True),
    ]
    it_leitung = Abteilungsleiter("Hugo", "Dietz", False)
    it_abteilung = Abteilung("IT", it_mitarbeiter, it_leitung)

    marketing_mitarbeiter = [
        Mitarbeiter("Hans", "Moolmann", False),
        Mitarbeiter("Uwe", "Klump", True),
    ]
    marketing_leitung = Abteilungsleiter("Susi", "Sauer", True)
    marketing_abteilung = Abteilung(
        "Marketing", marketing_mitarbeiter, marketing_leitung
    )

    return Firma("Byton Software", [it_abteilung, marketing_abteilung])


def main():
    data = create_data()
    print(data)


if __name__ == "__main__":
    main()
