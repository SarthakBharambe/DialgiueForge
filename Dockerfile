FROM python:3.10

WORKDIR /app

# Copy files into container
COPY requirements.txt .
COPY app.py .
COPY .streamlit/ .streamlit/

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Avoid permission error by setting working config directory
ENV STREAMLIT_HOME=/app
ENV STREAMLIT_CONFIG_FILE="/app/.streamlit/config.toml"

EXPOSE 7860

CMD ["streamlit", "run", "app.py", "--server.port=7860"]

