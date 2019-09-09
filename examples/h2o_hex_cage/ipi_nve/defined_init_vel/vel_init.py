#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import ase
from ase.io import read, write


# initial velocities in units of Ang / fs
vel = np.loadtxt('init_vel.dat')
# # change to Bohr / Aut
vel /= (ase.units.Bohr / (ase.units._aut * 1E15))
# change to m / s
# vel *= 1E5

np.savetxt('init_vel_au.dat', vel, fmt='%20.8E', newline=',\n', delimiter=',')

xx = read('init_pos.xyz')
xx.set_positions(vel)
write('init_vel.xyz', xx)
