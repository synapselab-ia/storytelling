import os
import google.generativeai as genai

# Conecta com a chave que escondemos no GitHub
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-pro')

# Lê as suas regras de narrativa e o texto gerado
with open('Storytelling', 'r', encoding='utf-8') as f:
    regras = f.read()
    
with open('capitulos/novo_capitulo.md', 'r', encoding='utf-8') as f:
    capitulo = f.read()

prompt = f"""Você é um auditor de continuidade impiedoso. 
Com base nas seguintes regras narrativas: \n{regras}\n
Analise este novo capítulo e aponte todos os erros, furos de roteiro e quebras de estilo cometidos pela outra IA: \n{capitulo}"""

response = model.generate_content(prompt)
print(response.text)
