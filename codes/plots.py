from config import *
import performances
import pumps_figure
"""
Author: Viviana Eloisa Quezada Dominguez
The script "plots" as its name says, has the function of process the data input 
by the user, as the outputs from files as: "flowrate_factors", "pumps_figure", 
and "performances", in order to elaborate the graph according to the 
established conditions.
"""


def plot_one():
    """
    This function plots the pump one performance curves according to the
    best-fit elevation with the user input. Also, prints the pump model
    according to the elevation and flow discharge.

    param: a: int of the best-fit elevation in (m).

    :return: The best-fit plot for the pump one, according to the user inputs.
    """

    # a is the int of the return from the function 'pump_one_performance' from
    # the file 'performances.py'. This elevation is in (m).
    a = performances.pump_one_performance()

    # Conditions for finding the best-fit curve performance and plot it.
    if a == 13:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate1.flow_range(),
                 pumps_figure.Pump1.head_formula(),
                 label="1.5HP(1.1kw)")
    elif a == 15:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate2.flow_range(),
                 pumps_figure.Pump2.head_formula(),
                 label="2HP(1.5kw)")
    elif a == 17:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate3.flow_range(),
                 pumps_figure.Pump3.head_formula(),
                 label="3HP(2.2kw)")
    elif a == 23:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate4.flow_range(),
                 pumps_figure.Pump4.head_formula(),
                 label="5HP(3.6kw)")
    elif a == 28:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate5.flow_range(),
                 pumps_figure.Pump5.head_formula(),
                 label="7.5HP(5.6kw)")

    # Plotting legend specifications.
    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 2009 1760 RPM")
    plt.savefig("pump3.png")
    plt.show()


def plot_two():
    """
    This function plots the pump two, performances curves according to the
    best-fit elevation with the user input. Also, prints the pump model
    according to the elevation and flow discharge.

     param: b: int of the best-fit elevation in (m).

    :return: The best-fit plot for the pump two, according to the user inputs.
    """
    # b is the int of the return from the function 'pump_two_performance'
    # from the file 'performances.py'. This elevation is in (m).
    b = performances.pump_two_performance()
    # Conditions for finding the best-fit curve performance and plot it.
    if b == 22:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate2_1.flow_range(),
                 pumps_figure.Pump2_1.head_formula(),
                 label="60HP(44kw)")
    elif b == 29:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate2_2.flow_range(),
                 pumps_figure.Pump2_2.head_formula(),
                 label="75HP(56kw)")
    elif b == 35:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate2_3.flow_range(),
                 pumps_figure.Pump2_3.head_formula(),
                 label="100HP(74.5kw)")
    elif b == 43:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate2_4.flow_range(),
                 pumps_figure.Pump2_4.head_formula(),
                 label="125HP(93.2kw)")
    elif b == 55:
        plt.figure(num=None, dpi=120)
        plt.plot(pumps_figure.flux_rate2_5.flow_range(),
                 pumps_figure.Pump2_5.head_formula(),
                 label="150HP(111.85kw)")
    # Plotting legend specifications.
    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 8013 1760 RPM")
    plt.savefig("pump4.png")
    plt.show()


def plot_three():
    """
    This function plots the parallel arrangement, when the user input an
    elevation that is higher than the maximum elevation of the pump two
    curve performance.

    :return: The plot of the parallel arrangement. In case the user input an
    elevation higher than the maximum elevation capacity of the pump two.
    """
    # Iterating for finding the amount un pumps arranged in parallel.
    for x in range(100000):
        #  Breaks when arranged pumps elevation is higher than user one.
        if (x * performances.max_elevation_two) > performances.user_elevation:
            break
        equation_parallel = \
            ((x + 1) * -0.0003) * \
            (pumps_figure.flux_rate2_5.flow_range() ** 2) + \
            ((x + 1) * 0.0521) * pumps_figure.flux_rate2_5.flow_range() \
            + ((x + 1) * 53.481)
        # Plotting the arranged performance curves.
        plt.plot(pumps_figure.flux_rate2_5.flow_range(), equation_parallel,
                 label="150HP(111.85kw)")
    # Plotting legend specifications.
    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 8013 1760 RPM")
    plt.savefig("pump5.png")
    plt.show()


def plot_four():
    """
     This function plots the series arrangement, when the user input a
    flow discharge that is higher than the maximum flow of the pump two
    curve performance.

    :return: The plot of the series arrangement. In case the flow discharge
     is higher than the maximum flow capacity of the pump two.
    """
    # Iterating for finding the amount un pumps arranged in series.
    for x in range(100000):
        #  Breaks when arranged pumps flow is higher than the user one.
        if (x * performances.max_flow_two) > performances.flow_discharge:
            break
        equation_series = \
            (-0.0003) * ((pumps_figure.flux_rate2_5.flow_range() * x) ** 2) + \
            0.0521 * (pumps_figure.flux_rate2_5.flow_range() * x) + 53.481

        # Plotting the arranged performance curves.
        plt.plot((pumps_figure.flux_rate2_5.flow_range() * (x + 1)),
                 equation_series,
                 label="150HP(111.85kw)")

    # Plotting legend specifications.
    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 8013 1760 RPM")
    plt.savefig("pump6.png")
    plt.show()


def plot_five():
    """
    This function plots the parallel and series arrangements, when the
    user input an elevation and the result of the 'flow_discharge.py'
    is a flow is higher than the maximum elevation and flow of the pump
    two curve performance.

    :return: The plot of the series and parallel arrangement. In case the
    elevation and flow discharge are higher than the maximum capacity of
    the pump two.
    """
    # Iterating for finding the amount un pumps arranged in parallel.
    for x in range(100000):
        #  Breaks when arranged pumps elevation is higher than the user one.
        if (x * performances.max_elevation_two) > performances.user_elevation:
            break
        equation_parallel_comb = \
            (x * -0.0003) * (pumps_figure.flux_rate2_5.flow_range() ** 2) + \
            (x * 0.0521) * pumps_figure.flux_rate2_5.flow_range() + (
                        x * 53.481)
        plt.plot(pumps_figure.flux_rate2_5.flow_range(),
                 equation_parallel_comb,
                 label="150HP(111.85kw)")

    # Iterating for finding the amount un pumps arranged in series.
    for z in range(100000):
        #  Breaks when arranged pumps flow is higher than the user one.
        if (z * performances.max_flow_two) > performances.flow_discharge:
            break
        equation_series_comb = \
            (-0.0003) * ((pumps_figure.flux_rate2_5.flow_range() * z) ** 2) + \
            0.0521 * (pumps_figure.flux_rate2_5.flow_range() * z) + 53.481

        # Plotting the arranged performance curves.
        plt.plot((pumps_figure.flux_rate2_5.flow_range() * (z + 1)),
                 equation_series_comb,
                 label="150HP(111.85kw)")

    # Plotting legend specifications.
    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 8013 1760 RPM")
    plt.savefig("pump6.png")
    plt.show()
