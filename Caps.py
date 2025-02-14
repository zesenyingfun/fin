import math
from scipy.stats import norm

def calculate_caplet_value(forward_rate, strike_rate, volatility, time_to_expiration, discount_factor):
    """
    Calculates the value of a caplet using the Black-Scholes formula.

    Parameters:
    forward_rate (float): The forward interest rate for the period.
    strike_rate (float): The strike rate or cap rate of the caplet.
    volatility (float): The volatility of the interest rate.
    time_to_expiration (float): Time in years until the caplet's expiration.
    discount_factor (float): The discount factor for the period.

    Returns:
    float: The value of the caplet.
    """
    d1 = (math.log(forward_rate / strike_rate) + 0.5 * volatility ** 2 * time_to_expiration) / (
                volatility * math.sqrt(time_to_expiration))
    d2 = d1 - volatility * math.sqrt(time_to_expiration)

    caplet_value = discount_factor * (forward_rate * norm.cdf(d1) - strike_rate * norm.cdf(d2))
    return caplet_value


def calculate_caplets_pricing(forward_rates, strike_rate, volatility, time_to_expirations, discount_factors):
    """
    Calculates the total value of caplets in an interest rate cap.

    Parameters:
    forward_rates (list of float): Forward interest rates for each period.
    strike_rate (float): Strike rate or cap rate for each caplet.
    volatility (float): Volatility of the interest rate.
    time_to_expirations (list of float): Times to expiration for each caplet in years.
    discount_factors (list of float): Discount factors for each period.

    Returns:
    list of float: The value of each caplet.
    float: Total value of all caplets (cap value).
    """
    caplet_values = []
    total_cap_value = 0.0

    for i in range(len(forward_rates)):
        caplet_value = calculate_caplet_value(
            forward_rates[i],
            strike_rate,
            volatility,
            time_to_expirations[i],
            discount_factors[i]
        )
        caplet_values.append(caplet_value)
        total_cap_value += caplet_value

    return caplet_values, total_cap_value


