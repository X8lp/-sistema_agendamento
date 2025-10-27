import pytest
from src.agendamento import Agendamento


class PacienteSimulado:
    def __init__(self, nome, ativo=True):
        self.nome = nome
        self.ativo = ativo


class MedicoSimulado:
    def __init__(self, nome):
        self.nome = nome
        self.horarios_disponiveis = ["2025-10-26 09:00"]

    def disponivel(self, horario):
        return horario in self.horarios_disponiveis

    def remover_horario(self, horario):
        if horario not in self.horarios_disponiveis:
            raise ValueError("Este horário não consta na agenda.")
        self.horarios_disponiveis.remove(horario)


@pytest.fixture
def ambiente_base():
    paciente = PacienteSimulado("João", ativo=True)
    medico = MedicoSimulado("Dra. Paula")
    agenda = Agendamento(paciente, medico, "2025-10-26 09:00")
    return agenda, paciente, medico


def test_confirmacao_valida(ambiente_base):
    agenda, paciente, medico = ambiente_base
    agenda.confirmar()
    assert agenda.status == "confirmado"
    assert "2025-10-26 09:00" not in medico.horarios_disponiveis


def test_confirmacao_paciente_inativo(ambiente_base):
    agenda, paciente, medico = ambiente_base
    paciente.ativo = False
    with pytest.raises(ValueError):
        agenda.confirmar()


def test_confirmacao_medico_sem_horario(ambiente_base):
    agenda, paciente, medico = ambiente_base
    medico.horarios_disponiveis = []
    with pytest.raises(ValueError):
        agenda.confirmar()


def test_realizacao_sem_confirmacao(ambiente_base):
    agenda, paciente, medico = ambiente_base
    with pytest.raises(ValueError):
        agenda.realizar()


def test_realizacao_apos_confirmacao(ambiente_base):
    agenda, paciente, medico = ambiente_base
    agenda.confirmar()
    agenda.realizar()
    assert agenda.status == "realizado"


def test_cancelamento_agendamento_confirmado(ambiente_base):
    agenda, paciente, medico = ambiente_base
    agenda.confirmar()
    agenda.cancelar()
    assert agenda.status == "cancelado"


def test_cancelamento_agendamento_realizado(ambiente_base):
    agenda, paciente, medico = ambiente_base
    agenda.confirmar()
    agenda.realizar()
    agenda.cancelar()
    assert agenda.status == "realizado"
