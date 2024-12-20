# Dockerfile

FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]
