# =============================================================================
# Undesirable solution 2
#
# Like the Undesirable 1 script, this has user inputs.
# Also, right triangle sides a and b use the same equations.
# If I wanted one function to calculate both side and hypotenuse,
# I would have needed user input the determine which equation to use.
# Since unit tests seem to be better fit for parameter inputs, I refactored.
# =============================================================================


def calc_pythagorean_theorem(side, length_first, length_second):
    """Calculate the Pythagorean theorem
    Results are printed to console, and also passed back as a float type"""

    print("\nCalculate triangle side lengths with the Pythagorean theorem")
    
    
    while True:
        try:
            side = input("To solve for Hypotenuse, enter 'c'. Otherwise, choose 'a' or 'b': ")
            assert side in ['a', 'b', 'c']
        
        except AssertionError:
            print("Must choose 'a', 'b' or 'c'")
        else:
            break            


    if side == 'a':
        
        while True:
            try:
                b = float(input("Enter the length of side b: "))
            except ValueError:
                print("Numeric only!")
                continue
            break

        while True:
            try:
                c = float(input("Enter the length of hypotenuse c: "))
            except ValueError:
                print("Numeric only!")
                continue
            break      

        a = ((c * c) - (b * b)) ** (1.0 / 2.0)

        if isinstance(a, complex):
            print("Your return is complex. Ensure values are meet Pythagorean requirements")
        
        print("\nThe length of " + side + " is " + str(complex(a)))
        
        return a
    
    elif side == 'b':        
        while True:
            try:
                a = float(input("Enter the length of side a: "))
            except ValueError:
                print("Numeric only!")
                continue
            break

        while True:
            try:
                c = float(input("Enter the length of hypotenuse c: "))
            except ValueError:
                print("Numeric only!")
                continue
            break      

        b = ((c * c) - (a * a)) ** (1.0 / 2.0)

        if isinstance(b, complex):
            print("Your return is complex. Ensure values are meet Pythagorean requirements")

        print("\nThe length of " + side + " is " + str(round(b, 3)))

        return b
    
    elif side == 'c':
        
        while True:
            try:
                a = float(input("Enter the length of side a: "))
            except ValueError:
                print("Numeric only!")
                continue
            break

        while True:
            try:
                b = float(input("Enter the length of hypotenuse b: "))
            except ValueError:
                print("Numeric only!")
                continue
            break   

        c = ((a * a) + (b * b)) ** (1.0 / 2.0)

        if isinstance(c, complex):
            print("Your return is complex. Ensure values are meet Pythagorean requirements")

        print("\nThe length of " + side + " is " + str(round(c, 3)))
        
        return c

    
result = calc_pythagorean_theorem()