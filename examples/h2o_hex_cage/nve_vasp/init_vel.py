#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import ase
from ase.io import read, write
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# initial temperature
T = 300
# read in the initial structure
init_pos = read('init_pos.vasp')
# set the momenta corresponding to T = 300 K
MaxwellBoltzmannDistribution(init_pos, T * ase.units.kB)

# scale the temperature to T = 300K
vel = init_pos.get_velocities()
Tn = init_pos.get_temperature()
vel *= np.sqrt(T / Tn)
init_pos.set_velocities(vel)

# write the structure
write('POSCAR', init_pos, vasp5=True, direct=True)

# units in VASP and ASE are different
vel = init_pos.get_velocities() * ase.units.fs
np.savetxt('init_vel.dat', vel, fmt='%20.16f')
# append the velocities to the POSCAR
with open('POSCAR', 'a+') as pos:
    pos.write('\n')
    pos.write(
            '\n'.join([
                ''.join(["%20.16f" % x for x in row])
                for row in vel
               ])
            )
