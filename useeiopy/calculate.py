"""
Calculates results of a USEEIO model
"""
import iomb.demand2dict as dd
import iomb.calc as calc
from useeiopy.common import log
from useeiopy.build import Model


class Result(object):
    """
    Extends the iomb result object to add metadata
    """
    def __init__(self,
                 iomb_result=calc.Result,
                 model=Model,
                 location=None,
                 demandtype=None,
                 perspective=None,
                 year=None,
                 include_data_quality=False):

        self.modelname = model.name
        self.path = model.path
        self.location = location
        self.demandtype = demandtype
        self.perspective = perspective
        self.year = year

        #Write all results to
        result_types = ['LCI_d','LCI_f','LCIA_d','LCIA_f']
        try:
           self.LCI = iomb_result['LCI_d']
        except KeyError:
            # Do nothing
            a=1
        try:
            self.LCI = iomb_result['LCI_f']
        except KeyError:
            # Do nothing
            a=1
        try:
            self.LCIA = iomb_result['LCIA_d']
        except KeyError:
            # Do nothing
            a=1
        try:
            self.LCIA = iomb_result['LCIA_f']
        except KeyError:
            # Do nothing
            a=1

        if include_data_quality:
            import iomb.matio as matio
            lci_contrib = self.LCI.transpose().values
            dqi_contributions = model.matrices.B_dqi.aggregate_mmult(model.matrices.C.values,
                                                            lci_contrib,
                                                            left=False)
            dqi_df = matio.dqi_matrix_to_df(dqi_contributions, model.matrices.C.index,
                                              model.matrices.A.index)
            dqi_df = dqi_df.transpose()
            self.DQI = dqi_df


def calculate_EEIO_model(model, year, location,
                         demandtype, perspective, include_data_quality):
    """
    Calculates an EEIO model result
    :param model: A useeopy Model object
    :param year: int, year of demand
    :param location: string, location acronym of demand
    :param demandtype: string, either 'production' or 'consumption'
    :param perspective: string, either 'DIRECT' or 'INDIRECT'
    :return: A useeiopy Result object
    """
    result = {}
    demandfile = model.path + model.name + "_FinalDemand.csv"
    demandcolumnname = str(year) + '_' + location + "_" + demandtype
    demand = dd.demandtodict(demandcolumnname,demandfile)
    if (perspective=='FINAL'):
        p = calc.FINAL_PERSPECTIVE
        r = calc.calculate(model.model, demand, p)
        result['LCI_f'] = r.lci_contributions.transpose()
        result['LCIA_f'] = r.lcia_contributions.transpose()
    elif (perspective=='DIRECT'):
        p = calc.DIRECT_PERSPECTIVE
        r = calc.calculate(model.model, demand, p)
        result['LCI_d'] = r.lci_contributions.transpose()
        result['LCIA_d'] = r.lcia_contributions.transpose()
    else:
        log.error('Perspective must be DIRECT or FINAL.')
    new_result = Result(result,model,location,demandtype,perspective,year,include_data_quality)


    return new_result








