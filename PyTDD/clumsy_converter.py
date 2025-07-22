def roman_converter (num):
    str=""
    value = [1000, 500, 100, 50, 10, 5, 1]
    letter = ["M", "D", "C", "L", "X", "V", "I"]
    poz=0
    if type(num) == type(11) :
        if num in range (0,4000):
            while poz < len(value):
                while num >= value[poz] :
                    str += letter[poz]
                    num -=value[poz]
                poz += 1
            return str
    return None
