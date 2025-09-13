# 📊 Dashboard de Produtos - Coleção Spring Summer 2026

Dashboard visual e interativo para a coleção de moda **Spring Summer 2026**, com o tema *"A Gente Sempre Volta Pro Mar"*. Este projeto organiza os produtos das categorias Feminino, Masculino e Acessórios em um layout moderno e responsivo, facilitando a visualização e gestão da coleção.

## ✨ Funcionalidades Principais

* **Visualização por Categorias:** Navegue facilmente entre as seções Feminino, Masculino e Acessórios.
* **Cards de Produtos Detalhados:** Cada produto possui um card com:
    * Foto do produto
    * Nome e Referência (SKU)
    * Tecido ou material
    * Cores disponíveis
    * Preço
* **Design Responsivo:** A interface se adapta perfeitamente a desktops, tablets e celulares, graças ao **Tailwind CSS**.
* **Script de Extração de Imagens:** Inclui um script em Python (`extrator_de_imagens.py`) que extrai todas as imagens do catálogo PDF original de forma automática.

## 🛠️ Tecnologias Utilizadas

* **Frontend:**
    * HTML5
    * [Tailwind CSS](https://tailwindcss.com/)
* **Ferramentas e Scripts:**
    * Python 3
    * Biblioteca `PyMuPDF` para manipulação de PDFs

## 🚀 Como Executar o Projeto

Existem duas partes neste projeto: a visualização do dashboard e a extração das imagens do catálogo.

### 1. Visualizando o Dashboard

Nenhuma instalação é necessária. Basta abrir o arquivo `dashboard_produtos.html` em qualquer navegador de internet.

### 2. Extraindo as Imagens do Catálogo PDF

Para usar o script que extrai as imagens, você precisará do Python configurado no seu computador.

1.  **Clone este repositório:**
    ```
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```

2.  **Crie e ative um ambiente virtual (venv):**
    ```
    # Criar o ambiente
    python -m venv venv

    # Ativar no Windows (Git Bash) ou macOS/Linux
    source venv/Scripts/activate
    ```

3.  **Instale as dependências necessárias:**
    ```
    pip install -r requirements.txt
    ```

4.  **Execute o script:**
    * Coloque o arquivo `Catálogo SS26_compressed.pdf` na pasta principal do projeto.
    * Execute o script para extrair as imagens:
        ```
        python extrator_de_imagens.py
        ```
    * As imagens serão salvas na pasta `/imagens_do_catalogo`.

## 📂 Estrutura do Projeto

```
.
├── dashboard_produtos.html     # O arquivo principal do dashboard
├── extrator_de_imagens.py      # Script para extrair imagens do PDF
├── requirements.txt            # Dependências do script Python
├── README.md                   # Esta descrição
└── imagens_do_catalogo/        # Pasta onde as imagens extraídas são salvas
```

## 📄 Fonte dos Dados

Todas as informações sobre os produtos (nomes, preços, tecidos, etc.) e as imagens foram extraídas dos seguintes documentos PDF:

* `Catálogo SS26_compressed.pdf`
* `Lista produtos SS26 - femininos.pdf`
* `Lista produtos SS26 - masculino.pdf`
* `Lista produtos SS26 - acessorios.pdf`