class Zvire:
    """Genericka trida pro obecne Zvire"""

    def __init__(self, jmeno: str, vek: int) -> None:
        """Inicializace zvirete"""
        self.jmeno: str = jmeno
        self.vek: int = vek
        self.hlad: int = 10  # Předpokládejme, že hodnota 10 značí maximální hlad

    def vydej_zvuk(self) -> None:
        """
        Rozhrani pro vydavani zvuku zvirete
        """
        pass

    def nakrm(self, potrava: int) -> None:
        self.hlad -= potrava
        if self.hlad < 0:
            self.hlad = 0

    def je_hladove(self) -> bool:
        return self.hlad > 0

    def kolik_je_hlad(self) -> int:
        return self.hlad


class Pes(Zvire):
    def __init__(self, jmeno: str, vek: int, plemeno: str) -> None:
        super().__init__(jmeno, vek)
        self.plemeno: str = plemeno

    def vydej_zvuk(self) -> None:
        print(f"{self.jmeno} říká haf!")

    def aportuj(self, predmet: str) -> None:
        print(f"{self.jmeno} aportuje {predmet}.")

    def chce_hrat(self) -> bool:
        return self.hlad < 5


class Kocka(Zvire):
    def __init__(self, jmeno: str, vek: int, barva_srsti: str) -> None:
        super().__init__(jmeno, vek)
        self.barva_srsti: str = barva_srsti

    def vydej_zvuk(self) -> None:
        print(f"{self.jmeno} říká mňau")

    def sleduj_svetlo(self) -> None:
        print(f"{self.jmeno} fascinovaně sleduje světlo.")

    def je_nalada_na_mazleni(self) -> bool:
        return self.hlad < 3


# Vytvoření instancí a testování
pes = Pes("Rex", 5, "Labrador")
kocka = Kocka("Mia", 3, "černobílá")

print(f"{pes.jmeno}, {pes.vek}-letý {pes.plemeno}, chce hrát:", pes.chce_hrat())
pes.nakrm(6)
print(f"Po krmení, {pes.jmeno} chce hrát:", pes.chce_hrat())

print(
    f"{kocka.jmeno}, {kocka.vek}-letá kočka s {kocka.barva_srsti} srstí, má náladu na mazlení:",
    kocka.je_nalada_na_mazleni(),
)
kocka.nakrm(8)
print(f"Po krmení, {kocka.jmeno} má náladu na mazlení:", kocka.je_nalada_na_mazleni())
