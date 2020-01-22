"""
A wrapper for the IO-Model-Builder for use with USEEIO family models.
Models are built from component pieces created by useeior
Functions are analagous to useeior with PEP names conventions

"""
import os
import useeiopy.build as build
import useeiopy.calculate as calculate
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
    #-2 = missing files ...abort
    case = check.look_for_model_files(modelname,modelpath)

    if case == 0:
        log.info("Assembling model...")
        model = build.make(modelname, modelpath)
        model = model.add_matrices()
        return(model)


def validate_EEIO_model(model):
    """
    Validates EEIO model
    :param model: A useeiopy Model object
    :return: None, writes validation out to file
    """
    import iomb.validation as v
    valid = v.validate(model.model)
    valid.display_count = -1
    f = open(model.path + model.name + '_validate.txt', 'w')
    f.write(valid.__str__())
    f.close()

def calculate_EEIO_model(model,
                         year=2012,
                         location='US',
                         demandtype='Production',
                         perspective='DIRECT',
                         include_data_quality=False):
    """
    Calculates LCI, LCIA and optionally DQI results for an identified demand vector
    present in the demand df identified by year, location and demandtype
    :param model: A useeiopy Model object
    :param year: int, year of demand
    :param location: string, location acronym of demand
    :param demandtype: string, either 'production' or 'consumption'
    :param perspective: string, either 'DIRECT' or 'INDIRECT'
    :return: A useeiopy Result object with LCI, LCIA and LCIA dataframes and metadata
    """

    result = calculate.calculate_EEIO_model(model, year, location,
                                            demandtype, perspective, include_data_quality)
    return result

def write_EEIO_result(result):
    """
    Writes out LCI, LCIA, and optionally DQI matrices to csv
    :param result: a useeiopy Result object
    :return: None
    """
    resultsfolder = result.path + "results/"
    if os.path.exists(resultsfolder) is False:
        os.mkdir(resultsfolder)
    result_pre = str(resultsfolder + result.modelname + "_" +
                 str(result.year) + "_" +
                 result.location + "_" +
                 result.demandtype + "_" +
                 result.perspective + "_")
    result.LCI.to_csv(result_pre + "LCI.csv")
    result.LCIA.to_csv(result_pre + "LCIA.csv")
    if result.DQI is not None:
        result.DQI.to_csv(result_pre + "DQI.csv")
    log.info("Wrote results files to " + resultsfolder)
