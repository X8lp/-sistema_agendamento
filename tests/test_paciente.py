import pytest
from src.paciente import Paciente


def test_instanciar_paciente_ativo():
   
    pessoa = Paciente("Maria", "12345678901")
    assert pessoa.nome == "Maria"
    assert pessoa.cpf == "12345678901"
    assert pessoa.ativo is True


def test_instanciar_paciente_inativo():
    
    pessoa = Paciente("João", "98765432100", ativo=False)
    assert pessoa.nome == "João"
    assert pessoa.ativo is False


def test_cpf_com_caracteres_invalidos():
   
    with pytest.raises(ValueError):
        Paciente("Carlos", "abc45678901")


def test_cpf_com_tamanho_reduzido():
   
    with pytest.raises(ValueError):
        Paciente("Ana", "12345")


def test_cpf_com_tamanho_excedente():
   
    with pytest.raises(ValueError):
        Paciente("Pedro", "1234567890123")
