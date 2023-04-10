import subprocess
import openai
from dotenv import load_dotenv
import os 

load_dotenv()

OPEN_AI_KEY = "OPEN_AI_KEY"

openai.api_key = os.getenv(OPEN_AI_KEY)
 
option = input("O que vai ser hoje? ")

prompt = f'''
         Escreva um comando em shell apenas se tiver 100% de certeza: 
         Context: "Eu tenho apenas 3 opcoes de pedido para fazer aqui na minha aplicação: Acai, pizza, hamburger", essas 3 opcoes podem ser digitadas completamente
         diferente, pode ser digitada em lowercase, uppercase, com pontuacao ou sem pontuacao.
         sabendo disso, na minha aplicação tem 3 scripts em python, um se chama, mini_kalzone.py que esta associado ao acai, o outro se chama, pizza.py e o outro se chama, hamburger.py
         Q: Escreva um comando shell para rodar o script em python baseado no que esse texto diz: "{option}" usando python3. 
         A:
         '''

def generate_command_shell(prompt): 
   response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      temperature=0.7,
      max_tokens=2048,
      n=1,
      stop=None
   )
   return response["choices"][0]["text"].strip()


def execute_command(command):
   try: 
       subprocess.run(command, shell=True, check=True)
   except subprocess.CalledProcessError as error:
      print(error)


def execute():
   command = generate_command_shell(prompt)
   execute_command(command)
   






 
