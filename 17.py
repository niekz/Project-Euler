ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: ''}
misc = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety', 0: ''}
hundreds = 'hundredand'
thousands = 'thousand'
a = 'and'

def one(x):
    return ones.get(x)

def ten(x):
    return tens.get(x)

def toText(number):
    if len(str(number)) == 1:
        return one(number)

    if len(str(number)) == 2:
        if misc.get(int(str(number)[len(str(number))-2:])) == None:
            return ten(int(str(number)[0])) + one(int(str(number)[1]))
        else:
            return misc.get(number)

    if len(str(number)) == 3:
        if int(str(number)[len(str(number))-2:]) != 0:
            if misc.get(int(str(number)[len(str(number))-2:])) == None:
                if int(str(number)[len(str(number))-2:]) != 0:
                    return one(int(str(number)[0])) + hundreds + ten(int(str(number)[1])) + one(int(str(number)[2]))
            else:
                return one(int(str(number)[0])) + hundreds + misc.get(int(str(number)[len(str(number))-2:]))
        else:
            return one(int(str(number)[0])) + hundreds[:-3] 

    if len(str(number)) == 4:
        if int(str(number)[len(str(number))-3:]) != 0: 
            if int(str(number)[len(str(number))-2:]) != 0:
                if misc.get(int(str(number)[len(str(number))-2:])) == None:
                    return one(int(str(number)[0])) + thousands + one(int(str(number)[1])) + hundreds + ten(int(str(number)[2])) + one(int(str(number)[3]))
                else:
                    return one(int(str(number)[0])) + thousands + one(int(str(number)[1])) + hundreds + misc.get(int(str(number)[len(str(number))-2:]))
            else:
                return one(int(str(number)[0])) + thousands + one(int(str(number)[1])) + hundreds[:-3]
        else:
            return one(int(str(number)[0])) + thousands

count = 0
for x in range(1, 1001):
    count += len(str(toText(x)))

print count
    
