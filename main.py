# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Caps
import numpy as np



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for strike_rate in [0.04,0.05,0.06,.07]:
        print(strike_rate)
    # Example parameters
        forward_rates = [0.05, 0.052, 0.055, 0.057, 0.06]  # forward rates for each period
        #strike_rate = 0.05  # cap rate
        volatility_bid = 0.2  # volatility of interest rate
        volatility_ask = 0.22
        time_to_expirations = [1, 2, 3, 4, 5]  # time to expiration for each caplet in years
        discount_factors = [0.95, 0.92, 0.89, 0.86, 0.83]  # discount factors for each period

        caplet_values, total_cap_value = Caps.calculate_caplets_pricing(
            forward_rates,
            strike_rate,
            volatility_bid,
            time_to_expirations,
            discount_factors
        )
        caplet_values_ask, total_cap_value_ask = Caps.calculate_caplets_pricing(
            forward_rates,
            strike_rate,
            volatility_ask,
            time_to_expirations,
            discount_factors
        )

        print("Caplet Values:", np.array(caplet_values)*100)
        print("Caplet Values:", np.array(caplet_values_ask)*100)
        print("bidask:",np.array(caplet_values_ask) - np.array(caplet_values))
        print("==========================================")
