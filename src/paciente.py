class Paciente:
    def __init__(self, nome: str, cpf: str, ativo: bool = True):
        if not (cpf.isdigit() and len(cpf) == 11):
            raise ValueError("O CPF informado deve conter exatamente 11 dígitos numéricos.")
        
        self.nome = nome
        self.cpf = cpf
        self.ativo = ativo
