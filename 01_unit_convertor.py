def unit_converter():
  print("Unit Convertor Program:")
  print("1. Length(m to km, km to m)")
  print("2. Weight(kg to lbs, lbs to kg)")
  print("3. Temprature(C to F, F to C )")

  choice = input("choice a conversion(1,2 or 3):").strip()

  if choice== "1":
    unit_type=input("convert from m to km or km to m:")
    value=float(input("Enter the value:"))
    if unit_type=="m to km":
      print(f"({value} meters={value/1000} kilometers)")
    elif unit_type=="km to m":
      print(f"({value} kilometers={value/1000} meters)")

  elif choice == "2":
    unit_type = input("Convert from 'kg to lbs' or 'lbs to kg': ").strip().lower()
    value = float(input("Enter the value: "))

    if unit_type == "kg to lbs":
        print(f"{value} kilograms = {value * 2.20462:.2f} pounds")

    elif unit_type == "lbs to kg":
        print(f"{value} pounds = {value / 2.20462:.2f} kilograms")

    else:
        print("Invalid unit type.")



  elif choice == "3":
    unit_type = input("Convert from 'C to F' or 'F to C': ").strip().lower()
    value = float(input("Enter the value: "))

    if unit_type == "c to f":
        fahrenheit = (value * 9/5) + 32
        print(f"{value}°C = {fahrenheit:.2f}°F")

    elif unit_type == "f to c":
        celsius = (value - 32) * 5/9
        print(f"{value}°F = {celsius:.2f}°C")

    else:
        print("Invalid unit type.")





unit_converter()











