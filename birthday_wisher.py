import smtplib
import random
import datetime
import pandas

my_email = "example@example.com"

now = datetime.datetime.now()
birthdays_csv = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays_csv.to_dict()
months = birthdays_dict["month"]
days = birthdays_dict["day"]
for key, value in months.items():
    if days[key] == now.day and months[key] == now.month:
        with open("letter_templates/letter_1.txt") as file:
            letter_1 = file.read()
        with open("letter_templates/letter_2.txt") as file:
            letter_2 = file.read()
        with open("letter_templates/letter_3.txt") as file:
            letter_3 = file.read()

        list_of_letters = [letter_1, letter_2, letter_3]
        letter = random.choice(list_of_letters)
        letter = letter.replace("[NAME]", f"{birthdays_dict['name'][key]}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, "password")
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthdays_dict['email'][key],
                                msg=f"Subject:Happy Birthday!\n\n{letter}")
