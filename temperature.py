def celltofahre(value): #this function convert C to F 
     convert = int(value) * 9/5 + 32
     return convert
def fahretocell(value): #this function convert F to C
    convert = (int(value) - 32) * 5/9
    return convert
    
temp = input("enter your temp value in degree -") #take C temp from user 
convert = celltofahre(temp) #call the 1st function
print("Equivalent Fahrenheit temperature is - ", convert, "F" )

temp = input("enter your temp value in Fahrenheit -") #take F temp from user 
convert = fahretocell(temp) #call the 2nd function
print("Equivalent degree temperature is - ", convert, "C" )
