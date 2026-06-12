import sqlite3
def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()
def insert_student(name: str, marks: float):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
    conn.commit()
    conn.close()
def get_all_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return students
def get_student_by_id(student_id: int):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    student = cursor.fetchone()
    conn.close()
    return student
def update_marks(student_id: int, new_marks: float):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )
    conn.commit()
    conn.close()
def delete_student(student_id: int):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()
    conn.close()
def get_students_above(threshold: float):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )
    students = cursor.fetchall()
    conn.close()
    return students
create_table()
insert_student("Adila", 95)
insert_student("John", 70)
insert_student("Sara", 88)
print("All Students:")
print(get_all_students())
print("\nStudent ID 1:")
print(get_student_by_id(1))
update_marks(2, 80)
print("\nAfter Updating Marks:")
print(get_all_students())
print("\nStudents Above 85:")
print(get_students_above(85))
delete_student(3)
print("\nAfter Deleting Student:")
print(get_all_students())