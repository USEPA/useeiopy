#Performs validation on USEEIO form model

import iomb.validation as v

def validate(model):
    valid = v.validate(model)
    valid.display_count = -1
    f = open(model.path + model.name + '_validate.txt', 'w')
    f.write(valid.__str__())
    f.close()
