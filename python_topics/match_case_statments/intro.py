# Match case statement (switch) : An alternative to using many 'elif' statements 
# Execute some code if a value matches a 'case' 
#  Benefits : cleaner and syntax is more readable 
#   _ = else
#  | = or 

def weekday_check(day_count) : 
    match day_count : 
        case 1 : 
            return "Monday "
        case 2 : 
            return "Tuesday"
        case 3 : 
            return "wednesday"
        case 4 : 
            return "Thursday"
        case 5 : 
            return "Friday"
        case 6 : 
            return "Satday"
        case 7 : 
            return "Sunday"
        case _ :
            return "Invalid"

print(weekday_check(3))

def weekday_or_weekend(day):
    match day :
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday" : 
            return "Weekday "
        case "Saturday" | "Sunday" : 
            return "Weekend"
        case _ :
            return "Invalid"

print(weekday_or_weekend("Saturday"))
