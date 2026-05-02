# pdf-utils

Biblioteca Python para manipulação de arquivos PDF. Fornece funcionalidades para dividir, unir e reorganizar páginas de PDFs de forma simples e intuitiva.

## Características

- 📄 **Dividir PDFs**: Extraia páginas específicas de um PDF para writers individuais
- 🔗 **Unir PDFs**: Combine múltiplos writers em um único PDF
- 💾 **Salvar com flexibilidade**: Exporte seus PDFs em pastas customizadas
- 🔄 **Reorganizar páginas**: Reordene páginas facilmente antes de salvar

## Requisitos

- Python 3.6+
- pypdf

## Instalação

### Usando pip

```bash
pip install -r requirements.txt
```

## Uso Rápido

### Exemplo Básico

```python
from pdf import PDF

# Criar instância com um arquivo PDF
pdf = PDF("meu_documento.pdf")

# Dividir o PDF em páginas individuais
pdf.split('primeira_pagina', start=0, end=1)
pdf.split('segunda_pagina', start=1, end=2)

# Unir os writers
pdf.join(['primeira_pagina', 'segunda_pagina'])

# Salvar o resultado
pdf.save("documento_final", output_folder="output")
```

## API

### Classe `PDF`

#### `__init__(path: str)`

Inicializa uma instância da classe PDF com um arquivo PDF existente.

**Parâmetros:**
- `path` (str): Caminho para o arquivo PDF a ser processado

**Exemplo:**
```python
pdf = PDF("documento.pdf")
```

#### `split(writer_name: str, start: int = 0, end: int = None)`

Divide o PDF em um novo writer contendo as páginas especificadas.

**Parâmetros:**
- `writer_name` (str): Nome identificador para o novo writer
- `start` (int): Índice da primeira página (padrão: 0)
- `end` (int): Índice da última página (padrão: última página do PDF)

**Exemplo:**
```python
# Extrair páginas 5 a 10
pdf.split('paginas_5_a_10', start=5, end=10)

# Extrair apenas a primeira página
pdf.split('capa', start=0, end=1)

# Extrair da página 5 até o final
pdf.split('resto_documento', start=5)
```

#### `join(writers: List[str])`

Une múltiplos writers em um único PDF na ordem especificada.

**Parâmetros:**
- `writers` (List[str]): Lista com os nomes dos writers a unir, em ordem

**Exemplo:**
```python
pdf.join(['capa', 'paginas_5_a_10', 'contrapage'])
```

#### `save(filename: str, output_folder: str = ".")`

Salva o PDF processado em arquivo.

**Parâmetros:**
- `filename` (str): Nome do arquivo (sem extensão .pdf)
- `output_folder` (str): Pasta de destino (padrão: diretório atual)

**Exemplo:**
```python
# Salvar na pasta atual
pdf.save("documento_final")

# Salvar em pasta específica
pdf.save("documento_final", output_folder="output")
```

## Exemplo Completo

Para um exemplo prático de uso, veja `example.py` que demonstra como:

1. Extrair a capa de um PDF
2. Dividir o PDF em múltiplas seções
3. Reordenar as seções
4. Salvar o resultado

```bash
python example.py
```

## Estrutura do Projeto

```
pdf-utils/
├── pdf.py           # Classe principal PDF
├── example.py       # Exemplo de uso
├── requirements.txt # Dependências
├── setup.py         # Configuração do pacote
├── pyproject.toml   # Configuração do projeto
└── README.md        # Este arquivo
```

## Testes

Execute os testes com:

```bash
pytest
```

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contribuindo

Contribuições são bem-vindas! Sinta-se livre para abrir issues ou pull requests.
