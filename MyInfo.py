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

BUILD_GROWTH = 1.15


class MyInfo:
    """
    Class to track build information.
    """

    def __init__(self, build_info=None, growth_factor=BUILD_GROWTH):
        self._build_growth = growth_factor
        # if there is not default items to purchase, initialize it with the Cursor and Grandma
        if build_info == None:
            self._info = {'Cursor':
                              [15.0, 0.10000000000000001], 'Grandma': [100.0, 0.5]}
        # otherwise, build the given list into dictionary of with key is the name of the item and values are the price and the effect on CPS
        else:
            self._info = {}
            for key, value in build_info.items():
                self._info[key] = list(value)

    def build_items(self):
        """
        Get a list of buildable items.
        """
        return self._info.keys()

    def get_cost(self, item):
        """
        Get the current cost of an item
        Will throw a KeyError exception if item is not in the build info
        """
        return self._info[item][0]

    def get_cps(self, item):
        """
        Get the current CPS effect of the item
        Will throw a KeyError exception if item is not in the build info.
        """
        return self._info[item][1]

    def update_item(self, item):
        """
        Update the cost of an item by the growth factor
        Will throw a KeyError exception if item is not in the build info.
        """
        # save the current cost and CPS of the item
        cost, cps = self._info[item]
        self._info[item] = [cost * BUILD_GROWTH, cps]

    def clone(self):
        """
        Return a clone of this BuildInfo
        """
        return MyInfo(self._info, self._build_growth)


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
        Return human readable state.
        """
        return "\n" + "Total cookies: " + str(self.total_cookies) + "\n"
        + "Current cookies: " + str(self.current_cookies) + "\n"
        + "Current time: " + str(self.current_time) + "\n"
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
        Firstly, you need to find the cheapest item. And then determine if with the current number of cookies and the cookies made in the time left,
        is >= the cheapest price.
        """
        items_list = build_info.build_items()
        cheapest_item = items_list[0]
        cheapest_price = build_info.get_cost(items_list[0])

        for item in items_list:
            if build_info.get_cost(item) < cheapest_price:
                cheapest_item = item
                cheapest_price = build_info.get_cost(item)

        if (cookies + cps * time_left) < cheapest_price:
            return None
        else:
            return cheapest_item

    def strategy_expensive(cookies, cps, history, time_left, build_info):
        """
        Always buy the most expensive item you can afford in the time left.
        Firstly, you need to find the cheapest item. And then determine if with the current number of cookies and the cookies made in the time left,
        is >= the cheapest price.
        """
        items_list = build_info.build_items()
        most_expensive_item = items_list[0]
        most_expensive_price = build_info.get_cost(items_list[0])

        for item in items_list:
            if build_info.get_cost(item) > most_expensive_price:
                most_expensive_item = item
                most_expensive_price = build_info.get_cost(item)

        if (cookies + cps * time_left) < most_expensive_price:
            return None
        else:
            return most_expensive_item

    def strategy_best(cookies, cps, history, time_left, build_info):
        """
        The best strategy that you are able to implement.
        """
        items_list = build_info.build_items()

        best_item = items_list[0]
        best_price = build_info.get_cost(items_list[0])

        # calculate and compare based on the ratio of cps and cost of the items
        best_ratio = build_info.get_cps(items_list[0]) / build_info.get_cost(items_list[0])

        for item in items_list:
            if build_info.get_cps(item) / build_info.get_cost(item) >= best_ratio and (
                    cookies + cps * time_left) > build_info.get_cost(item):
                # update the new item with best ratio
                best_item = item
                best_price = build_info.get_cost(item)
        if (cookies + cps * time_left) < best_price:
            return None
        else:
            return best_item

    def run_strategy(strategy_name, time, strategy):
        """
        Run a simulation for the given time with one strategy.
        """
        # state = simulate_clicker(provided.BuildInfo(), time, strategy)
        print
        # strategy_name, ":", state

        # Plot total cookies over time

        # Uncomment out the lines below to see a plot of total cookies vs. time
        # Be sure to allow popups, if you do want to see it

        # history = state.get_history()
        # history = [(item[0], item[3]) for item in history]
        # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


"""def run():

Run
the
simulator.

run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)"""

# Add calls to run_strategy to run additional strategies
# run_strategy("Cheap", SIM_TIME, strategy_cheap)
# run_strategy("Expensive", SIM_TIME, strategy_expensive)
# run_strategy("Best", SIM_TIME, strategy_best)"""

# run()
