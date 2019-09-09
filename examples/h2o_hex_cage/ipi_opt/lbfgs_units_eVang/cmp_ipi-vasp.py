#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib as mpl
mpl.use('agg')
import matplotlib.pyplot as plt

from ase.io import read

############################################################
# Load the data
############################################################
g_ipi = read('final.xyz')
g_vasp = read('../../opt_vasp/CONTCAR')

d0 = g_ipi.get_all_distances()[np.triu_indices(g_ipi.get_number_of_atoms(), k=1)]
d1 = g_vasp.get_all_distances()[np.triu_indices(g_ipi.get_number_of_atoms(), k=1)]
yx = np.linspace(d0.min(), d0.max(), 500)

fig = plt.figure(
    figsize=(3.6, 4.8)
)
# ax = plt.subplot()

import matplotlib.gridspec as gridspec

gs1 = gridspec.GridSpec(nrows=3, ncols=1,
                        left=None, right=None,
                        bottom=None, top=None,
                        wspace=None, hspace=None)
axes = [
        plt.subplot(gs1[:2]),
        plt.subplot(gs1[2]),
]

ax = axes[0]

ax.set_aspect(1.0)
ax.plot(d0, d1, ls='none', lw=0.8, color='k', ms=3.0,
        marker='h', mfc='r', mew=0.0, alpha=0.7)
ax.plot(yx, yx,
        ls='--', color='blue', lw=0.6,
        alpha=0.7)

# ax.set_xlim(0.0, 7.2)
# ax.set_ylim(0.0, 7.2)
# ax.set_xticks(np.arange(1.0, 7.2, 1.0))
# ax.set_yticks(np.arange(1.0, 7.2, 1.0))
ax.set_xlabel('Bond Length i-pi [$\AA$]', labelpad=5)
ax.set_ylabel('Bond Length VASP [$\AA$]', labelpad=5)

############################################################
ax = axes[1]
dd = d0 - d1
xx = np.arange(d0.size)

ax.vlines(xx[dd > 0], ymin=0, ymax=dd[dd > 0], lw=0.5, alpha=0.8)
ax.vlines(xx[dd < 0], ymax=0, ymin=dd[dd < 0], lw=0.5, alpha=0.8)

ax.set_ylabel('Bond Length Diff [$\AA$]', labelpad=5, fontsize='small')

for ax in axes:
    ax.grid('on', ls=':', lw=0.5)
############################################################
plt.tight_layout()
plt.savefig('kaka.png', dpi=300)
# plt.show()

from subprocess import call
call('feh -xdF kaka.png'.split())
