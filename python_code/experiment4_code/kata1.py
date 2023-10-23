def naughty_or_nice(data):
    Naughty_count = 0
    Nice_count = 0
    
    for month_data in data.values():
        for day,behavior in month_data.items():
            if behavior == 'Naughty':
                Naughty_count +=1
            elif behavior == 'Nice':
                Nice_count +=1


    if Naughty_count > Nice_count:
        return 'Naughty!'
    else:
        return 'Nice!'

# 示例数据
year_data = {
    'January': {'1': 'Naughty', '2': 'Naughty', '31': 'Nice'},
    'February': {'1': 'Nice', '2': 'Naughty', '28': 'Nice'},
    # ... 其他月份的数据
    'December': {'1': 'Nice', '2': 'Nice', '31': 'Naughty'}
}

result = naughty_or_nice(year_data)
print(result)

