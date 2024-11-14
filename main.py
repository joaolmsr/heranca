from datetime import datetime

class Funcionario:
  def __init__(self, nome:str, cpf:str, email:str, telefone: str, salario:float) -> None:
    self.nome = nome
    self.cpf = cpf
    self.email = email
    self.telefone = telefone
    self.salario = salario

  def BaterPonto(self):
      agora = datetime.now()
      print(f'o funcionário {self.nome} bateu o ponto às {agora.hour}:{agora.minute}')
  def ReceberSalario(self):
      print(f'o funcionário {self.nome}, foi pago ({self.salario})')
  def almocar(self):
      print(f'{self.nome} está de bucho cheio')

class Gerente(Funcionario):
  def __init__(self, nome: str, cpf: str, email: str, telefone: str, salario: float) -> None:
    super().__init__(nome, cpf, email, telefone, salario)

  def Contratar(self, funcionario):
    print(f'{self.nome} contratou o funcionário {funcionario.nome}')

  def Demitir(self, funcionario):
    print(f'{self.nome} demitiu o funcionário {funcionario.nome}')
  
class GarotoDePrograma(Funcionario):
  def __init__(self, nome: str, cpf: str, email: str, telefone: str, salario: float, stack: str, linguagem_dominio: str) -> None:
    super().__init__(nome, cpf, email, telefone, salario)
    self.stack = stack
    self.linguagem_dominio = linguagem_dominio

  def MarcarReuniao(self):
    print(f'{self.nome} está com uma reunião marcada')

class Estagiario(Funcionario):
  def __init__(self, nome: str, cpf: str, email: str, telefone: str, salario: float, carga_horaria: str) -> None:
    super().__init__(nome, cpf, email, telefone, salario)
    self.carga_horaria = carga_horaria

class Atendente(Funcionario):
  def __init__(self, nome: str, cpf: str, email: str, telefone: str, salario: float) -> None:
    super().__init__(nome, cpf, email, telefone, salario)











