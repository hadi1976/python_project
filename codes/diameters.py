from config import*


class DiameterReader:
    """
    Author: Viviana Eloisa Quezada Dominguez
        The class 'DiameterReader' has the function to read the
        'EconomicDiameter' csv file. Making  it reusable for others
        water distribution designing codes.
    """

    def __init__(self, csv_file_name="EconomicDiameter.csv", delimiter=","):
        """
        param csv_file_name: csv file with the economic diameter and velocity
                                according to the flow discharge.
        param delimiter: separator in the csv file.
        """
        self.sep = delimiter
        self.size_diameter_velocity = csv_file_name
        self.read_diameter_data(csv_file_name)

    def read_diameter_data(self, csv_file_name):
        """
        Reading the csv file and creating a pandas dataframe.
        param: csv_file_name:csv file with the economic diameter and velocity
                            according to the flow discharge.
        """

        self.size_diameter_velocity = pd.read_csv(csv_file_name,
                                                  header=0,
                                                  sep=self.sep,
                                                  usecols=[0, 1, 2],
                                                  names=["Flow", "Diameter",
                                                         "Velocity"]
                                                  )

    def __call__(self, csv_file_name, *args, **kwargs):
        print()
    """
    It is used to make the object callable (as a function), 
    so if we have an instance x that defines __call__(self, csv_file_name) 
    we can do x(csv_file_name), which is actually a shortcut to 
    x.__call__ (csv_file_name).
    """