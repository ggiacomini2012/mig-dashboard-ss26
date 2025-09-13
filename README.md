# 📊 Dashboard de Produtos - Coleção Spring Summer 2026

Dashboard dinâmico e interativo construído com **React** para a coleção de moda **Spring Summer 2026**, com o tema *"A Gente Sempre Volta Pro Mar"*. Este projeto organiza os produtos em um layout moderno e responsivo, facilitando a visualização e gestão da coleção.

## ✨ Funcionalidades Principais

* **Renderização Dinâmica:** Os produtos são carregados dinamicamente a partir de um arquivo de dados, tornando a atualização do catálogo simples.
* **Cards de Produtos Detalhados:** Cada produto possui um card com:
    * Foto do produto
    * Nome e Referência (SKU)
    * Tecido ou material
    * Cores disponíveis
    * Preço
* **Design Responsivo:** A interface se adapta perfeitamente a desktops, tablets e celulares, utilizando **Tailwind CSS**.
* **Scripts de Automação:**
    * `extrator_de_imagens.py`: Extrai imagens de um catálogo PDF.
    * `gerar_dados.py`: Consolida informações de um arquivo Excel e das imagens extraídas em um único `products.json` para o frontend.

## 🛠️ Tecnologias Utilizadas

* **Frontend:**
    * React (com Vite)
    * [Tailwind CSS](https://tailwindcss.com/)
* **Ferramentas e Scripts:**
    * Python 3
    * `PyMuPDF` para extração de imagens de PDF
    * `Pandas` para leitura de arquivos Excel

## 🚀 Como Executar o Projeto

O fluxo de trabalho consiste em preparar os dados (extrair imagens e gerar o JSON) e depois rodar a aplicação React.

1.  **Clone o repositório e configure o ambiente Python:**
    ```
    git clone [URL_DO_SEU_REPOSITORIO]
    cd dashboard-ss26
    ```
    
    Crie e ative um ambiente virtual:
    ```
    # Criar o ambiente
    python -m venv .venv

    # Ativar no Windows (Git Bash) ou macOS/Linux
    source .venv/Scripts/activate
    ```

    Instale as dependências do Python:
    ```
    pip install -r requirements.txt
    ```

2.  **Prepare os Dados dos Produtos:**
    * **(Opcional) Extraia as imagens:** Se precisar extrair as imagens do PDF novamente, coloque o `Catálogo SS26_compressed.pdf` na raiz e execute:
      ```
      python extrator_de_imagens.py
      ```
      As imagens serão salvas em `imagens_extraidas/`.
    * **Gere o arquivo de dados:** Coloque o arquivo `Lista-produtos-SS26.xlsx` na raiz do projeto e execute o script para gerar o JSON:
      ```
      python gerar_dados.py
      ```
      Isso criará o arquivo `frontend/public/products.json`.

3.  **Execute a Aplicação React:**
    Navegue até a pasta do frontend, instale as dependências e inicie o servidor de desenvolvimento:
    ```bash
    cd frontend
    npm install
    npm run dev
    ```
    Abra o navegador no endereço fornecido (geralmente `http://localhost:5173`).

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