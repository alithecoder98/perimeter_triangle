def perimeter():
    print("Calculate the perimeter of a triangle.")
    s1 = float(input("Enter side 1: "))
    s2 = float(input("Enter side 2: "))
    s3 = float(input("Enter side 3: "))

    pm = s1 + s2 + s3
    print(f"The perimeter of the triangle is: {pm}")

    # Ask the user if they want to calculate another perimeter
    again = input("Do you want to calculate another perimeter? (yes/no): ").strip().lower()
    if again == "yes":
        perimeter()  # Recursive call to start over
    else:
        print("Goodbye!")

if __name__ == "__main__":
    perimeter()
