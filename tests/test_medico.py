import pytest
from src.medico import Medico


@pytest.fixture
def medico_base():
    return Medico("Dra. Ana", "Cardiologia")


def test_instanciacao_medico(medico_base):
    medico = medico_base
    assert medico.nome == "Dra. Ana"
    assert medico.especialidade == "Cardiologia"
    assert medico.agenda == []


def test_inserir_horario_valido(medico_base):
    medico = medico_base
    medico.adicionar_horario("2025-10-27 09:00")
    assert "2025-10-27 09:00" in medico.agenda


def test_bloquear_horario_repetido(medico_base):
    medico = medico_base
    medico.adicionar_horario("2025-10-27 10:00")
    with pytest.raises(ValueError):
        medico.adicionar_horario("2025-10-27 10:00")


def test_remocao_de_horario_existente(medico_base):
    medico = medico_base
    medico.adicionar_horario("2025-10-27 11:00")
    medico.remover_horario("2025-10-27 11:00")
    assert "2025-10-27 11:00" not in medico.agenda


def test_remocao_de_horario_inexistente(medico_base):
    medico = medico_base
    with pytest.raises(ValueError):
        medico.remover_horario("2025-10-28 08:00")


def test_verificacao_de_disponibilidade(medico_base):
    medico = medico_base
    medico.adicionar_horario("2025-10-27 13:00")
    assert medico.disponivel("2025-10-27 13:00") is True
    assert medico.disponivel("2025-10-27 14:00") is False
