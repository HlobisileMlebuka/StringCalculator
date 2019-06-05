import re

def add(numberstr):
    if numberstr == "":                                 #empty string
        return 0


    elif re.search(r"(\[.\])", numberstr):           #(//[symbols]\n)#multipledelimeter
        symbolstring = re.findall(r"\d+", numberstr)
        symbolSumTotal = 0
        for symbolnum in symbolstring:
            symbolSumTotal = symbolSumTotal + int(symbolnum)
        return symbolSumTotal



    elif re.match(r"(\/\/.+\n)", numberstr):            #(//;67\n) and (///***\n)
        delimeter = re.findall(r"((?<=\/\/).*?(?=\n))", numberstr)
        y = delimeter[0]
        delimeterstring = re.findall(r"((?<=\n)\d+(?=%s)|(?<=%s)\d+(?=%s)|(?<=%s)\d+)" %(y,y,y,y), numberstr)
        delimeterSumTotal = 0
        for delimeternum in delimeterstring:
            if int(delimeternum) < 1000:
                delimeterSumTotal = delimeterSumTotal + int(delimeternum)
        return delimeterSumTotal

    
    elif re.match(r"(^(\d+|-\d+))", numberstr):         #newline characters/no big numbers/exception for negatives
        newlinestring = re.findall(r"(-\d+|\d+)", numberstr)
        negativenumbers = re.findall(r"(-\d+)", numberstr)
        newlineSumTotal = 0
        for newlinenum in newlinestring:
            if int(newlinenum) < 0:
                raise ValueError("negatives: " + str(negativenumbers) + " not allowed")
            else:
                newlineSumTotal = 0
                for newlinenum in newlinestring:
                    if int(newlinenum) < 1000:           
                        newlineSumTotal = newlineSumTotal + int(newlinenum)
                return newlineSumTotal


# if __name__ == "__main__":
#     x = '21,12\n,4,-7,9'
#     print(add(x))
    





            
         

       
            
    