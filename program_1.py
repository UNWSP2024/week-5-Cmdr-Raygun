# Title: Kilometer Converter
# Author: Andrew Bittner
# Date: 10/4/2024

# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

# Define type conversion function
def convert_typ(inp, outp_typ):
    inp = float(inp)
    while not type(inp) == outp_typ:
        if type(outp_typ) == int:
            inp = int(inp)
        elif type(outp_typ) == float:
            inp = float(inp)
        else:
            inp = str(inp)
    return inp

# Define input validation function
def validate_inp(inp, inp_typ, outp_typ, err_msg = 'Invalid input entered.', inp_msg = 'Please re-enter your answer: '):
    while not type(inp) == outp_typ:
        try:
            inp = float(inp)
            inp = convert_typ(inp, float)
        except:
            print(err_msg)
            inp = (input(inp_msg))
    return inp

# Define kilometer-to-mile converter function
def kilometer_conversion(kilometers):    
    LENGTH_CONVERSION = 0.6214
    miles = kilometers * LENGTH_CONVERSION

    # Return the variable to the calling function
    return miles

#### This piece of the code has been done for you,
#### you only need to worry about the actual temp 
#### conversion logic in the temp_conversion function
if __name__ == '__main__':

    # Get User Input
    kilometers = input('Enter the distance in kilometers (number only; no units): ')
    kilometers = validate_inp(kilometers, str, float)

    # Call kilometer_conversion
    miles = kilometer_conversion(kilometers)

    # Display the miles
    print(f'OK, that distance is equivalent to {miles:.1f} miles.')