import os
import logging
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


requiredModelFileEndings = ['_DRC.csv',
                            '_MarketShares.csv',
                            '_sat.csv',
                            '_LCIA.csv',
                            '_sector_meta_data.csv',
                            '_FinalDemand.csv']

try: modulepath = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
except NameError: modulepath = 'useeiopy/'

modelbuildpath = modulepath + '/Model Builds/'
