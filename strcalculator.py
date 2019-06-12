import re

def add(numberstring):

    """ This function inputs a sequence of numbers written 
    in a string format. It then returns the sum of all the numbers
    within the sequence. It does not include numbers 
    that are greater than or equal to 1000. It throws an exception for any sequence
    that contains a negative number. The string calclulator 
    handle strings of the following format:
    1) returns an empty string as the number 0.
    2) multiple delimeters in the form "//[delimeter]\n..." or "//[&][^]...\n..."
    3) sequences with new line characters """

    extracted_string = extracting_numbers_from_the_string(numberstring)
    sum_of_string_numbers = addition_of_extracted_strings(extracted_string)
     
    return sum_of_string_numbers

def extracting_numbers_from_the_string(numberstring):
    if numberstring == "":                                  #empty strings return a zero
        extracted_string = '0'
        
    elif re.search(r"(\[.\])", numberstring):               #matches '//[&][*][$]\n...&'         
        extracted_string = re.findall(r"\d+", numberstring)
    
    elif re.match(r"(\/\/.+\n)", numberstring):             #matches "//[delimeter]\n245;145;245;2000"      
        delimeter_string = re.findall(r"((?<=\/\/).*?(?=\n))", numberstring)
        y = delimeter_string[0]                             #convert delimeter_string into a string that can be handled by the extracted_string regex
        extracted_string = re.findall(r"((?<=\n)[-+]?\d+(?=%s)|(?<=%s)[-+]?\d+(?=%s)|(?<=%s)[-+]?\d+)" %(y,y,y,y), numberstring)  #this regular expression also uses
        
    elif re.match(r"(^(\d+|-\d+))", numberstring):          #matches '-52, 1\n5, 1, 1'
        extracted_string = re.findall(r"(-\d+|\d+)", numberstring)
        
    return extracted_string
        
def addition_of_extracted_strings(extracted_string):        #handles string of numbers extracted from different formats
    negativenumbers = re.findall(r"-\d+", str(extracted_string))
    sum_of_string_numbers = 0
    for number in extracted_string:
        
        if int(number) < 0:                                 #no negative numbers allowed
            raise Exception("Negatives: " + str(negativenumbers) + " Not Allowed" )
        
        elif int(number) < 1000:                            #numbers larger than 1000 ignored
            sum_of_string_numbers = sum_of_string_numbers + int(number)
    
    return sum_of_string_numbers

if __name__ == "__main__":
     
    numberstring = '//[&][*][$]\n1*56$1&'
    print(add(numberstring))  
