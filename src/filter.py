import fitz  # PyMuPDF
import os
import re

# Caminho do arquivo PDF
caminho_arquivo = r'C:\Users\hugod\OneDrive\Documentos\Pessoal\FREELAS\F01\Anais\anais-forum-sthem-brasil-2017.pdf'

# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print("Erro: O arquivo PDF nao foi encontrado. Verifique o caminho!")
else:
    # Função para ler o conteúdo do PDF e normalizar o texto
    def ler_documento(caminho):
        texto = ""
        with fitz.open(caminho) as pdf:
            for pagina in pdf:
                texto += pagina.get_text("text") + " "
        return " ".join(texto.split()) 

    # Extrai o texto do PDF
    texto = ler_documento(caminho_arquivo)

    # Lista de termos específicos
    termos_especificos = [
        
    ]

    # Função para contar as ocorrências exatas de cada termo
    def contar_ocorrencias(texto, termos):
        ocorrencias = {}
        texto_lower = texto.lower()
        for termo in termos:
            ocorrencias[termo] = len(re.findall(r'\b' + re.escape(termo.lower()) + r'\b', texto_lower))
        return ocorrencias

    # Função para encontrar a posição dos termos no texto
    def encontrar_posicoes(texto, termos):
        posicoes = []
        texto_lower = texto.lower()

        for termo in termos:
            termo_regex = r'\b' + re.escape(termo.lower()) + r'\b'
            for match in re.finditer(termo_regex, texto_lower):
                indice = len(texto_lower[:match.start()].split())  # Conta palavras antes da ocorrência
                posicoes.append(indice)

        return sorted(posicoes)  # Retorna os índices ordenados

    # Função para ajustar a contagem considerando proximidade (janela de 6 palavras)
    def ajustar_contagem_proximidade(texto, termos, janela):
        posicoes = encontrar_posicoes(texto, termos)
        grupos = []
        grupo_atual = []

        for i in range(len(posicoes)):
            if not grupo_atual:
                grupo_atual.append(posicoes[i])
            else:
                if posicoes[i] - grupo_atual[-1] <= janela:
                    grupo_atual.append(posicoes[i])
                else:
                    grupos.append(grupo_atual)
                    grupo_atual = [posicoes[i]]

        if grupo_atual:
            grupos.append(grupo_atual)
        return len(grupos)  #grupo conta como uma única ocorrência

    # Contagem inicial sem ajuste
    contagem_ocorrencias = contar_ocorrencias(texto, termos_especificos)

    # Ajusta a contagem removendo os termos próximos dentro de 6 palavras
    ocorrencias_ajustadas = ajustar_contagem_proximidade(texto, termos_especificos, janela=6)

    # Calcula o total ajustado corretamente
    total_ocorrencias_ajustado = sum(contagem_ocorrencias.values()) - (sum(contagem_ocorrencias.values()) - ocorrencias_ajustadas)

    # Exibir os resultados
    for termo, contagem in contagem_ocorrencias.items():
        print(f"O termo '{termo}' apareceu {contagem} vezes no documento.")

    print(f"\nTotal de ocorrencias ajustadas (removendo termos proximos dentro de 6 palavras): {total_ocorrencias_ajustado}")
