# =============================================================================
# Define functions
# 
# In order to use unit tests on functions, it seems they will need to return
# values. That is, don't print the results to screen within the functions.
# =============================================================================

def calc_avg_two_numbers(number_1: float, number_2: float) -> float:
    """Calculate the average of two input numbers"""

    average = (number_1 + number_2) / 2

    # print("Average:", average)

    return average


def calc_roi_one_period(price_time_1: float, price_time_2: float) -> float:
    """Calculate the return on investment from period 1 to period 2.
    Assume that portfolio value is always positive.
    There are no interim PMTs."""

    roi = (price_time_2 - price_time_1) / price_time_1

    # print("Return on investment:", roi)

    return roi


def calc_pythagorean_theorem_side(hypotenuse_length: float, side_length: float) -> float:
    """Calculate the Pythagorean theorem for a missing side
    Results are passed back as a float type.
    
    Right triangles only!

    Input:
        hypotenuse_length - int or float
        side_length - int or float
    """

    while True:
        try:
            b = float(hypotenuse_length)
        except ValueError:
            print("Numeric only!")
            continue
        break

    while True:
        try:
            c = float(side_length)
        except ValueError:
            print("Numeric only!")
            continue
        break      

    a = ((c * c) - (b * b)) ** (1.0 / 2.0)

    if isinstance(a, complex):
        print("Your return is complex. Ensure values are meet Pythagorean requirements")

    # print("Side length:", round(a, 5))

    return round(a, 5)


def calc_pythagorean_theorem_hyp(side_length_a: float, side_length_b: float) -> float:
    """Calculate the Pythagorean theorem for a missing hypotenuse.
    Results are passed back as a float type.
    
    Right triangles only!

    Input:
        side_length_a - int or float
        side_length_b - int or float
    """

    while True:
        try:
            a = float(side_length_a)
        except ValueError:
            print("Numeric only!")
            continue
        break

    while True:
        try:
            b = float(side_length_b)
        except ValueError:
            print("Numeric only!")
            continue
        break      

    c = ((a * a) + (b * b)) ** (1.0 / 2.0)

    if isinstance(c, complex):
        print("Your return is complex. Ensure values are meet Pythagorean requirements")
    
    # print("Hypotenuse length:", round(c, 5))

    return round(c, 5)


# %%

# =============================================================================
# Use the functions defined in this script
# =============================================================================

calc_avg = calc_avg_two_numbers(10, 10)

calc_roi = calc_roi_one_period(2.5, 0)

calc_side = calc_pythagorean_theorem_side(2, 5)

calc_hypo = calc_pythagorean_theorem_hyp(4, 5)
