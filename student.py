from database import get_connection


def add_student():

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    age = int(input("Enter Age: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO students
        (Student_Name, Department, Email, Phone, Age)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, department, email, phone, age)

    cursor.execute(query, values)
    connection.commit()

    print("Student added successfully!")

    cursor.close()
    connection.close()


def view_students():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("\n========== STUDENT LIST ==========")

    if not students:
        print("No student records found.")

    else:
        for student in students:
            print(
                f"ID: {student[0]} | "
                f"Name: {student[1]} | "
                f"Department: {student[2]} | "
                f"Email: {student[3]} | "
                f"Phone: {student[4]} | "
                f"Age: {student[5]}"
            )

    cursor.close()
    connection.close()


def search_student():

    student_id = int(input("Enter Student ID: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT *
        FROM students
        WHERE Student_ID = %s
    """

    cursor.execute(query, (student_id,))

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Department:", student[2])
        print("Email:", student[3])
        print("Phone:", student[4])
        print("Age:", student[5])

    else:
        print("Student not found.")

    cursor.close()
    connection.close()


def update_student():

    student_id = int(input("Enter Student ID to update: "))

    connection = get_connection()
    cursor = connection.cursor()

    check_query = """
        SELECT *
        FROM students
        WHERE Student_ID = %s
    """

    cursor.execute(check_query, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        cursor.close()
        connection.close()
        return

    name = input("Enter New Name: ")
    department = input("Enter New Department: ")
    email = input("Enter New Email: ")
    phone = input("Enter New Phone: ")
    age = int(input("Enter New Age: "))

    query = """
        UPDATE students
        SET Student_Name = %s,
            Department = %s,
            Email = %s,
            Phone = %s,
            Age = %s
        WHERE Student_ID = %s
    """

    values = (
        name,
        department,
        email,
        phone,
        age,
        student_id
    )

    cursor.execute(query, values)
    connection.commit()

    print("Student updated successfully!")

    cursor.close()
    connection.close()


def delete_student():

    student_id = int(input("Enter Student ID to delete: "))

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        DELETE FROM students
        WHERE Student_ID = %s
    """

    cursor.execute(query, (student_id,))

    if cursor.rowcount > 0:
        connection.commit()
        print("Student deleted successfully!")

    else:
        print("Student not found.")

    cursor.close()
    connection.close()