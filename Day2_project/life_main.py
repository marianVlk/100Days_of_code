
age = input("What is your age: ")

age_as_int = int(age)

years_remain= 90 - age_as_int
days_re = years_remain * 365
week_r = years_remain * 52
months_r = years_remain * 12

mesaj = f"You have {days_re} days, {week_r} weeks, {months_r} mounts remaining."
print(mesaj)