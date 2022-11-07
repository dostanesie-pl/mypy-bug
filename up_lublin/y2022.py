import typing
from uuid import UUID

from . import UniwersytetPrzyrodniczyWLublinie

MaturaResults = typing.Any


class Base(UniwersytetPrzyrodniczyWLublinie):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')
    year = 2022
    max_score = 600


class AnalitykaSrodowiskowaIPrzemyslowa(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class Agrobiznes(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class AktywnoscFizycznaIAgroturystykaKwalifikowana(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class AnalitykaWeterynaryjna(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')
    max_score = 400

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.biology * 1.0, matura_results.biology_advanced * 2.0),
            max([
                max(matura_results.chemistry * 1.0, matura_results.chemistry_advanced * 2.0),
                max([matura_results.physics_astronomy * 1.0, matura_results.physics_astronomy_advanced * 2.0,
                     matura_results.physics_advanced * 2.0]),
                max(matura_results.math * 1.0, matura_results.math_advanced * 2.0),
            ]),
        ])


class ArchitekturaKrajobrazu(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class BehawiorystykaZwierzat(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class BiobezpieczenstwoIZarzadzanieKryzysowe(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Bioinzynieria(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Biokosmetologia(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Biologia(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Biotechnologia(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class BezpieczenstwoIHigienaPracy(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class BezpieczenstwoICertyfikacjaZywnosci(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Dietetyka(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class EkologiaMiasta(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.history * 2.0, matura_results.history_advanced * 4.0),
                max(matura_results.history_of_art * 2.0, matura_results.history_of_art_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class Ekonomia(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.history * 2.0, matura_results.history_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class Ekoenergetyka(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.biology * 1.3, matura_results.biology_advanced * 2.0),
                max(matura_results.chemistry * 1.3, matura_results.chemistry_advanced * 2.0),
            ]),
        ])


class EnologiaICydrownictwo(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class GastronomiaISztukaKulinarna(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class GeodezjaIKartografia(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.biology * 1.3, matura_results.biology_advanced * 2.0),
                max(matura_results.chemistry * 1.3, matura_results.chemistry_advanced * 2.0),
            ]),
        ])


class GospodarkaPrzestrzenna(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class HipologiaIJezdziectwo(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class InzynieriaChemicznaIProcesowa(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class InzynieriaEkologiczna(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class InzynieriaRolniczaILesna(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class InzynieriaSrodowiska(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class KryminalistykaWBiogospodarce(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Lesnictwo(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class OchronaSrodowiska(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Ogrodnictwo(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class PielegnacjaZwietIAnimaloterapia(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class PszczelarstwoWAgroekosystemach(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Rolnictwo(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class SztukaOgrodowaIAranzacjeRoslinne(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class TechnikaRolniczaIAgrotronika(SztukaOgrodowaIAranzacjeRoslinne):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')


class TechnologiaBiosurowcowIBiomaterialow(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class TechnologiazywnosciIzywienieCzlowieka(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class TransportILogistyka(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0, matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class TurystykaIRekreacja(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.history * 2.0, matura_results.history_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
                max(matura_results.civics * 2.0, matura_results.civics_advanced * 4.0),
            ]),
        ])


class Weterynaria(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')
    max_score = 400

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.biology * 1.0, matura_results.biology_advanced * 2.0),
            max([
                max(matura_results.chemistry * 1, matura_results.chemistry_advanced * 2),
                max([matura_results.physics_astronomy * 1, matura_results.physics_astronomy_advanced * 2,
                     matura_results.physics_advanced * 2]),
                max(matura_results.math * 1, matura_results.math_advanced * 2),
            ]),
        ])


class ZarzadzanieIAdaptacjaDoZmianKlimatu(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0,
                     matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class ZarzadzanieIInzynieriaProdukcji(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0,
                     matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class ZielarstwoIFitoprodukty(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0,
                     matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])


class Zootechnika(Base):
    uuid = UUID('bbbbbbbb-aaaa-4444-bbbb-88888888888')

    def calculate(self, matura_results: MaturaResults) -> float:
        return sum([
            max(matura_results.any_foreign * 1.3, matura_results.any_foreign_advanced * 2.0),
            max([
                max(matura_results.biology * 2.0, matura_results.biology_advanced * 4.0),
                max(matura_results.chemistry * 2.0, matura_results.chemistry_advanced * 4.0),
                max([matura_results.physics_astronomy * 2.0,
                     matura_results.physics_astronomy_advanced * 4.0,
                     matura_results.physics_advanced * 4.0]),
                max(matura_results.geography * 2.0, matura_results.geography_advanced * 4.0),
                max(matura_results.informatics * 2.0, matura_results.informatics_advanced * 4.0),
                max(matura_results.math * 2.0, matura_results.math_advanced * 4.0),
            ]),
        ])
