str = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = str.split(',')

total_ = 0

for j in time_values:
    j = j.strip()
    
    parts = j.split()

    for part in parts:
        if 'h' in part:
            total += int(part.replace('h', '')) * 60
        elif 'm' in part:
            total += int(part.replace('m', ''))
        elif 's' in part:
            total += int(part.replace('s', '')) // 60

print(total)
