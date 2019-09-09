#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt

ipi_md = np.loadtxt('nve.prp')
vasp_md = np.loadtxt('../../nve_vasp/.vasp_md.dat')

init_temp_diff = ipi_md[0,2] - vasp_md[0,1]

fig = plt.figure(
    figsize=(4.8, 3.0)
)
ax = plt.subplot()

ax.plot(ipi_md[:,1], ipi_md[:,2], ls='-', lw=0.8, color='k', ms=2.5,
        marker='h', mfc='k', mew=0.0, alpha=0.7)
ax.plot(vasp_md[:,0]*0.5, vasp_md[:,1],
        ls='-', color='blue', lw=1.0,
        alpha=0.8)
ax.plot(ipi_md[:,1], ipi_md[:,2] - init_temp_diff,
        ls='--', color='r', lw=1.0,
        alpha=0.8)

ax.axhline(y=150, lw=1.0, ls=':', color='k', alpha=0.8)

ax.legend(ax.get_lines(), ['i-pi MD', 'VASP MD', 'i-pi MD shifted'],
          loc='upper right', 
          fontsize='small',
          frameon=True,
          framealpha=0.7,)

ax.set_xlabel('Time [fs]', labelpad=5)
ax.set_ylabel('Temperature [K]', labelpad=5)

ax.grid('on', ls=':', lw=0.5)
ax.minorticks_on()

plt.tight_layout()
plt.savefig('cmp_T.png', dpi=300)
# plt.show()

from subprocess import call
call('feh -xdF cmp_T.png'.split())
