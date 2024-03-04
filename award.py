swimming_time = int(input("Enter swimming time (in minutes): "))
cycling_time = int(input("Enter cycling time (in minutes): "))
running_time = int(input("Enter running time (in minutes): "))

total_time = swimming_time + cycling_time + running_time

if total_time <= 100:
    award = "Provincial Colours"
elif 100 < total_time <= 105:
    award = "Provincial Half Colours"
elif 105 < total_time <= 110:
    award = "Provincial Scroll"
else:
    award = "No award"

print("Total time taken to complete the triathlon:", total_time, "minutes")
print("Award:", award)