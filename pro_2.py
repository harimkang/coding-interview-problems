import datetime

n = 3
customers = [
    "10/01 23:20:25 30",
    "10/01 23:25:50 26",
    "10/01 23:31:00 05",
    "10/01 23:33:17 24",
    "10/01 23:50:25 13",
    "10/01 23:55:45 20",
    "10/01 23:59:39 03",
    "10/02 00:10:00 10",
]

nc = [0 for _ in range(n)]
machine = [
    [i + 1, datetime.datetime.strptime("01/01 00:00:00", "%m/%d %H:%M:%S")]
    for i in range(n)
]

while customers:

    customer = customers.pop(0)
    use_machine = machine.pop(0)
    nc[use_machine[0] - 1] += 1

    cus_time = datetime.datetime.strptime(customer[:-3], "%m/%d %H:%M:%S")
    use_time = cus_time + datetime.timedelta(minutes=int(customer[-2:]))
    machine.append([use_machine[0], use_time])
    machine.sort(key=lambda x: (x[1], x[0]))

print(nc)
print(machine)
