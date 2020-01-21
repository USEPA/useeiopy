"""
A wrapper for the IO-Model-Builder for use with USEEIO family models
"""
import os
import useeiopy.build as build
import useeiopy.calculate as calculate
import useeiopy.ValidateModel as ValidateModel
import useeiopy.check as check
from useeiopy.common import modelbuildpath, log

def build_EEIO_model(inputmodelname):
    """Assembles a USEEIO model as an iomb Model instance
    Determines status of current builds as a case, finds or create missing files to proeeed to the next step
    :param inputmodelname: full model name, e.g. 'USEEIOv1.1'
    :return: an useeiopy Model instance
    """
    modelname = inputmodelname
    modelpath = modelbuildpath + '/' + modelname + '/'

    #status code
    #0  = all files present .. proceed with assembly
    #-2 = missing other files ...abort
    case = check.look_for_model_files(modelname,modelpath)

    if case == 0:
        log.info("Assembling model...")
        model = build.make(modelname, modelpath)
        return(model)

def validate(model):
    ValidateModel.validate(model)

def calculate_EEIO_model(model,year=2007,location='US',demandtype='Consumption',perspective='DIRECT'):
    result = calculate.calculate_EEIO_model(model,
                             year,
                             location,
                             demandtype,
                             perspective)
    return result

def write_EEIO_result(result):
    resultsfolder = result.path + "results/"
    if os.path.exists(resultsfolder) is False:
        os.mkdir(resultsfolder)
    result.LCI.to_csv(resultsfolder+result.modelname+"_"+ str(result.year)+"_"+result.location+"_"+result.demandtype+"_"+result.perspective+"_"+"LCI.csv")
    result.LCIA.to_csv(resultsfolder+result.modelname+"_"+ str(result.year)+"_"+result.location+"_"+result.demandtype+"_"+result.perspective+"_"+"LCIA.csv")
    log.info("Wrote results files to " + resultsfolder)
