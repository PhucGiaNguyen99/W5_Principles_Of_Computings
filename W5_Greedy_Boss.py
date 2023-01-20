import math

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Simulation of the greedy boss
    """

    # initialize the necessary varibles
    current_day = 0
    bribe_times = 0
    total_salary = 0
    current_saving = 0
    current_salary = INITIAL_SALARY
    current_bribe = INITIAL_BRIBE_COST

    # initialize the list consisting of days and total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    while current_day <= days_in_simulation:

        # check whether we have enough savings to bribe without waiting
        if current_saving < current_bribe:
            current_saving += current_salary
            total_salary += current_salary
            current_day += 1
        else:
            current_saving -= current_bribe  # purchase current bribe
            current_salary += SALARY_INCREMENT
            current_bribe += bribe_cost_increment
            days_vs_earnings.append((current_day, total_salary))
            # current_day += 1
    return days_vs_earnings


def recommended_solution_greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    current_day = 0
    current_savings = 0
    total_salary_earned = 0
    current_bribe_cost = INITIAL_BRIBE_COST
    current_salary = INITIAL_SALARY

    days_vs_earnings = []
    while current_day <= days_in_simulation:
        if current_savings >= current_bribe_cost:
            days_vs_earnings = 0
        else:
            time_to_next_bribe = (current_bribe_cost - current_savings) / float(current_salary)
            days_to_next_bribe = int(math.ceil(time_to_next_bribe))
        current_day += days_to_next_bribe

        current_savings += days_to_next_bribe * current_salary
        current_savings -= current_bribe_cost
        total_salary_earned += days_to_next_bribe * current_salary
        current_bribe_cost += bribe_cost_increment
        current_salary += SALARY_INCREMENT
    return days_vs_earnings


print(greedy_boss(35, 100, STANDARD))

# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700), (37, 14700)]
# 7845
# print
# greedy_boss(35, 0, STANDARD)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900), (36, 18600)]
