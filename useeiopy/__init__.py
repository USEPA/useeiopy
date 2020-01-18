"""
A wrapper for the IO-Model-Builder for use with USEEIO family models
"""

import useeiopy.AssembleModel as AssembleModel
import useeiopy.CalculateModel as CalculateModel
import useeiopy.ValidateModel as ValidateModel
import useeiopy.check as check
from useeiopy.common import modelbuildpath, log

def assemble(inputmodelname):
    """Assembles a USEEIO model as an iomb Model instance
    Determines status of current builds as a case, finds or create missing files to proeeed to the next step
    :param inputmodelname: full model name, e.g. 'USEEIOv1.1'
    :return: an useeiopy Model instance
    """
    modelname = inputmodelname
    modelpath = modelbuildpath + modelname + '/'

    #status code
    #0  = all files present .. proceed with assembly
    #-2 = missing other files ...abort
    case = check.look_for_model_files(modelname,modelpath)

    if case == 0:
        log.info("Assembling model...")
        model = AssembleModel.make(modelname, modelpath)
        return(model)

def validate(model):
    ValidateModel.validate(model)

def calculate(model,year=2007,location='US',demandtype='Consumption',perspective='DIRECT'):
    CalculateModel.calculate(model,
                             year,
                             location,
                             demandtype,
                             perspective)
    log.info("Wrote results files to model's results folder.")

