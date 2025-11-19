FROM python:3.11-slim

RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

COPY requirements.txt .

# Instalando dependências
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Healthcheck para o Docker verificar se a app está viva
HEALTHCHECK --interval=30s --timeout=3s --retries=3 \
  CMD curl --silent --fail http://localhost:5000/files || exit 1

USER appuser

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
