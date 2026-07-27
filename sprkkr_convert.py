from ase.io import read
from ase2sprkkr.sprkkr.calculator import SPRKKR
from ase2sprkkr.input_parameters.input_parameters import InputParameters
from ase2sprkkr.sprkkr.sprkkr_atoms import SPRKKRAtoms

atoms = read("pos_sym.cif")
atoms = SPRKKRAtoms.promote_ase_atoms(atoms)

input_parameters = InputParameters.create('SCF')

#MODE 
input_parameters.MODE.MODE = 'SP-SREL'

#Energy Grid
input_parameters.ENERGY.NE = 32
input_parameters.ENERGY.GRID = 5
input_parameters.ENERGY.ImE = 0.00
input_parameters.ENERGY.EMIN = -0.2

#GRIDS
input_parameters.TAU.BZINT = 'POINTS'
input_parameters.TAU.NKTAB = 250

#SCF
input_parameters.SCF.VXC= 'PBE'
input_parameters.SCF.NITER = 500
input_parameters.SCF.MSPIN = {2.50, -2.50}
input_parameters.SCF.MIX = 0.20
input_parameters.SCF.TOL = 0.00001

#CONTROL
input_parameters.CONTROL.KRMT = 4
input_parameters.CONTROL.KRWS = 1
input_parameters.CONTROL.NOSYM = True

#CPA 
input_parameters.CPA.NITER = 1000
input_parameters.CPA.TOL = 0.00001 

calculator = SPRKKR(atoms=atoms, input_parameters=input_parameters)

calculator.save_input(input_file="struc_SCF.inp", potential_file="struc.pot")

print("Success! Generated both scf_run.inp and scf_run.pot perfectly.")

