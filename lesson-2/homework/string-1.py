name=input("Enter your name ")
year_of_birth=int(input("Enter your birth date "))
current_year=datetime.now().year
age=current_year-year_of_birth
print(f"Hello, {name}! you are {age} years old ")
