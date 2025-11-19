FROM mysql:8.0

# Apenas definindo nomes das variáveis (sem valores)
ENV MYSQL_ROOT_PASSWORD=
ENV MYSQL_DATABASE=
ENV MYSQL_USER=
ENV MYSQL_PASSWORD=

# Script de inicialização do banco
COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
