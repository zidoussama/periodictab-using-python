import periodictable

atom = int(input("Enter atomic number: "))

elem= periodictable.elements[atom]
print(f"Element: {elem.name}")
print(f"Symbol: {elem.symbol}")
print(f"Atomic Number: {elem.number}")
print(f"Atomic Mass: {elem.mass}")
print(f"Density: {elem.density}")