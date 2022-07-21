number_of_students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
no_of_groups = ((number_of_students // group_size) + (number_of_students % group_size >0))

print(f"Number of groups formed: {no_of_groups}")

