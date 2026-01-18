
def suspicious_device(length = None):
    """
    Find the first repeated number in a list of numbers.
    
    :param length: expected even length of numbers (optional)
    :return: first repeated number or error message
    """

    if length:
        if length % 2 != 0:
            return "Length should be even"
        numbers = list(map(int,input().split()))    # Read numbers from input
        if len(numbers) != length:
            return "Insufficient numbers"
    
    else:
        numbers = list(map(int,input().split()))
        length = len(numbers)
        if length % 2 != 0:
            return "Length should be even"

    numbers_dict = {}
    for number in numbers:
        if number not in numbers_dict:
            numbers_dict[number] = 1    
        else:
            return number   # first repeated number

length = 6
#print("Length:", length)
print("Suspicious Number:",suspicious_device())