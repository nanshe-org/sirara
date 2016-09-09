import spams as _spams

from sirara import wrapper

trainDL = wrapper.factorizer(data_kw="X", num_atoms_kw="K", init_kw="D")(_spams.trainDL)
