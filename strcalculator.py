import re

def add(numberstr):
    if numberstr == "":
        return 0
      
    elif re.findall(r"-\d+", numberstr):
        negativenumbers = re.findall(r"-\d+", numberstr)
        raise Exception("negatives: " + str(negativenumbers) + " not allowed")
        
    else:
        SumTotal = 0
        splitstring = re.findall(r"\d+", numberstr)
        for num in splitstring:
            SumTotal = SumTotal + int(num)
        return SumTotal
                





