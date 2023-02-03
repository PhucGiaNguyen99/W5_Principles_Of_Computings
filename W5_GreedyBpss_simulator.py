import math

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Simulation of greedy boss

    :param days_in_simulation: the number of days of simulation
    :param bribe_cost_increment: the increment of the bribe cost after each time you purchase the current bribe
    :param plot_type: either STANDARD or LOGLOG
    :return: list of tuples of day of purchasing a bribe and the total earning until that dau
    """
    # initialize necessary local variables
    # total salary earned until that day
    total_earnings = 0

    # total bribe cost paid
    total_bribe_costs = 0

    # current bribe cost
    current_bribe_cost = INITIAL_BRIBE_COST

    # current salary
    current_salary = INITIAL_SALARY

    # current_day is used to keep track of the day of days in simulation
    current_day = 0

    # last_purchase day is used to keep track the day of the last purchase bribe
    last_purchase_day = 0

    # define  list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day < days_in_simulation:
        # increment the day
        current_day += 1
        total_earnings += current_salary
        print("Day", current_day, ": ", total_earnings - total_bribe_costs)
        # check if we have enough money to purchase the current_bribe_cost
        # the difference between the total earnings and total bribe costs is the net earning and is used to determine if there's enough money to buy current_bribe
        if total_earnings - total_bribe_costs >= current_bribe_cost:
            total_bribe_costs += current_bribe_cost

            # append the current_day and total_earnings to the result list
            days_vs_earnings.append((current_day, total_earnings))

            # after buying current bribe, increment both the current_salary
            current_bribe_cost += bribe_cost_increment
            current_salary += SALARY_INCREMENT
            last_purchase_day = current_day
    return days_vs_earnings


def greedy_boss_2(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Method to calculate the days of purchasing bribes and total earnings.

    :param days_in_simulation: the number of days of simulation
    :param bribe_cost_increment: the increment of the bribe cost after each time you purchase the current bribe
    :param plot_type: either STANDARD or LOGLOG
    :return: list of tuples of day of purchasing a bribe and the total earning until that dau
    """

    # initialize the necessary local variables
    current_day = 0
    current_savings = 0  # current savings equals to the difference of total salary earned and the total bribes costs you purchased so far
    total_salary_earned = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_salary = INITIAL_SALARY

    # define list of consisting of days and total salary earned
    days_vs_earnings = []

    # each iteration of this while loop simulates one bribe
    while current_day <= days_in_simulation:
        # update list with days and total salary earned
        # use plot_type to control whether regular or log/log plot
        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, total_salary_earned))
        else:
            days_vs_earnings.append([math.log(current_day), math.log(total_salary_earned)])

        # check if we have enough money to purchase a bribe without waiting
        if current_savings >= current_bribe_cost:
            days_to_next_bribe = 0
        else:
            time_to_next_bribe = (current_bribe_cost - current_savings) / float(current_salary)
            days_to_next_bribe = int(math.ceil(time_to_next_bribe))  # round up the calculated time to the nearest day

        # advance current day to day of next bribe ( DO NOT INCREMENT BY ONE DAY)
        current_day += days_to_next_bribe

        # update state of simulation to reflect bribe
        current_savings += days_to_next_bribe * current_salary
        current_savings -= current_bribe_cost
        total_salary_earned += days_to_next_bribe * current_salary
        current_bribe_cost += bribe_cost_increment
        current_salary += SALARY_INCREMENT

    return days_vs_earnings


print(greedy_boss(25, 100))
