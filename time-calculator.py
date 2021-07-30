def add_time(start, duration, weekday=False):

    #We create a tuple (inmutable list)
    weekdays_index = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    weekdays_array = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    duration_tuple = duration.partition(':')
    print(duration_tuple)
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])
    #0 is  hours, 1 is  : and 2 is minutes
    
    start_tuple = start.partition(':')
    start_minutes_tuple = start_tuple[2].partition(' ')
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2]
    am_and_pm_flip = {'AM': 'PM', 'PM': 'AM'}
    
    #We take the start_minutes_tuple as 0 because it was already declared in 2
    
    amount_of_days = int(duration_hours / 24)

    end_minutes = start_minutes + duration_minutes
    if(end_minutes >= 60) :
      start_hours += 1
      end_minutes = end_minutes % 60
    amount_of_am_pm_flips = int((start_hours + duration_hours) / 12)
    end_hours = (start_hours + duration_hours) % 12

    #What are the % for?

    end_minutes = end_minutes if end_minutes > 9 else '0' + str(end_minutes)
    end_hours = end_hours = 12 if end_hours == 0 else end_hours
    if(am_or_pm == 'PM' and start_hours + (duration_hours % 12) >= 12):
      amount_of_days += 1
    
    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm

    returnTime = str(end_hours) + ':' + str(end_minutes) + ' ' + am_or_pm
    if(weekday) :
      weekday = weekday.lower()
      index = int((weekdays_index[weekday]) + amount_of_days) % 7
      new_day = weekdays_array[index]
      returnTime += ', ' + new_day

    if(amount_of_days == 1):
      return returnTime + ' ' + '(next day)'
    elif(amount_of_days > 1):
      return returnTime + '(' + str(amount_of_days) + 'days later)'



    #We've declared the 'ifs' in the opposite way

    return start

  
  from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))
