class Person:
    def __init__(self, first_name, last_name, is_female):
        # Represents a person with a first name, last name, and gender.
        self.first_name = first_name
        self.last_name = last_name
        self.is_female = is_female

    def is_female(self):
        # Returns True if the person is female, False otherwise.
        return self.is_female


class Mitarbeiter(Person):
    def __init__(self, first_name, last_name, is_female):
        # Represents an employee who is a person with a first name, last name, and gender.
        super().__init__(first_name, last_name, is_female)


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, first_name, last_name, is_female):
        # Represents a department leader who is an employee with a first name, last name, and gender.
        super().__init__(first_name, last_name, is_female)


class Abteilung:
    def __init__(self, name, employees, leader):
        # Represents a department with a name, employees, and a leader.
        self.name = name
        self.employees = employees
        self.leader = leader

    def get_name(self):
        # Returns the name of the department.
        return self.name

    def employee_count(self):
        # Returns the number of employees in the department, including the leader.
        return len(self.employees) + 1

    def female_count(self):
        # Returns the number of female employees in the department, including the leader.
        return (
            sum([employee.is_female for employee in self.employees])
            + self.leader.is_female
        )


class Firma:
    def __init__(self, name, departments):
        # Represents a company with a name and departments.
        self.name = name
        self.departments = departments

    def __str__(self):
        return (
            "Firma: "
            + self.name
            + " - Anzahl der Mitarbeiter: "
            + str(self.employee_count())
            + " - Anzahl der Abteilungen: "
            + str(self.department_count())
            + " - Groesste Abteilung: "
            + str(self.largest_department())
            + " - Frauenquote in %: "
            + str(self.female_employee_ratio() * 100)
        )

    def employee_count(self):
        # Returns the total number of employees in the company.
        return sum([department.employee_count() for department in self.departments])

    def department_count(self):
        # Returns the number of departments in the company.
        return len(self.departments)

    def largest_department(self):
        # Returns the largest department in the company based on the number of employees.
        max_department = ([], 0)
        for department in self.departments:
            name = department.get_name()
            employee_count = department.employee_count()
            if employee_count > max_department[1]:
                max_department = ([name], employee_count)
            elif department.employee_count() == max_department[1]:
                max_department[0].append(name)
        return max_department

    def female_employee_ratio(self):
        # Returns the ratio of female employees to total employees in the company.
        female_count = sum(
            [department.female_count() for department in self.departments]
        )
        return female_count / self.employee_count()
