import csv

main_str = input()

name = main_str[15:-3]
age = main_str[-2:]

row1 = ['name', 'age']
row2 = [name, age]

with open('trainee.csv','w', newline='') as write_file:
    write_data = csv.writer(write_file)
    write_data.writerow(row1)
    write_data.writerow(row2)



