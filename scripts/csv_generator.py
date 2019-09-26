import pandas as pd
import re

# functions

def string_creator(digits, pos):
    if len(digits) == 1:
        digits.append(digits[0])        
    return int(digits[pos])

def get_time_spent(in_string, pos):
    if type(in_string) != str:
        return ''
    digits = re.findall(r"\d*\.\d+|\d+", in_string)
    digits = [float(d) for d in digits]
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
    returned_val = string_creator(digits, pos)
    return returned_val

def get_time_spent_0(in_string):
    return get_time_spent(in_string, 0)

def get_time_spent_1(in_string):
    return get_time_spent(in_string, 1)

popular_times_1 = pd.read_csv('../data/popular_times_1.csv')
popular_times_2 = pd.read_csv('../data/popular_times_2.csv')
places = pd.read_csv('../data/places_healthcare.csv')
popular_times = pd.concat([popular_times_1, popular_times_2])
print("unikalne", len(popular_times['place_id'].unique()), len(places['place_id'].unique()))
print(type(popular_times['place_id'].unique()))
klucze_popular_times = set(popular_times['place_id'].unique().tolist())
klucze_places = set(places['place_id'].unique().tolist())
print("cześć wspolna", len(klucze_popular_times.intersection(klucze_places)))
print("")
print(len(popular_times))
data = pd.merge(places, popular_times, how='inner')
print(len(data))

data['min_time_spent_minutes'] = data['av_time_spent'].apply(get_time_spent_0)
data['max_time_spent_minutes'] = data['av_time_spent'].apply(get_time_spent_1)
data.to_csv("../data/data.csv")