from ase.io import read
from pymatgen.io.ase import AseAtomsAdaptor
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.io.cif import CifWriter

# Read POSCAR / CONTCAR
atoms = read("CONTCAR")

# Convert ASE -> pymatgen
structure = AseAtomsAdaptor.get_structure(atoms)

# Analyze symmetry
sga = SpacegroupAnalyzer(structure, symprec=1e-5)
print("Space group:", sga.get_space_group_symbol(), sga.get_space_group_number())

# Get standardized conventional structure
conv = sga.get_conventional_standard_structure()

# Set Fe site occupancy to 0.5 (50%)
conv.replace_species({"Fe": {"Fe": 0.5}})

# Write CIF with symmetry information
writer = CifWriter(conv, symprec=1e-5)
writer.write_file("pos_sym.cif")
