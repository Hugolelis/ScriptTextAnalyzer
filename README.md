# 🚀 ScriptTextAnalyzer

![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg) ![Status](https://img.shields.io/badge/status-complete-brightgreen.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)


> Powerful and flexible script for lexical analysis of PDF files using natural language processing techniques.

---

## 📚 About

This script performs a basic lexiometric analysis on PDF files by extracting text and counting occurrences of specific terms within the content. It also adjusts the count to disregard multiple nearby occurrences (within a configurable word window), which helps avoid overlap in simple lexical analyses.

---

## 🧰 Tech Stack

- 🐍 Python 3.x  
- 📄 PyMuPDF (fitz) for PDF text extraction  
- 🔍 Regular expressions (regex) for term search and counting  

---

## 📂 Script Structure

- `ler_documento(caminho)`: reads and normalizes the text from the PDF  
- `contar_ocorrencias(texto, termos)`: counts exact occurrences of the terms  
- `encontrar_posicoes(texto, termos)`: finds positions of the occurrences in the text  
- `ajustar_contagem_proximidade(texto, termos, janela)`: adjusts the count to avoid counting very close terms more than once  

---

## ⚙️ How to Use

### 🔧 1. Set the PDF file path

```bash
caminho_arquivo = r'Path\To\Your\File.pdf'
```

### 📦 2. Define specific terms for analysis

```bash
termos_especificos = [
    "Social inclusion",
    "inclusion"
]
```

### ⚙️ 3. Run the script

```bash
O termo 'Social inclusion' apareceu 12 vezes no documento.
O termo 'inclusion' apareceu 25 vezes no documento.

Total de ocorrencias ajustadas (removendo termos proximos dentro de 6 palavras): 30

```
