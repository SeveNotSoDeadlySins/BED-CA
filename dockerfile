# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Create virtual environment
RUN python -m venv /opt/venv
RUN pip install cryptography

# Activate it
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip first
RUN python -m ensurepip --upgrade
RUN pip install --upgrade pip setuptools wheel

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy wait script and make executable
COPY wait_for_mysql.sh /app/wait_for_mysql.sh


# Install netcat and make script executable
RUN apt-get update && apt-get install -y dos2unix netcat-openbsd \
    && dos2unix /app/wait_for_mysql.sh \
    && chmod +x /app/wait_for_mysql.sh


# Copy project code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Use wait script to ensure MySQL is ready
CMD ["sh", "-c", "/app/wait_for_mysql.sh mysql_db && python -m app.seeder.seed_users && uvicorn app.main:app --host 0.0.0.0 --port 8000"]
