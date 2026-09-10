import os
import glob
import google.generativeai as genai

# Conecta na API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro')

# LER AS REGRAS QUE JÁ ESTÃO NO SEU GITHUB
caminho_regras = 'editorial/GLOBAL_WRITING_RULES.md'

try:
    with open(caminho_regras, 'r', encoding='utf-8') as f:
        regras = f.read()
except FileNotFoundError:
    print(f"Erro: O arquivo de regras '{caminho_regras}' não foi encontrado.")
    exit(1)

# LER O CAPÍTULO DO GEPETO
pasta_manuscrito = 'projects/o-futuro-onde-te-perco/manuscript/'
arquivos_capitulos = glob.glob(os.path.join(pasta_manuscrito, '*.md'))

if not arquivos_capitulos:
    # Se não achar nada no manuscrito, pega o README só pra não dar erro e a gente ver funcionar
    caminho_capitulo = 'README.md' 
else:
    caminho_capitulo = arquivos_capitulos[0]

with open(caminho_capitulo, 'r', encoding='utf-8') as f:
    capitulo = f.read()

# Manda pra API
prompt = f"""Você é um auditor de continuidade impiedoso. 
Com base nestas regras globais de escrita: \n{regras}\n
Analise este texto: \n{capitulo}"""

response = model.generate_content(prompt)
print(f"--- RELATÓRIO DO ARQUIVO: {caminho_capitulo} ---")
print(response.text)
