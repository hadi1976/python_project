from typing import TextIO
from pipes import TypeOfPipe
import flowrate_factors
import performances
import plots
from config import *

"""
Author: Viviana Eloisa Quezada Dominguez
Author: Seyedhadi Hashemi

The script "main.py" has the function of integrating the outputs from all 
the codes, through the implementation of functions. These functions are going 
to be called in the "GUI.py" code.

"""

"""
First part of the code: Integrating  "flowrate_factors" outputs through 
functions, for be referenced in the  GUI.
"""


def consumption():
    """
    :return: int of the consumption depending on the selected country in
    (lit/sec.Capita).
    """
    country_consumption = flowrate_factors.get_flow_discharge()
    return country_consumption


def hourly():
    """
    :return: float of the flow discharge per hour in (lit/hour).
    """
    flow_hourly = flowrate_factors.max_hourly_flow()
    return "%.2f" % flow_hourly


def daily():
    """
    :return: float of the flow discharge per day in (lit/day).
    """
    flow_daily = flowrate_factors.max_daily_flow()
    return "%.2f" % flow_daily


"""
Second part of the code: Instantiating the objects from the TypeOfPipe class.
And, integrating this class outputs through functions, to be called in the GUI.
"""
# Reading the length, inputted by the user, from the GUI.
with open(transmission_pipe_length) as file:
    transmission_pipe_length = float(file.read())

# Instantiating transmission_pipeline as an object from 'TypeOfPipe' class.
transmission_pipeline = TypeOfPipe(flowrate_factors.max_daily_flow(),
                                   transmission_pipe_length)

# Reading the length, inputted by the user, from the GUI.
with open(distribution_pipe_length) as file:
    distribution_pipe_length = float(file.read())
# Instantiating distribution_pipeline as an object from 'TypeOfPipe' class.
distribution_pipeline = TypeOfPipe(flowrate_factors.max_hourly_flow(),
                                   distribution_pipe_length)
# Referencing the method 'pipe_dimensioning' from 'TypeOfPipe' class.
transmission_dim = transmission_pipeline.pipe_dimensioning()
distribution_dim = distribution_pipeline.pipe_dimensioning()


# Integrating the pipes dimensions, for be referenced in the GUI.

def diameter_transmission():
    """
    :return: int of the diameter of the transmission pipeline in (mm).
    """
    return str(transmission_dim[4])


def velocity_transmission():
    """
    :return: float of the velocity of the transmission pipeline in (m/s).
    """
    return str(transmission_dim[5])


def reynolds_transmission():
    """
    :return: float of the reynolds number of the transmission pipeline.
    """
    return "%.2f" % transmission_dim[0]


def friction_transmission():
    """
    :return: float of the friction factor of the transmission pipeline.
    """
    return "%.2f" % transmission_dim[1]


def slope_transmission():
    """
    :return: float of the slope of the transmission pipeline in (%).
    """
    return "%.5f" % transmission_dim[2]


def loss_transmission():
    """

    :return: float of the head loss of the transmission pipeline in (m).
    """
    return "%.5f" % transmission_dim[3]


def diameter_distribution():
    """
    :return:  int of the diameter of the distribution pipeline in (mm).
    """
    return str(distribution_dim[4])


def velocity_distribution():
    """
    :return: float of te velocity of the distribution pipeline in (m/s).
    """
    return str(distribution_dim[5])


def reynolds_distribution():
    """
    :return: float of the reynolds number of the distribution pipeline.
    """
    return "%.2f" % distribution_dim[0]


def friction_distribution():
    """
    :return: float of the friction factor of the distribution pipeline.
    """
    return "%.2f" % distribution_dim[1]


def slope_distribution():
    """
    :return: float of the slope of the distribution pipeline in (%).
    """
    return "%.5f" % distribution_dim[2]


def head_distribution():
    """

    :return: float of the head loss of the distribution pipeline in (m).
    """
    return "%.5f" % distribution_dim[3]


"""
Third part of the code: Pumps "Model 2009 1760 RPM" performances graphs:
basic, parallel arrangement, series arrangement and combined arrangement.
 Also, the theoretical explanation for the user, about what can be seen in the
 plot. This two functions will be called in the GUI.
"""


# Conditions for pump one model 2009 1760 RPM curves performance.
with open(user_elevation) as file:
    elevation = float(file.read())


