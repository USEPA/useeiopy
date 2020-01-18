"""
Calculates results of a USEEIO form model; writes them to disk
"""
import iomb.demand2dict as dd
import iomb.calc as calc
import os

#Returns model calculation results for demand vector
def calculate (model,year,location,demandtype,perspective):

    demandfile = model.path + model.name + "_FinalDemand.csv"
    demandcolumnname = str(year) + '_' + location + "_" + demandtype
    demand = dd.demandtodict(demandcolumnname,demandfile)
    if (perspective=='FINAL'):
        p = calc.FINAL_PERSPECTIVE
    else:
        p = calc.DIRECT_PERSPECTIVE
    result = calc.calculate(model.model, demand, p)
    lciacontributions = result.lcia_contributions.transpose()
    lciaflowcontributions = result.lcia_flow_contributions.transpose()
    resultsfolder = model.path + "results/"
    if os.path.exists(resultsfolder) is False:
        os.mkdir(resultsfolder)
    lciacontributions.to_csv(resultsfolder+model.name+"_"+ str(year)+"_"+location+"_"+demandtype+"_"+perspective+"_"+"lciacontributions.csv")
    lciaflowcontributions.to_csv(resultsfolder+model.name+"_"+ str(year)+"_"+location+"_"+demandtype+"_"+perspective+"_"+"lciaflowcontributions.csv")