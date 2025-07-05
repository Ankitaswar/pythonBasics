#install mysql-> add path to.zprofile or .zshrc
# install (connector) to connect mysql with code : pip install mysql-connector

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Ankit123@',
    database='telusko'  # optional
)

cursor = conn.cursor()

# 1. CREATE Table (only run once)
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10)
        )
    """)
    conn.commit()
    print("Table created")

# 2. INSERT (Create)
def insert_student(name, age, grade):
    query = "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    print("Student inserted")

# 3. SELECT (Read)
def fetch_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    for row in results:
        print(row)

def fetch_One_students():
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchone()
    print("Fetch One Data ", results)

# 4. UPDATE
def update_student(student_id, new_name):
    query = "UPDATE students SET name = %s WHERE id = %s"
    cursor.execute(query, (new_name, student_id))
    conn.commit()
    print("Student updated")

# 5. DELETE
def delete_student(student_id):
    query = "DELETE FROM students WHERE id = %s"
    cursor.execute(query, (student_id,))
    conn.commit()
    print("Student deleted")

# Example usage:
create_table()
insert_student("John", 18, "A")
insert_student("Emma", 20, "B")
fetch_students()
fetch_One_students()
update_student(1, "Johnny")
delete_student(2)
fetch_students()

# Close the connection
cursor.close()
conn.close()

