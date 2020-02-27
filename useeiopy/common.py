import os
import logging
import appdirs

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


requiredModelFileEndings = ['_DRC.csv',
                            '_sat.csv',
                            '_LCIA.csv',
                            '_sector_meta_data.csv',
                            '_FinalDemand.csv']

try: modulepath = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/') + '/'
except NameError: modulepath = 'useeiopy/'

modelbuildpath = appdirs.user_data_dir()
modelbuildpath = modelbuildpath + '/USEEIO/Model_Builds'
modelbuildpath = os.path.realpath(modelbuildpath)