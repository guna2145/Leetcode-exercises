def get_military_time(time):
    # code solution here
    #split the time
    split_time = time.split(":")
    hh = split_time[0]
    mm = split_time[1]
    ss = split_time[2][0:2]
    time_format = split_time[2][2:4]

    #check if AM and hh=12
    if time_format == 'AM' and int(hh) == 12:
        return f"00:{mm}:{ss}"
    #check if PM and hh>12
    elif time_format == 'PM' and int(hh) == 12:
        return f"{hh}:{mm}:{ss}"
    #check if PM 
    elif time_format == 'PM' and int(hh) >= 1 and int(hh) < 12:
        return f"{int(hh)+12}:{mm}:{ss}"
    #return time just remove the timeformat
    else:
        return f"{hh}:{mm}:{ss}"


  
    #return f"{int(split_time[0])+int(12)}:{split_time[1]}:{split_time[2][0:2]}"
print(get_military_time("01:00:00AM"))