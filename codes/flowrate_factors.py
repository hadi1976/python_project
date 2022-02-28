from config import *

"""
Author: Seyedhadi Hashemi
"""

# read the country name from text file
with open(country) as file:
    country_name = file.read()

# read the number of inhabitants from text file
with open(inhabitants) as file:
    number_inhabitants = int(file.read())


def get_flow_discharge():
    """
    this function read the xlsx file which contains of country names and the
    respective consumption value. Then it created a dictionary which the
    keys are country name and the value is flow discharge. after the user
    give us the name of the country it returns it's respective flow
    discharge :return Water consumption in Lit/day.capita
    """
    dictionary_country = dict()
    wb = load_workbook(country_codes)
    ws = wb.active
    for row in range(2, ws.max_row + 1):
        if ws["B" + str(row)].value is None:
            pass
        else:
            dictionary_country[ws["B" + str(row)].value] = int(
                ws["C" + str(row)].value)

    return dictionary_country[country_name]


def hour_factor():
    """
    This function give us the hourly factor which will be used in pipes design
    :return:hourly_factor
    """
    if number_inhabitants <= 1000:
        hourly_factor = 5.66
        return hourly_factor
    elif 1000 < number_inhabitants <= 10000:
        hourly_factor = 3.84
        return hourly_factor
    elif 10000 < number_inhabitants <= 100000:
        hourly_factor = 2.61
        return hourly_factor
    elif 100000 < number_inhabitants <= 1000000:
        hourly_factor = 1.77
        return hourly_factor


def day_factor():
    """
    This function give us the daily factor which will be used in
    max_daily_flow function.
    :return:daily_factor
    """
    if number_inhabitants <= 1000:
        daily_factor = 2.32
        return daily_factor
    elif 1000 < number_inhabitants <= 10000:
        daily_factor = 1.95
        return daily_factor
    elif 10000 < number_inhabitants <= 100000:
        daily_factor = 1.64
        return daily_factor
    elif 100000 < number_inhabitants <= 1000000:
        daily_factor = 1.38
        return daily_factor


def max_hourly_flow():
    """
    Calculation of Max hourly flow rate.This will be used in pipes design.
    :return: flow2
    """
    flow2 = ((get_flow_discharge() / 24) * number_inhabitants *
             hour_factor()) / 3600
    return float(flow2)


def max_daily_flow():
    """
    Calculation of Max daily flow rate. This will be used in pipes design.
    :return:flow1
    """
    flow1 = ((get_flow_discharge() * number_inhabitants
             * day_factor())) / 86400
    return float(flow1)
