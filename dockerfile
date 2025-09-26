# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Create a virtual environment inside the container
RUN python -m venv /opt/venv

# Activate it for all future RUN/CMD instructions
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Run app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
