import sys
from deformation_cube import box_lammps

if __name__ == '__main__':
    # relax_box_lammps(type_lattice, parameter_lattice, size, potential_file, mass_atom, temp, steps)
    box_lammps()
    sys.exit()