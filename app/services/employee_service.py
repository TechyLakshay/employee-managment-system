# from app.database import get_db_connection
# from app.logger import get_logger
# from app.logger import logger, correlation_id_ctx

# SYSTEM_ID = "employee_api"

# logger = get_logger(__name__)

# def get_correlation_id():
#     return correlation_id_ctx.get()  # Retrieve the current correlation ID from context

# def create_employee(employee, user_id="system"):
#     correlation_id = get_correlation_id()
#     connection = None
#     cursor = None
#     try:
#         logger.debug(
#             f"Creating employee {employee.employee_id} | "
#             f"user_id={user_id} | system_id={SYSTEM_ID} | correlation_id={correlation_id}"
#         )

#         connection = get_db_connection()
#         cursor = connection.cursor()

#         query = """
#         INSERT INTO employees
#         (employee_id, name, age, department, manager_name, email, salary)
#         VALUES (%s, %s, %s, %s, %s, %s, %s)
#         """

#         cursor.execute(
#             query,
#             (
#                 employee.employee_id,
#                 employee.name,
#                 employee.age,
#                 employee.department,
#                 employee.manager_name,
#                 employee.email,
#                 employee.salary,
#             ),
#         )

#         connection.commit()

#         logger.info(
#             f"Employee created | employee_id={employee.employee_id} | correlation_id={correlation_id}"
#         )

#         return {"message": "Employee created successfully"}

#     except Exception as error:
#         logger.error(
#             f"Create failed | employee_id={employee.employee_id} | "
#             f"correlation_id={correlation_id} | error={error}"
#         )
#         return {"error": str(error)}

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#         logger.debug(f"DB closed for create_employee | correlation_id={correlation_id}")


# def get_all_employees(user_id="system"):
#     correlation_id = get_correlation_id()
#     connection = None
#     cursor = None
#     try:
#         logger.debug(
#             f"Fetching employees | user_id={user_id} | "
#             f"system_id={SYSTEM_ID} | correlation_id={correlation_id}"
#         )

#         connection = get_db_connection()
#         cursor = connection.cursor(dictionary=True)

#         cursor.execute("SELECT * FROM employees")
#         employees = cursor.fetchall()

#         logger.info(f"Fetched {len(employees)} employees | correlation_id={correlation_id}")

#         return employees

#     except Exception as error:
#         logger.error(f"Fetch failed | correlation_id={correlation_id} | error={error}")
#         return {"error": str(error)}

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#         logger.debug(f"DB closed for get_all_employees | correlation_id={correlation_id}")


# def update_employee(employee_id, employee, user_id="system"):
#     correlation_id = get_correlation_id()
#     connection = None
#     cursor = None
#     try:
#         logger.debug(
#             f"Updating employee {employee_id} | user_id={user_id} | correlation_id={correlation_id}"
#         )

#         connection = get_db_connection()
#         cursor = connection.cursor()

#         query = """
#         UPDATE employees
#         SET name=%s, age=%s, department=%s,
#             manager_name=%s, email=%s, salary=%s
#         WHERE employee_id=%s
#         """

#         cursor.execute(
#             query,
#             (
#                 employee.name,
#                 employee.age,
#                 employee.department,
#                 employee.manager_name,
#                 employee.email,
#                 employee.salary,
#                 employee_id,
#             ),
#         )

#         connection.commit()

#         if cursor.rowcount == 0:
#             logger.warning(
#                 f"No employee found | employee_id={employee_id} | correlation_id={correlation_id}"
#             )
#             return {"message": "Employee not found"}

#         logger.info(f"Employee updated | employee_id={employee_id} | correlation_id={correlation_id}")

#         return {"message": "Employee updated successfully"}

#     except Exception as error:
#         logger.error(
#             f"Update failed | employee_id={employee_id} | correlation_id={correlation_id} | error={error}"
#         )
#         return {"error": str(error)}

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#         logger.debug(f"DB closed for update_employee | correlation_id={correlation_id}")


# def delete_employee(employee_id,  user_id="system"):
#     correlation_id = get_correlation_id()
#     connection = None
#     cursor = None
#     try:
#         logger.debug(
#             f"Deleting employee {employee_id} | user_id={user_id} | correlation_id={correlation_id}"
#         )

#         connection = get_db_connection()
#         cursor = connection.cursor()

#         cursor.execute("DELETE FROM employees WHERE employee_id = %s", (employee_id,))

#         connection.commit()

#         if cursor.rowcount == 0:
#             logger.warning(
#                 f"No employee found to delete | employee_id={employee_id} | correlation_id={correlation_id}"
#             )
#             return {"message": "Employee not found"}

#         logger.info(f"Employee deleted | employee_id={employee_id} | correlation_id={correlation_id}")

#         return {"message": "Employee deleted successfully"}

#     except Exception as error:
#         logger.error(
#             f"Delete failed | employee_id={employee_id} | correlation_id={correlation_id} | error={error}"
#         )
#         return {"error": str(error)}

#     finally:
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#         logger.debug(f"DB closed for delete_employee | correlation_id={correlation_id}")

from app.database import get_db_connection
from app.observability.logger import get_logger

logger = get_logger(__name__)
SYSTEM_ID = "employee_api"


def create_employee(employee, user_id="system"):
    connection = None
    cursor = None

    try:
        logger.info(
            f"Creating employee | employee_id={employee.employee_id} | user_id={user_id}"
        )

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

        logger.info(f"Employee created successfully | employee_id={employee.employee_id}")
        return {"message": "Employee created successfully"}

    except Exception as error:
        logger.error(f"Create employee failed | error={error}")
        return {"error": str(error)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        logger.debug("DB connection closed (create_employee)")


def get_all_employees(user_id="system"):
    connection = None
    cursor = None

    try:
        logger.info("Fetching all employees")

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        logger.info(f"Fetched {len(employees)} employees")
        return employees

    except Exception as error:
        logger.error(f"Fetch employees failed | error={error}")
        return {"error": str(error)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        logger.debug("DB connection closed (get_all_employees)")


def update_employee(employee_id, employee, user_id="system"):
    connection = None
    cursor = None

    try:
        logger.info(f"Updating employee | employee_id={employee_id}")

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

        if cursor.rowcount == 0:
            logger.warning(f"Employee not found | employee_id={employee_id}")
            return {"message": "Employee not found"}

        logger.info(f"Employee updated | employee_id={employee_id}")
        return {"message": "Employee updated successfully"}

    except Exception as error:
        logger.error(f"Update failed | employee_id={employee_id} | error={error}")
        return {"error": str(error)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        logger.debug("DB connection closed (update_employee)")


def delete_employee(employee_id, user_id="system"):
    connection = None
    cursor = None

    try:
        logger.info(f"Deleting employee | employee_id={employee_id}")

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM employees WHERE employee_id=%s",
            (employee_id,),
        )

        connection.commit()

        if cursor.rowcount == 0:
            logger.warning(f"Employee not found | employee_id={employee_id}")
            return {"message": "Employee not found"}

        logger.info(f"Employee deleted | employee_id={employee_id}")
        return {"message": "Employee deleted successfully"}

    except Exception as error:
        logger.error(f"Delete failed | employee_id={employee_id} | error={error}")
        return {"error": str(error)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
        logger.debug("DB connection closed (delete_employee)")
