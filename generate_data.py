from faker import Faker
fake = Faker()
def generate_data():

    data = []

    for i in range(100):

        age = fake.random_int(min=20, max=60)

        gender = fake.random_element(elements=('Male', 'Female'))

        job_type = fake.random_element(elements=('Manager', 'Engineer', 'Salesperson', 'Accountant'))

        cups_per_day = fake.random_int(min=1, max=6)

        cups_per_week = cups_per_day * 5

        row = (i+1, age, gender, job_type, cups_per_day, cups_per_week)

        data.append(row)

    return data
import csv

 

data = generate_data()

 

with open('coffee_consumption_data.csv', mode='w', newline='') as file:

    writer = csv.writer(file)

    writer.writerow(['ID', 'Age', 'Gender', 'Job Type', 'Cups of Coffee Per Day', 'Cups of Coffee Per Week'])

    for row in data:

        writer.writerow(row)