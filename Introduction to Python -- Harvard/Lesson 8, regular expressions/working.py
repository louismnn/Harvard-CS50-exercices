import re

def main():
    print(convert(input("Hours: ")))

def convert(s):

    try:
        matchfunction = re.search(r"^([0-9]{1,2}:[0-9]{2}|[0-9]{1,2})\s?(AM|PM)?\s?to\s?([0-9]{1,2}:[0-9]{2}|[0-9]{1,2})\s?(AM|PM)?$", s)
        morning = matchfunction.group(1)
        afternoon = matchfunction.group(3)

        if matchfunction.group(2) == "AM":
            new_morning = avant_midi(morning)
        elif matchfunction.group(2) == "PM":
            new_morning = apres_midi(morning)
        else:
            new_morning = nothing_two(morning)

        if matchfunction.group(4) == "AM":
            new_afternoon = avant_midi(afternoon)
        elif matchfunction.group(4) == "PM":
            new_afternoon = apres_midi(afternoon)
        else:
            new_afternoon = nothing_two(afternoon)

        result = new_morning + " to " + new_afternoon
        if "ValueError" in result:
            return ValueError
        else:
            return result    
    
    except ValueError:
        return ValueError

def avant_midi(hour):
    if ":" in hour:
        start, end = str(hour).split(":")
        if int(end) > 59:
            return ValueError
    else:
        start = hour
        end = "00"

    if int(start) > 12:
        return ValueError
    
    if len(start) == 1:
        return "0" + start + ":" + end
    else:
        return start + ":" + end

def apres_midi(hour):
    if ":" in hour:
        start, end = str(hour).split(":")
        if int(end) > 59:
            return ValueError
    else:
        start = hour
        end = "00"

    if int(start) < 12:
        new_start = int(start) + 12
    else:
        new_start = start

    if new_start == 24:
        return "00:" + end
    else:
        return str(new_start) + ":" + end

def nothing_one(hour):
    if ":" in hour:
        start, end = str(hour).split(":")
    else:
        start = hour
        end = "00"

    if len(start) == 1:
        new_start = "0" + start
    else:
        new_start = start

    return new_start + ":" + end

def nothing_two(hour):
    if ":" in hour:
        start, end = str(hour).split(":")
    else:
        start = hour
        end = "00"

    if len(start) == 1:
        new_start = "0" + str(int(start) + 12)
    elif len(start) == 2 and int(start) < 12:
        new_start = str(int(start) + 12)
    else:
        new_start = start

    return new_start + ":" + end


main()