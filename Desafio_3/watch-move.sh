#!/bin/bash

WATCH_DIR="/home/yara/NG-Billing/Desafio_3/monitorar"
DEST_DIR="/home/yara/NG-Billing/Desafio_3/destino"

# Garante que os diretórios existem
mkdir -p "$WATCH_DIR"
mkdir -p "$DEST_DIR"

echo "Monitorando o diretório: $WATCH_DIR"

# Monitora criação de arquivos
inotifywait -m -e create "$WATCH_DIR" |
while read path action file; do
    echo "Novo arquivo detectado: $file"
    mv "$WATCH_DIR/$file" "$DEST_DIR/"
    echo "Arquivo movido para: $DEST_DIR/$file"
done
