import application.salary as salary
import application.db.people as people
import datetime


def return_date_now():
    """Возвращает текущую дату"""
    date_now = datetime.datetime.now().strftime('%d.%m.%Y')
    return date_now


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(return_date_now())
