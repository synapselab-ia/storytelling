import os
import glob
import google.generativeai as genai

# Conecta na API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro')

# Lê as suas regras base
try:
    with open('Storytelling', 'r', encoding='utf-8') as f:
        regras = f.read()
except FileNotFoundError:
    print("Erro: O arquivo 'Storytelling' não foi encontrado na raiz do projeto.")
    exit(1)

# Procura o arquivo do capítulo na pasta correta do seu projeto
pasta_manuscrito = 'projects/o-futuro-onde-te-perco/manuscript/'
arquivos_capitulos = glob.glob(os.path.join(pasta_manuscrito, '*.md'))

if not arquivos_capitulos:
    print(f"Erro: O auditor não achou nenhum arquivo de capítulo dentro de {pasta_manuscrito}")
    exit(1)

# Pega o capítulo que está na pasta (estou pegando o primeiro da lista para o teste)
caminho_capitulo = arquivos_capitulos[0]

with open(caminho_capitulo, 'r', encoding='utf-8') as f:
    capitulo = f.read()

# Manda pra API
prompt = f"""Você é um auditor de continuidade impiedoso. 
Com base nas seguintes regras narrativas: \n{regras}\n
Analise este novo capítulo e aponte todos os erros, furos de roteiro e quebras de estilo cometidos pela outra IA: \n{capitulo}"""

response = model.generate_content(prompt)
print(f"--- RELATÓRIO DO ARQUIVO: {caminho_capitulo} ---")
print(response.text)
