class Seseorang:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Address:", self.address)

# Single Inheritance
class Dosen(Seseorang):
    def __init__(self, name, age, address, nip):
        super().__init__(name, age, address)
        self.nip = nip

    def get_info(self):
        super().get_info()
        print("Student ID:", self.nip)

# Single Inheritance
class Employee(Seseorang):
    def __init__(self, name, age, address, employee_id, salary):
        super().__init__(name, age, address)
        self.employee_id = employee_id
        self.salary = salary

    def get_info(self):
        super().get_info()
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)

# Multiple Inheritance
class Penulis(Employee, Dosen):
    def __init__(self, name, age, address, employee_id, salary, nip, published_books):
        Employee.__init__(self, name, age, address, employee_id, salary)
        Dosen.__init__(self, name, age, address, nip)
        self.published_books = published_books
        
    def get_info(self):
        super().get_info()
        print("NIP:", self.nip)
        print("Published Books:", self.published_books)