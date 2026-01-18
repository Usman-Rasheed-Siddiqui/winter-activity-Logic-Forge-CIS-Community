
def suspicious_device(length):

    if length:
        if length % 2 != 0:
            return "Length should be even"
        numbers = list(map(int,input().split()))
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
            return number

print(suspicious_device(6))
            
