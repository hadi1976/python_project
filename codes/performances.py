from flowrate_factors import max_daily_flow
from config import*

"""" Author: Viviana Eloisa Quezada Dominguez 
The script 'performances.py' has the function of evaluating the performances 
of the two pump capacities for the model 2009 1760 RPM and the model 8013 1760 
RPM. This evaluation is according to: elevation (m) and flow discharge 
(lit/sec). """

with open(user_elevation) as file:
    user_elevation = int(file.read())

flow_discharge = max_daily_flow()  # Output: flow_discharge.
# Constant parameters of the pumps capacity performance.
pump_one_elevation = [13, 15, 17, 23, 28]
max_elevation_one = max(pump_one_elevation)
pump_one_flow = [12.5, 14, 15, 16, 17.5]
max_flow_one = max(pump_one_flow)

pump_two_elevation = [22, 29, 35, 43, 55]
max_elevation_two = max(pump_two_elevation)
pump_two_flow = [155, 205, 240, 255, 270]
max_flow_two = max(pump_two_flow)


def pump_one_performance():
    """
    param: user_elevation: float of the elevation of the town in m.
    param: flow_discharge: float of the flow discharge in lit/sec.
    param: pump_one_elevation: int of the elevations of the pump one (m)
                                regarding flow discharge (lit/sec).
    param: pump_one_flow: int of the flow discharge of the pump one (lit/sec)
                          regarding elevations (m).
    param: max_elevation_one: int of the maximal elevation reached by pump one
    (m).
    param: max_flow_one: int of the maximal flow discharge reached by pump one
     (lit/sec).

    """
    # Verifying that user inputs demand, can be supplied with the pump one.
    if user_elevation <= pump_one_elevation[-1] and flow_discharge <= \
            pump_one_flow[-1]:
        # Iterating for finding the best-fit performance curve.
        i = 1
        for i in range(len(pump_one_elevation)):
            if user_elevation < pump_one_elevation[i]:
                break
        j = 1
        for j in range(len(pump_one_flow)):
            if flow_discharge < pump_one_flow[j]:
                break
        y = max(i, j)
        # Returning the elevation of the best-fits performing curve.
        return pump_one_elevation[y]


def pump_two_performance():

    """
    param: pump_two_elevation: int of the elevations of the pump two (m)
     regarding flow discharge (lit/sec).
    param: pump_two_flow: int of the flow discharge of the pump two (lit/sec)
                          regarding elevations (m).
    param: max_elevation_two: int of the maximal elevation reached by pump
    two (m).
    param: max_flow_two: int of the maximal flow discharge reached by pump
    two (lit/sec).
    """
    # Verifying that user inputs demand, can be supplied with the pump two.
    if user_elevation <= pump_two_elevation[-1] and flow_discharge <= \
            pump_two_flow[-1]:
        # Iterating for finding the best-fit performance curve.
        i = 1
        for i in range(len(pump_two_elevation)):
            if user_elevation < pump_two_elevation[i]:
                break
        j = 1
        for j in range(len(pump_two_flow)):
            if flow_discharge < pump_two_flow[j]:
                break
        y = max(i, j)
        # Returning the elevation of the best-fits performing curve.
        return pump_two_elevation[y]