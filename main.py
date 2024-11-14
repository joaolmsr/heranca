from datetime import datetime

class Employee:
  def __init__(self, name:str, cpf:str, email:str, number: str, salary:float) -> None:
    self.name = name
    self.cpf = cpf
    self.email = email
    self.number = number
    self.salary = salary

  def Presence(self):
      now = datetime.now()
      print(f'o funcionário {self.name} bateu o ponto às {now.hour}:{now.minute}')
  def ReceiveSalary(self):
      print(f'o funcionário {self.name}, foi pago ({self.salary})')
  def HaveLunch(self):
      print(f'{self.name} está de bucho cheio')

class Manager(Employee):
  def __init__(self, name: str, cpf: str, email: str, number: str, salary: float) -> None:
    super().__init__(name, cpf, email, number, salary)

  def Hire(self, employee):
    print(f'{self.name} contratou o funcionário {employee.name}')

  def Dismiss(self, employee):
    print(f'{self.name} demitiu o funcionário {employee.name}')
  
class Programmer(Employee):
  def __init__(self, name: str, cpf: str, email: str, number: str, wage: float, stack: str, domain_language: str) -> None:
    super().__init__(name, cpf, email, number, wage)
    self.stack = stack
    self.domain_language = domain_language

  def ScheduleMeeting(self, day: int, hour:int):
    print(f'{self.name} está com uma reunião marcada para o dia {day}, às {hour} horas')

class Trainee(Employee):
  def __init__(self, name: str, cpf: str, email: str, number: str, wage: float, workload: str) -> None:
    super().__init__(name, cpf, email, number, wage)
    self.workload = workload

class Attendant(Employee):
  def __init__(self, name: str, cpf: str, email: str, number: str, wage: float) -> None:
    super().__init__(name, cpf, email, number, wage)
