from lammps import lammps


def relax_box_lammps(type_lattice, parameter_lattice, size, potential_file, mass_atom, temp, steps):
    lmp = lammps(cmdargs=["-echo", "both"])

    lmp.commands_string(f"""
    units metal
    dimension 3
    boundary p p p
    atom_style atomic

    lattice {type_lattice} {parameter_lattice}
    region box block 0 {size} 0 {size} 0 {size}
    create_box 1 box
    create_atoms 1 box

    pair_style eam
    pair_coeff * * {potential_file}

    mass 1 {mass_atom}
    velocity all create {temp} 12345 mom yes rot yes

    fix 1 all nvt temp {temp} {temp} 0.05 
    thermo 1000  
    thermo_style custom step temp etotal pe press vol  
    timestep 0.001
    run {steps} 
    write_restart relaxed_box.restart 
    """)

    lmp.close()