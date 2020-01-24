"""
Assembles Model
"""

import iomb
import logging as log
from useeiopy.common import modulepath

#Turn on logging to see process in terminal
iomb.log_all(level=log.INFO)

"""
Class to extend iomb.model to give it a name and modelpath
"""
class Model(object):

    def __init__(self, iomb_model=iomb.model,
                 modelname=None, modelpath=None):
        self.model = iomb_model
        self.name = modelname
        self.path = modelpath

    def add_matrices(self):
        import iomb.matio as matio
        self.matrices = matio.Matrices(self.model,DQImatrices=True)
        return self


def make(modelname, modelpath):
    """
    Builds a Model
    :param modelname: str with model name
    :param modelpath: str with path
    :return: a useeiopy Model
    """
    drcfile = modelpath + modelname +"_DRC.csv"
    satfile = modelpath+modelname+"_sat.csv"
    sectormetafile = modelpath+modelname+'_sector_meta_data.csv'
    compartmentmetadatafile = modulepath + "data/USEEIO_compartment_meta_data.csv"
    lciafile = modelpath + modelname + "_LCIA.csv"
    #Build model
    iomb_model = iomb.make_model(drcfile,
                            [satfile],
                            sectormetafile,
                            compartments_csv=compartmentmetadatafile,
                            ia_tables=[lciafile])
    useeiopy_model = Model(iomb_model, modelname, modelpath)
    print("Model assembled.")
    return(useeiopy_model)
