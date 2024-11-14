import sys
from lammps_methods import relax_box_lammps

if __name__ == '__main__':
    # relax_box_lammps(type_lattice, parameter_lattice, size, potential_file, mass_atom, temp, steps)
    relax_box_lammps("fcc", 3.615, 10, "Cu_u3.eam", 63.546,
                     100, 5000)
    sys.exit()