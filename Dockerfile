FROM python:3.10

# Set working directory
WORKDIR /app

# Copy app files
COPY app.py .
COPY requirements.txt .
COPY .streamlit/ .streamlit/   # ✅ Copy the config explicitly

# Set environment variable so Streamlit uses this config
ENV STREAMLIT_CONFIG_DIR=/app/.streamlit

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Expose port
EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
