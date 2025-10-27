class Agendamento:
    def __init__(self, paciente: str, medico: str, horario: str):
        self.paciente = paciente
        self.medico = medico
        self.horario = horario
        self.status = "criado"

    def confirmar(self):
        if not self.paciente.ativo:
            raise ValueError("Paciente não se encontra ativo para agendamento.")
        
        if not self.medico.disponivel(self.horario):
            raise ValueError("O horário escolhido não está disponível para o médico informado.")
        
        self.medico.removerHorario(self.horario)
        self.status = "confirmado"

    def realizar(self):
        if self.status != "confirmado":
            raise ValueError("Não é possível realizar o procedimento sem confirmação prévia.")
        
        self.status = "realizado"

    def cancelar(self):
        if self.status == "realizado":
            self.status = "realizado"
        else:
            self.status = "cancelado"
