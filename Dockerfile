FROM python:3.10

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
COPY app.py .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

# Expose the Streamlit default port
EXPOSE 7860

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.enableCORS=false"]
