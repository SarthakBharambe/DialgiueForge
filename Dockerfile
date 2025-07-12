FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY .streamlit/ .streamlit/   # ✅ Add this line to copy config

RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false", "--server.headless=true"]
