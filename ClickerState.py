"""
Cookie Clicker Simulator
"""
import math

# import simpleplot

# Used to increase the timeout, if necessary
# import codeskulptor

# codeskulptor.set_timeout(20)

# import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self, time_in_simulation):
        self.total_cookies = 0.0
        self.current_cookies = 0.0
        self.current_time = 0.0
        self.current_CPS = 1.0

        self.time_in_simulation = time_in_simulation

        self.item_name = None
        self.item_cost = 0.0

        # history list includes tuples of time, item was bought at that time or None, cost of the item, total number
        # of cookies
        self.history_list = [(self.current_time, self.item_name, self.item_cost, self.total_cookies)]

    def __str__(self):
        """
        Return human readable state
        """
        return "\n" + "Total cookies: " + str(self.total_cookies) + "\n" \
            + "Current cookies: " + str(self.current_cookies) + "\n" \
            + "Current time: " + str(self.current_time) + "\n" \
            + "Current CPS: " + str(self.current_CPS) + "\n"

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self.current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self.current_CPS

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self.current_time

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self.history_list

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        # if the current_cookies is lower than the required number of cookies, return the number of seconds
        # needed to reach the required number of cookies
        if (cookies > 0 and cookies > self.current_cookies):
            return math.ceil((cookies - self.current_cookies) / self.current_CPS)
        else:
            return 0.0

    def wait(self, time):
        """
        Wait for given amount of time and update state.
        Given time is time from current time to the next item purchase.
        Should do nothing if time <= 0.0
        """
        if time <= 0:
            pass
        # Corresponding to update the current day to the day purchasing bribe, the current salary and the total
        # number of earnings in GreedyBoss simulation
        else:
            self.current_time += time
            self.current_cookies += self.current_CPS * time
            self.total_cookies += self.current_CPS * time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if (self.current_cookies >= cost):
            self.item_name = item_name
            self.item_cost = cost
            self.current_cookies -= cost
            self.current_CPS += additional_cps
            new_history_tuple = (self.current_time, self.item_name, self.item_cost, self.total_cookies)
            self.history_list.append(new_history_tuple)
        else:
            pass

    def simulate_clicker(build_info, duration, strategy):
        """
        Function to run a Cookie Clicker game for the given
        duration with the given strategy.  Returns a ClickerState
        object corresponding to the final state of the game.
        """

        # Replace with your code
        return ClickerState()

    def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
        """
        Always pick Cursor!

        Note that this simplistic (and broken) strategy does not properly
        check whether it can actually buy a Cursor in the time left.  Your
        simulate_clicker function must be able to deal with such broken
        strategies.  Further, your strategy functions must correctly check
        if you can buy the item in the time left and return None if you
        can't.
        """
        return "Cursor"

    def strategy_none(cookies, cps, history, time_left, build_info):
        """
        Always return None

        This is a pointless strategy that will never buy anything, but
        that you can use to help debug your simulate_clicker function.
        """
        return None

    def strategy_cheap(cookies, cps, history, time_left, build_info):
        """
        Always buy the cheapest item you can afford in the time left.
        """
        return None

    def strategy_expensive(cookies, cps, history, time_left, build_info):
        """
        Always buy the most expensive item you can afford in the time left.
        """
        return None

    def strategy_best(cookies, cps, history, time_left, build_info):
        """
        The best strategy that you are able to implement.
        """
        return None

    def run_strategy(strategy_name, time, strategy):
        """
        Run a simulation for the given time with one strategy.
        """
        state = simulate_clicker(provided.BuildInfo(), time, strategy)
        print
        strategy_name, ":", state

        # Plot total cookies over time

        # Uncomment out the lines below to see a plot of total cookies vs. time
        # Be sure to allow popups, if you do want to see it

        # history = state.get_history()
        # history = [(item[0], item[3]) for item in history]
        # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

    def run():
        """
        Run the simulator.
        """
        run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

        # Add calls to run_strategy to run additional strategies
        # run_strategy("Cheap", SIM_TIME, strategy_cheap)
        # run_strategy("Expensive", SIM_TIME, strategy_expensive)
        # run_strategy("Best", SIM_TIME, strategy_best)


run()