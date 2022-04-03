duration = int(input('Введите количество секунд: '))
sec_minute = 60
sec_hour = 60*60
sec_day = sec_hour*24


if duration < sec_minute:      #секунды
    print('{} сек'.format(duration))

elif sec_minute <= duration and sec_hour > duration: # минуты
    this_minute = duration//sec_minute
    this_second = duration % sec_minute
    print('{} мин  {} сек'.format(this_minute, this_second))
elif duration >= sec_hour and duration < sec_day:     #часы
    this_hour = duration // sec_hour
    duration = duration % sec_hour
    this_minute = duration // sec_minute
    this_second = duration % sec_minute
    print('{} час {} мин {} сек'.format(this_hour, this_minute, this_second))

elif duration >= sec_day:  # дни
    this_day = duration // sec_day
    duration = duration % sec_day
    this_hour = duration // sec_hour
    duration = duration % sec_hour
    this_minute = duration // sec_minute
    this_second = duration % sec_minute
    print('{} дни {} час {} мин {} сек'.format(this_day, this_hour, this_minute, this_second))