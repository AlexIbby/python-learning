# Write your solution here

no_of_students = int(input("How many students on the course? "))
desired_group_size = int(input("Desired group size?"))

no_of_groups = no_of_students // desired_group_size 

modulo_check = no_of_students % desired_group_size 

if modulo_check > 0:
    no_of_groups += 1

print(f"Number of groups formed: {no_of_groups}")