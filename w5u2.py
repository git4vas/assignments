def get_student_data():
    last_name = input("l_name")
    first_name = input("name")
    student_id = input("st_id")
    return (last_name, first_name, student_id)
student_data = get_student_data()
print(student_data)