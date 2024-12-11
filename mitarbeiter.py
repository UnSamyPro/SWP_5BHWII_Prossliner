
class Person:
    def __init__(self, first_name: str, last_name: str, gender: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, first_name: str, last_name: str, gender: bool):
        super().__init__(first_name, last_name, gender)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, first_name: str, last_name: str, gender: bool):
        super().__init__(first_name, last_name, gender)


class Abteilung:
    def __init__(self, name: str, leiter: Abteilungsleiter):
        self.name = name
        self.leiter = leiter
        self.mitarbeitende: list[Mitarbeiter] = [leiter]

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.mitarbeitende.append(mitarbeiter)

    def count_mitarbeiter(self):
        return len(self.mitarbeitende)

    def count_males(self):
        return sum([1 for mitarbeiter in self.mitarbeitende if mitarbeiter.gender is True])

    def count_females(self):
        return sum([1 for mitarbeiter in self.mitarbeitende if mitarbeiter.gender is False])


class Firma:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen: list[Abteilung] = []

    def add_abteilung(self, abteilung: Abteilung):
        self.abteilungen.append(abteilung)

    def count_mitarbeiter(self):
        return sum([abteilung.count_mitarbeiter() for abteilung in self.abteilungen])

    def count_abteilungen(self):
        return len(self.abteilungen)

    def count_abteilungsleiter(self):
        return len([abteilung.leiter for abteilung in self.abteilungen])

    def biggest_abteilung(self):
        return max(self.abteilungen, key=lambda abteilung: abteilung.count_mitarbeiter())

    def count_males(self):
        return sum([abteilung.count_males() for abteilung in self.abteilungen])

    def count_females(self):
        return sum([abteilung.count_females() for abteilung in self.abteilungen])

    def gender_distribution(self):
        return {
            "m": (self.count_males() / self.count_mitarbeiter()) * 100,
            "f": (self.count_females() / self.count_mitarbeiter()) * 100,
        }


def main():
    firma = Firma("Firma")

    abteilung1 = Abteilung("Produktentwicklung", Abteilungsleiter("Max", "Mustermann", True))
    abteilung1.add_mitarbeiter(Mitarbeiter("Hans", "Müller", True))
    abteilung1.add_mitarbeiter(Mitarbeiter("Peter", "Meier", True))
    abteilung1.add_mitarbeiter(Mitarbeiter("Anna", "Schmidt", False))
    abteilung1.add_mitarbeiter(Mitarbeiter("Lisa", "Schneider", False))

    abteilung2 = Abteilung("Buchhaltung", Abteilungsleiter("Max", "Mustermann", True))
    abteilung2.add_mitarbeiter(Mitarbeiter("Andreas", "Heinz", True))
    abteilung2.add_mitarbeiter(Mitarbeiter("Klaus", "Schmidt", True))
    abteilung2.add_mitarbeiter(Mitarbeiter("Maria", "Schneider", False))
    abteilung2.add_mitarbeiter(Mitarbeiter("Elisa", "Schnitz", False))
    abteilung2.add_mitarbeiter(Mitarbeiter("Liane", "Schwartz", False))

    firma.add_abteilung(abteilung1)
    firma.add_abteilung(abteilung2)

    print("count_mitarbeiter:", firma.count_mitarbeiter())
    print("count_abteilungen:", firma.count_abteilungen())
    print("count_abteilungsleiter:", firma.count_abteilungsleiter())
    print("biggest_abteilung:", firma.biggest_abteilung().name)
    print("count_males:", firma.count_males())
    print("count_females:", firma.count_females())
    print("gender_distribution:", firma.gender_distribution())


if __name__ == "__main__":
    main()
