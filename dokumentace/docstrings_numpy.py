"""
Tento modul poskytuje jednoduchou demonstraci Docstringů v Pythonu.
Obsahuje třídu Kalkulacka s metodami pro základní matematické operace.
"""


class Kalkulacka:
    """
    Třída Kalkulacka nabízí základní matematické operace jako jsou sčítání a odečítání.

    Attributes
    ----------
    Neobsahuje žádné atributy.
    """

    def scitani(self, a: int, b: int) -> int:
        """
        Vrátí součet dvou celých čísel.
        """
        return a + b

    def nasobeni(self, a: int, b: int) -> int:
        """Vrátí násobek dvou celých čísel."""
        return a * b

    def odecitani(self, a: int, b: int) -> int:
        """
        Vrátí rozdíl dvou celých čísel.

        Parameters
        ----------
        a : int
            Menšenec.
        b : int
            Menšitel.

        Returns
        -------
        int
            Rozdíl `a` a `b`.
        """
        return a - b


instance_kalkulacky = Kalkulacka()
print(instance_kalkulacky.__doc__)
