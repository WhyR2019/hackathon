import pandas as pd
import re

# functions

def string_creator(digits):
    output_string = ''
    for d in digits:
        output_string+= str(int(d))+' '
        
    return output_string[:-1]

def get_time_spent(in_string):
    if type(in_string) != str:
        return ''
    digits = re.findall(r"\d*\.\d+|\d+", in_string)
    digits = [float(d) for d in digits]
    #print(digits)
    minutes_positions = [m.start() for m in re.finditer('min', in_string)]
    hours_positions = [m.start() for m in re.finditer('hr', in_string)]
    hours_positions += [m.start() for m in re.finditer('hours', in_string)]
    hours_positions += [m.start() for m in re.finditer('hour', in_string)]
    if len(minutes_positions) and len(hours_positions): #zmieszane minuty i godziny
        if minutes_positions[0] < hours_positions[0]:
            digits[1] = digits[1]*60
        if minutes_positions[0] > hours_positions[0]:
            digits[0] = digits[0]*60
    else:
        if len(hours_positions):
            for i in range(len(digits)):
                digits[i] = digits[i]*60.0
    returned_val = string_creator(digits)
    #try:
    #print(in_string, returned_val, type(returned_val) )
    #assert type(returned_val)=='str'
    #except AssertionError as e:
    #    print(in_string, returned_val, type(returned_val), e)
    return returned_val

popular_times_1 = pd.read_csv('../data/popular_times_1.csv')
popular_times_2 = pd.read_csv('../data/popular_times_2.csv')
places = pd.read_csv('../data/places_healthcare.csv')
popular_times = pd.concat([popular_times_1, popular_times_2])
print(len(popular_times))
data = pd.merge(places, popular_times, how='inner')
print(len(data))
data['av_time_spent_minutes'] = data['av_time_spent'].apply(get_time_spent)

data.to_csv("../data/data.csv")