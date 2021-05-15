import numpy as np
from nefertiti.protocols.kbest import kbest_backbone_rmsd

import logging
logging.basicConfig()
logging.getLogger("nefertiti").setLevel(logging.INFO)

fraglib = np.load("../fraglib/dummy.npy")
refe = open("1AVXA-unbound-heavy.pdb").read()
#refe = "\n".join(refe.splitlines()[:143])  # 20 residues, 9min15s  1.24213513 A
refe = "\n".join(refe.splitlines()[1009:1152]) #20 residues, 2m1s 1.1878649 A  

k = 1
main_state = kbest_backbone_rmsd(
    refe, fraglib,
    format="pdb",
    k=k
)
natoms = main_state.refe.nfrags * main_state.refe.fraglen * len(main_state.refe.bb_atoms)
traj = main_state.stages[-1].trajectories[:k]
np.save("kbest-test-traj.npy", traj)
scores = main_state.stages[-1].scores[:k]
rmsd = np.sqrt(scores/natoms)
np.save("kbest-test-rmsd.npy", rmsd)
print(rmsd[:30])