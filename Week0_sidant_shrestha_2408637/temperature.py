


temperatures = [
   1,2,5,11,13,16,18
]


cold = []  
mild = []  
comfortable = []  

for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp < 15:
        mild.append(temp)
    elif 15 <= temp <= 20:
        comfortable.append(temp)

print("Cold temperatures:", cold)
print("Mild temperatures:", mild)
print("Comfortable temperatures:", comfortable)


num_cold = len(cold)
num_mild = len(mild)
num_comfortable = len(comfortable)

print(f"Number of cold temperatures: {num_cold}")
print(f"Number of mild temperatures: {num_mild}")
print(f"Number of comfortable temperatures: {num_comfortable}")


temperatures_fahrenheit = []

for temp in temperatures:
    fahrenheit = (temp * 9 / 5) + 32
    temperatures_fahrenheit.append(fahrenheit)

print("Temperatures in Fahrenheit:", temperatures_fahrenheit)



night = []  
evening = [] 
day = []  

for i, temp in enumerate(temperatures):
    if i % 3 == 0: 
        night.append(temp)
    elif i % 3 == 1:  
        evening.append(temp)
    elif i % 3 == 2:  
        day.append(temp)

average_day_temp = sum(day) / len(day)
print(f"Average daytime temperature: {average_day_temp:.2f}°C")
