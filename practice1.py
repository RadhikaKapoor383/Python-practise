passengers = ["Ali", "Sana", "Usman", "Hina"]
print(passengers[-1])
print(passengers[0])
print(passengers[1:3])
print(passengers)

passengers.append("Bilal")
print(passengers)
passengers.remove("Usman")
print(passengers)
passengers.insert(1, "Fatima")
i = 1
for name in passengers:
    print(f"Passenger {i}: {name}")
    i+=1
    
ages = [22, 45, 17, 31, 8, 55]
adults = [age for age in ages if age >= 18]
print(adults)