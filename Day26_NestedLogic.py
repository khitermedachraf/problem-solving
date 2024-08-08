# Read the input as space-separated integers
actualDay, actualMonth, actualYear = map(int, input().split())
expectedDay, expectedMonth, expectedYear = map(int, input().split())

fine = None
if actualYear < expectedYear:
    fine = 0
elif actualYear == expectedYear:
    if actualMonth == expectedMonth:
        if actualDay <= expectedDay:
            fine = 0
        else:
            fine = (actualDay - expectedDay) * 15
    elif actualMonth < expectedMonth:
        fine = 0
    else:
        fine = (actualMonth - expectedMonth) * 500

else:
    fine = 10000

print(fine)