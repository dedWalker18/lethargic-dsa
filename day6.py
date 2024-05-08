times = [53897698]
distance = [313109012141201]

product = 1
for time,dist in zip(times,distance):
    req_speed = float(dist/time)
    count = 0
    for ms in range(1,time):
        if ms * (time-ms) > dist:
            count+=1
    product= product*count
    
print(product)