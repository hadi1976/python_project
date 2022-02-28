from config import *


class FlowRatePump:
    """
    Author:Seyedhadi Hashemi
    This class "FlowRatePump" has 3 attributes;start, stop, name
    The Method is called flow_rate which gets the attributes and
    create a list of 500 numbers between stop and start.
    """

    def __init__(self, start, stop, name):
        self.start = start
        self.stop = stop
        self.name = name

    def flow_range(self):
        """
        It gets the start,stop point and generate a
        list of 500 numbers between them.
        :return: self.name
        """
        self.name = np.linspace(self.start, self.stop, num=500)
        return self.name


# Object of FlowRatePump class for the first pump
flux_rate1 = FlowRatePump(0, 12, "flux_rate1")
flux_rate2 = FlowRatePump(0, 12.5, "flux_rate2")
flux_rate3 = FlowRatePump(0, 14, "flux_rate3")
flux_rate4 = FlowRatePump(0, 16, "flux_rate4")
flux_rate5 = FlowRatePump(0, 17.2, "flux_rate5")

# Object of FlowRatePump class for the second pump
flux_rate2_1 = FlowRatePump(0, 160, "flux_rate1")
flux_rate2_2 = FlowRatePump(0, 200, "flux_rate2")
flux_rate2_3 = FlowRatePump(0, 230, "flux_rate3")
flux_rate2_4 = FlowRatePump(0, 250, "flux_rate4")
flux_rate2_5 = FlowRatePump(0, 285, "flux_rate5")


class HeadPump:
    """
    author:Seyedhadi Hashemi
    This class "HeadPump" create 6 attributes.
    It gives us the pumps' equation which is a 3rd grade equation.
    so the equation of our pump is; y=aX^3+bX^2+cX+d
    in this class our X is flux_rate1,flux_rate2,...flux_rate5.
    and y is our head pump. And the Method's name is head_formula which
    gets all the attributes and generate the respective equation.
    """

    def __init__(self, a, b, c, d, flux_rate, name):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.name = name
        self.flux_rate = flux_rate

    def head_formula(self):
        """
        It gets the coefficients of the formula
        and generate the formula
        :return: self.name
        """

        self.name = self.a * (self.flux_rate ** 3) + self.b *\
            (self.flux_rate ** 2) + self.c * (
                self.flux_rate ** 1) + self.d * (
                            self.flux_rate ** 0)
        return self.name


# Object of HeadPump class for the first pump
Pump1 = HeadPump(-0.0061, -0.01, 0.015, 11.364, flux_rate1.flow_range(),
                 "Pump1")
Pump2 = HeadPump(-0.0051, 0.0121, - 0.0341, 14.619, flux_rate2.flow_range(),
                 "Pump2")
Pump3 = HeadPump(-0.0034, - 0.014, 0.1205, 18.116, flux_rate3.flow_range(),
                 "Pump3")
Pump4 = HeadPump(0, -0.0612, 0.3119, 22.021, flux_rate4.flow_range(), "Pump4")
Pump5 = HeadPump(0, -0.0589, 0.3821, 26.731, flux_rate5.flow_range(), "Pump5")

# Object of HeadPump class for the second pump
Pump2_1 = HeadPump(0, -0.001, 0.07, 22.941, flux_rate2_1.flow_range(), "Pump1")
Pump2_2 = HeadPump(0, -0.0006, 0.0648, 28.838, flux_rate2_2.flow_range(),
                   "Pump2")
Pump2_3 = HeadPump(0, -0.0006, 0.0779, 35.279, flux_rate2_3.flow_range(),
                   "Pump3")
Pump2_4 = HeadPump(0, -0.0004, 0.0521, 43.847, flux_rate2_4.flow_range(),
                   "Pump4")
Pump2_5 = HeadPump(0, -0.0003, 0.0521, 53.481, flux_rate2_5.flow_range(),
                   "Pump5")


def plot_pump1():
    """
    This function would plot all the pumps bg getting the flow_rate in X_axis
    and head pump in y_axis.
    """
    plt.figure(num=None, dpi=120)
    plt.plot(flux_rate1.flow_range(), Pump1.head_formula(),
             label="1.5HP(1.1kw)")
    plt.plot(flux_rate2.flow_range(), Pump2.head_formula(), label="2HP(1.5kw)")
    plt.plot(flux_rate3.flow_range(), Pump3.head_formula(), label="3HP(2.2kw)")
    plt.plot(flux_rate4.flow_range(), Pump4.head_formula(), label="5HP(3.6kw)")
    plt.plot(flux_rate5.flow_range(), Pump5.head_formula(),
             label="7.5HP(5.6kw)")

    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 2009 1760 RPM")
    plt.savefig("pump1.png")
    plt.show()


def plot_pump2():
    """
    This function would plot all the pumps bg getting the flow_rate in X_axis
    and head pump in y_axis.
    """

    plt.figure(num=None, dpi=120)
    plt.plot(flux_rate2_1.flow_range(), Pump2_1.head_formula(),
             label="60HP(44kw)")
    plt.plot(flux_rate2_2.flow_range(), Pump2_2.head_formula(),
             label="75HP(56kw)")
    plt.plot(flux_rate2_3.flow_range(), Pump2_3.head_formula(),
             label="100HP(74.5kw)")
    plt.plot(flux_rate2_4.flow_range(), Pump2_4.head_formula(),
             label="125HP(93.2kw)")
    plt.plot(flux_rate2_5.flow_range(), Pump2_5.head_formula(),
             label="150HP(111.85kw)")

    plt.legend()
    plt.xlabel("flow rate Lit/Sec")
    plt.ylabel("Head (m)")
    plt.title("Model 8013 1760 RPM")
    plt.savefig("pump2.png")
    plt.show()
