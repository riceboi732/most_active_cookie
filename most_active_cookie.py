import sys
from datetime import date, datetime, time


def usage():
    print(f"Template: {sys.argv[0]} <some csv file> -d \"yyyy-mm-dd\"")
try:
    if len(sys.argv) != 4 or sys.argv[2] != '-d': #Check for valid user input
        print("Please Enter a Valid Input Following the Template Below\n")
        usage()
        exit(1)

    c_tracker = {} #Creating a dictionary tracker to track cookie 

    c_hist = open('cookie_log.csv', "r") #Read and store the cookie history file into c_hist

    date_time = datetime.strptime(sys.argv[3], "%Y-%m-%d") #Convert date into a datetime object

    # Iterate through the data and split each csv line into readable format
    for line in c_hist.readlines(): 
        c, t = line.split(",")
        t = t.replace("\n", "")
        # Convert the timestamp for each line into a readable datetime
        tmp_datetime = datetime.strptime(t, '%Y-%m-%dT%H:%M:%S%z')
        if date_time.strftime('%Y-%m-%d') == tmp_datetime.strftime('%Y-%m-%d'):
            #f the cookie already exists, add one to its count
            if c in c_tracker:
                c_tracker[c] += 1
            else:
                # If the has not been seen before, create the cookie and set its count to 1
                c_tracker[c] = 1

    max_occurred = max(c_tracker.values(), key= lambda x: x) #Return the max dictionary value (the most active cookie)
    
#Error catching, if the user input is invalid or there were no cookies for the date given    
except ValueError:
    print("No active cookies for the date you provided or input was invalid, please follow input template below")
    usage()
    exit(1)


for cookie, occurrences in c_tracker.items(): #Print cookie(s) that is the most active (have the highest count)
    if occurrences == max_occurred:
        print(cookie)

c_hist.close() #Close