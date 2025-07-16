def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("C. Celsius F. Fahrenheit")
    choice = input("Choose conversion (C/F): ").strip().lower()

    if choice == 'c':
        c = float(input("Enter temperature in Celsius: "))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")
    elif choice == 'f':
        f = float(input("Enter temperature in Fahrenheit: "))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.2f}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()