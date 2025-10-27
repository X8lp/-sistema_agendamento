# Criar ambiente virtual
python -m venv env

# Ativar o ambiente virtual
# Windows:
env\Scripts\activate
# Linux/Mac:
source env/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar a suíte de testes
pytest

# Exibir relatório de cobertura no terminal
pytest --cov=src --cov-report=term-missing

# Gerar relatório de cobertura em formato HTML
pytest --cov=src --cov-report=html
