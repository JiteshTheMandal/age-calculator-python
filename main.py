# Author: Jitesh Mandal
# Location: Delhi
# Date: 20-03-2023

import time
import json

people = {}


with open("info.json", "r") as info_json:
    people.update(json.load(info_json))


def update_file(u_name, dob):
    people.update({u_name: dob})
    with open("info.json", "w") as json_file:
        json_file.write(json.dumps(people, indent=5))
    print("Your data has been successfully saved for future use!")


def age_calc(name):
    if name in people.keys():
        diff_age = (int(time.time()) - people[name])
        print(f"You are {int(diff_age / (365.2425 * 24 * 60 * 60))} years old!")

    else:
        name = input("Enter Your Name: ")

        # Date Of Birth (Simplified)
        start_date = input("Please enter start date in DD\MM\YYYY format: ")
        end_date = int(time.time())

        # Converting user entered date to epoch
        try:
            start_date = int(time.mktime(time.strptime(start_date, "%d\%m\%Y")))
            save_bool = input("Do you want to save this info for future use? Yes(y), No(n): ")
            if save_bool.lower() == "y": 
                update_file(name, start_date)
            elif save_bool.lower() == "n":
                print("User Denied!")
        except Exception:
            print("Error calculating your age!")
            exit()

        if start_date < end_date:
            date_diff = end_date - start_date

            # Calculate age in years
            age_years = (date_diff / (365.2425 * 24 * 60 * 60))

            print(f"You are {int(age_years)} years old!")

age_calc("Jitesh")
