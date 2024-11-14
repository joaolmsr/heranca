from main import *


gerente = Manager(nome="Ana Silva", cpf="123.456.789-00", email="ana.silva@empresa.com", telefone="11987654321", salario=8000)

# Programador
programador = Programmer(nome="Carlos Souza", cpf="987.654.321-00", email="carlos.souza@empresa.com", telefone="11912345678", salario=5000, stack="Backend", linguagem_dominio="Python")

# Estagiário
estagiario = Trainee(nome="João Santos", cpf="321.654.987-00", email="joao.santos@empresa.com", telefone="11923456789", salario=1500, carga_horaria="6 horas")

# Atendente
atendente = Attendant(nome="Maria Oliveira", cpf="654.321.987-00", email="maria.oliveira@empresa.com", telefone="11934567890", salario=2500)

# Testando os métodos

# Gerente contratando e demitindo
gerente.Hire(programador)
gerente.Dismiss(atendente)

# Programador marcando reunião
programador.MarcarReuniao()

# Estagiário batendo ponto, recebendo salário e indo almoçar
estagiario.BaterPonto()
estagiario.ReceberSalario()
estagiario.almocar()

# Atendente batendo ponto e recebendo salário
atendente.BaterPonto()
atendente.ReceberSalario()