def plot():
    """

    :return: The plot according thar corresponds to the user input and the
    fulfillment with the if/elif statements.
    """
    # Conditions for pump one model 2009 1760 RPM curves performance.
    if performances.max_elevation_one >= elevation > 0 and \
            performances.max_flow_one >= performances.flow_discharge > 0:
        return plots.plot_one()

    # Conditions for pump two model 8013 1760 RPM curves performance.
    elif performances.max_elevation_two >= elevation > 0 and \
            performances.flow_discharge <= performances.max_flow_two:
        return plots.plot_two()

    # Conditions for pump two model 8013 1760 RPM parallel curves performance.
    elif performances.user_elevation > performances.max_elevation_two and \
            float(performances.flow_discharge) < \
            float(performances.max_flow_two) and\
            performances.user_elevation > 0:
        return plots.plot_three()

    # Conditions for pump two model 8013 1760 RPM curves performance in series.
    elif performances.max_elevation_two > elevation > 0 and \
            performances.flow_discharge > performances.max_flow_two:
        return plots.plot_four()

    # Conditions for pump two model 8013 1760 RPM curves performance combined.
    elif performances.user_elevation > performances.max_elevation_two and \
            performances.flow_discharge > performances.max_flow_two and \
            performances.user_elevation > 0:
        return plots.plot_five()


def explanation():
    """

    :return: The explanation of the plot according thar corresponds to the
    user input and the fulfillment with the if/elif statements.
    """
    # Conditions for pump one model 2009 1760 RPM curves performance.
    if performances.max_elevation_one >= elevation > 0 and \
            performances.max_flow_one >= performances.flow_discharge > 0:
        return ("For an elevation of %d m and flow discharge of %d lit/sec,"
                "is needed one pump of Model 2009 1760 RPM, with the "
                "performance shown in the graph."
                % (performances.user_elevation, performances.flow_discharge))

    # Conditions for pump two model 8013 1760 RPM curves performance.
    elif performances.max_elevation_two >= elevation > 0 and \
            performances.flow_discharge <= performances.max_flow_two:
        return (
                "For an elevation of %d m and flow discharge of %d, "
                "is needed one pump of Model 8013 1760 RPM, with the "
                "performance shown in the graph."
                % (performances.user_elevation,
                   performances.flow_discharge))

    # Conditions pump two model 8013 1760 RPM curves performance in parallel.
    elif performances.user_elevation > performances.max_elevation_two and \
            float(performances.flow_discharge) \
            < float(performances.max_flow_two) and \
            performances.user_elevation > 0:
        x = 1
        for x in range(100000):
            #  Breaks when arranged pumps elevation is higher than user one.
            if (
                    x * performances.max_elevation_two) > \
                    performances.user_elevation:
                break
        return (
                "For an elevation of %d m and flow discharge of %d lit/sec, "
                "in the Model 8013 1760 RPM, %d pumps has to be arranged in"
                " parallel, in order to supply the demand. Please observe the "
                "graph shown for a better understanding."
                % (performances.user_elevation,
                   performances.flow_discharge, x))

    # Conditions for pump two model 8013 1760 RPM curves performance in series.
    elif performances.max_elevation_two > elevation > 0 and \
            performances.flow_discharge > performances.max_flow_two:
        x = 1
        for x in range(100000):
            #  Breaks when arranged pumps flow is higher than the user one.
            if (x * performances.max_flow_two) > performances.flow_discharge:
                break
        return ("For an elevation of %d m and flow discharge of %d lit/sec, "
                "in the Model 8013 1760 RPM, %d pumps has to be arranged in "
                "series, in order to supply the demand. Please observe the "
                "graph shown for a better understanding."
                % (performances.user_elevation,
                   performances.flow_discharge, x))

    # Conditions for pump two model 8013 1760 RPM curves performance combined.
    elif performances.user_elevation > performances.max_elevation_two and \
            performances.flow_discharge > performances.max_flow_two and \
            performances.user_elevation > 0:
        x = 1
        z = 1
        # Iterating for finding the amount un pumps arranged in parallel.
        for x in range(100000):
            #  Breaks when arranged pumps elevation is higher than user one.
            if (
                    x * performances.max_elevation_two) > \
                    performances.user_elevation:
                break
        for z in range(100000):
            #  Breaks when arranged pumps flow is higher than the user one.
            if (z * performances.max_flow_two) > performances.flow_discharge:
                break
        return ("For an elevation of %d m and flow discharge of %d lit/sec, "
                "in the Model 8013 1760 RPM, %d pumps has to be arranged in "
                "parallel with %d series stages, in order to supply the "
                "demand. "
                "Please observe the graph "
                "shown for a better understanding."
                % (performances.user_elevation, performances.flow_discharge,
                   x, z))
