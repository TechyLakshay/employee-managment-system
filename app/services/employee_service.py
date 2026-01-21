from app.database import get_db_connection


def create_employee(employee):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO employees
        (employee_id, name, age, department, manager_name, email, salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                employee.employee_id,
                employee.name,
                employee.age,
                employee.department,
                employee.manager_name,
                employee.email,
                employee.salary,
            ),
        )

        connection.commit()
        return {"message": "Employee created successfully"}

    except Exception as error:
        return {"error": str(error)}

    finally:
        cursor.close()
        connection.close()


def get_all_employees():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        return employees

    except Exception as error:
        return {"error": str(error)}

    finally:
        cursor.close()
        connection.close()


def update_employee(employee_id, employee):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        UPDATE employees
        SET name=%s, age=%s, department=%s,
            manager_name=%s, email=%s, salary=%s
        WHERE employee_id=%s
        """

        cursor.execute(
            query,
            (
                employee.name,
                employee.age,
                employee.department,
                employee.manager_name,
                employee.email,
                employee.salary,
                employee_id,
            ),
        )

        connection.commit()
        return {"message": "Employee updated successfully"}

    except Exception as error:
        return {"error": str(error)}

    finally:
        cursor.close()
        connection.close()


def delete_employee(employee_id):
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id = %s",
            (employee_id,),
        )

        connection.commit()
        return {"message": "Employee deleted successfully"}

    except Exception as error:
        return {"error": str(error)}

    finally:
        cursor.close()
        connection.close()
