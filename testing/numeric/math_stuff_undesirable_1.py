# def calc_avg_two_numbers(n1, n2):
#     """Calculate the average of two input numbers"""
    
#     average = n1 + n2 / 2
    
#     return average
    

# def calc_roi_one_period(p1, p2):
#     """Calculate the return on investment from period 1 to period 2.
#     Assume that portfolio value is always positive.
#     There are no interim PMTs."""
    
#     roi = (p2 - p1) / p1
    
#     return roi


def calc_pythagorean_theorem():
    """Calculate the Pythagorean theorem
    Results are printed to console, and also passed back as unrounded float"""
    
    print("\nCalculate triangle side lengths with the Pythagorean theorem")
    
    side = input("To solve for Hypotenuse, enter 'c'. Otherwise, enter 'a' or 'b': ")

    if side == 'a':
    
        while True:
    
            try:
                b = float(input("Enter the length of side b: "))
                break
            except:
                print("invalid entry. Numeric only!")
    
            try:
                c = float(input("Enter the length of hypotenuse c: "))
                break
            except:
                print("invalid entry. Numeric only!")
    
            a = ((c * c) - (b * b)) ** (1.0 / 2.0)
            
            print("\nThe length of " + side + " is " + str(round(a, 3)))
        
        return a
    
    elif side == 'b':        
        a = input("Enter the length of side a: ")
        c = input("Enter the length of hypotenuse c: ")
        a = float(a)
        c = float(c)

        b = ((c * c) - (a * a)) ** (1.0 / 2.0)

        print("\nThe length of " + side + " is " + str(round(b, 3)))

        return b
    
    elif side == 'c':
        a = input("Enter the length of side a: ")
        b = input("Enter the length of side b: ")
        a = float(a)
        b = float(b)

        c = ((a * a) + (b * b)) ** (1.0 / 2.0)

        print("\nThe length of " + side + " is " + str(round(c, 3)))
        
        return c

    
result = calc_pythagorean_theorem()