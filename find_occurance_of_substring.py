def count_substring(string, sub_string):
    count = 0 
    for i in range(0, len(string)):
        subs = string[i:i+len(sub_string)]
        if subs == sub_string:
            count = count + 1
    return count

string = 'WoW!ItSCoOWoWW'
sub_string = 'oW'
print(count_substring(string,sub_string))
    