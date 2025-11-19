import os
import time
import mysql.connector

print("[1] variáveis de ambiente...")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = int(os.getenv("MYSQL_PORT"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

print("[2] Aguardando MySQL iniciar...")

for tent in range(20):
    try:
        conn = mysql.connector.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE
        )
        print("✓ MySQL conectado!\n")
        break
    except Exception as e:
        print(f"Tentativa {tent+1}/20: MySQL não disponível ainda...")
        time.sleep(2)
else:
    print("❌ Erro: MySQL não iniciou a tempo.")
    exit(1)

cursor = conn.cursor()

print("[3] Buscando o último ID...")
cursor.execute("SELECT MAX(id) FROM produtos;")
ultimo_id = cursor.fetchone()[0]

print(f"✓ Último ID = {ultimo_id}\n")

print("[4] Salvando resultado no arquivo...")

conteudo = f"Último ID encontrado: {ultimo_id}\n"

with open("resultado.txt", "w") as f:
    f.write(conteudo)

print("✓ Arquivo salvo como resultado.txt")
print("Processo finalizado.\n")

cursor.close()
conn.close()
