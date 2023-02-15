import math

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


class Greedy_boss:
    def __init__(self):
        # initialize the variables
        self.current_day = 0
        self.current_savings = 0
        self.total_salary_earned = 0

        self.current_bribe_cost = INITIAL_BRIBE_COST
        self.current_salary = INITIAL_SALARY

        # list for days and total earnings
        self.days_vs_earnings = []

    def greedy_boss(self, days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
        """
        Simulation.
        :param days_in_simulation: the number of days the simulation happens
        :param bribe_cost_increment: increase in the bribe cost
        :param plot_type: game plot type standard or loglog
        :return: list of days the player buys bribe and the total earning on those days.
        """

        while self.current_day <= days_in_simulation:
            if self.current_savings >= self.current_bribe_cost:
                days_vs_earnings = 0
            else:
                # calculate the number of days to next bribe purchasing
                time_to_next_bribe = (self.current_bribe_cost - self.current_savings) / float(self.current_salary)
                days_to_next_bribe = int(math.ceil(time_to_next_bribe))

            # shift cu
            # current_day to the day purchasing bribe
            self.current_day += days_to_next_bribe

            # shift everything to the day purchasing bribe
            self.current_savings += days_to_next_bribe * self.current_salary
            self.current_savings -= self.current_bribe_cost

            self.total_salary_earned += days_to_next_bribe * self.current_salary

            self.current_bribe_cost += bribe_cost_increment
            self.current_salary += SALARY_INCREMENT

            self.days_vs_earnings.append((self.current_day, self.total_salary_earned))
        return self.days_vs_earnings

    def calculate(self, num1, num2):
        return num1 + num2


if __name__ == '__main__':
    greedy_boss = Greedy_boss()
    #print(greedy_boss.greedy_boss(35, 100))
    assert 7, greedy_boss.calculate(2, 3)
