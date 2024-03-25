from dataclasses import dataclass


@dataclass
class Student:
   jmeno: str
   vek: int
   znamky: list[int]

   def __post_init__(self):
       if not self.jmeno.strip():
           raise ValueError("Jméno nemůže být prázdné nebo jen mezerou")
       if not (0 <= self.vek <= 120):
           raise ValueError("Věk musí být mezi 0 a 120")

# Správná data
student = Student(jmeno="Petr Novák", vek=20, znamky=[90, 85, 88])
print(student)

# Nesprávná data - toto vyvolá ValueError
try:
   nespravny_student = Student(jmeno=" ", vek=25, znamky=[105, 85, 90])
except ValueError as e:
   print(e)
