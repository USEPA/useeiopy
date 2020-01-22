"""
Builds, validates, calculates and writes out results of an EEIO model
The EEIO model files must be predefined and in the appropriate model build folder
"""
import useeiopy

# Set the model name here that must be a predefined model with all model components present
modelname = "USEEIOv1.2-WASTE"

def main():
    model = useeiopy.build_EEIO_model(modelname)
    useeiopy.validate_EEIO_model(model)
    result = useeiopy.calculate_EEIO_model(model)
    useeiopy.write_EEIO_result(result)

if __name__ == '__main__':
    main()
