from config import *
from diameters import DiameterReader


class TypeOfPipe:

    """
    Author: Viviana Eloisa Quezada Dominguez
    The class 'TypeOfPipe' has the function of dimensioning the pipes
    parameters that are needed for supplying the demand in a sewer system.
    """
    def __init__(self, flow_discharge, length):

        """
                param: flow_discharge: float of the flow discharge
                (daily or hourly) in (lit/sec).
                param: length: int of the pipe length in (m).

        """

        self.flow_discharge = float(flow_discharge)
        self.length = float(length)
        self.diameter = int  # Variable returned in (mm), by the method two.
        self.velocity = float  # Variable returned in (m/s), by the method two.

    def get_diameter_velocity_data(self):
        """
        This method is iterating over the 'EconomicDiameter' csv file, which
        is in the class 'DiameterReader'.

        param: economic_diameter_csv: Instantiation of the DiameterReader
        class.
        param: df: 'size_diameter_velocity" dataframe.
        param: self.diameter: int of the diameter in (mm) read from the
        'EconomicDiameters' csv.
        param: self.velocity: float of the velocity in (m/s) read from the
        'EconomicDiameters' csv.
        """
        # Instantiating DiameterReader class.
        economic_diameter_csv = DiameterReader()
        # Renaming the pandas dataframe "size_diameter_velocity" as "df".
        df = economic_diameter_csv.size_diameter_velocity
        # Iteration for finding the right diameter and velocity.
        for i in df.index:
            if self.flow_discharge <= df["Flow"][i]:
                self.diameter = df['Diameter'][i]
                self.velocity = df['Velocity'][i]
                break
            elif self.flow_discharge > df["Flow"][i]:
                self.diameter = 1000
                self.velocity = 1.75

        return self.diameter

    def pipe_dimensioning(self):
        """
        The main function of this method is to use best-fit diameter from the
        previous method. Using it for dimensioning a pipe.

        param: diam: int of 'self.diameter' in (mm).
        param: reynolds: float of the Reynolds Number in the pipe.
        param: friction: float of the friction coefficient in the pipe.
        param: slope: float of the pipe distance slope in (%).
        param: head_loss: float of the head losses of the pipe in (m).

        """
        diam = self.get_diameter_velocity_data()
        # Calculating Reynolds number of the pipe.
        reynolds = (1000 * ((self.flow_discharge / 1000) /
                            ((math.pi * (diam / 1000) ** 2) / 4))) / 0.0089

        # Calculating the friction factor of the pipe.
        friction = (1 / (-2 * math.log10(((0.0001 / (diam / 1000))
                                          / 3.715) + (15 / reynolds)))) ** 2

        # Calculating the slope of the distance traveled by the pipe.
        slope = friction * (((self.flow_discharge / 1000) /
                             ((math.pi * (diam / 1000) ** 2) / 4)) /
                            (2 * 9.82 * diam)) * 1000

        # Calculating the losses in the pipe.
        head_loss = (slope / self.length) * 1000

        # Parameters returned in a list format.
        return [reynolds, friction, slope, head_loss, self.diameter,
                self.velocity]
