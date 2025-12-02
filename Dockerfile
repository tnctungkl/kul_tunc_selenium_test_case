# Use official Python image as base.
FROM python:3.14

# Set workdirectory.
WORKDIR /app

# System deps for Chrome and ChromeDriver installation.
RUN apt-get update && \
    apt-get install -y wget gnupg unzip curl && \
    apt-get install -y chromium chromium-driver && \
    rm -rf /var/lib/apt/lists/*

# Set environment variables for Chrome and headless mode.
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver
ENV HEADLESS=true
ENV BROWSER=chrome

# Copy project files.
COPY . /app

# Install Python deps from requirements.txt.
RUN pip install --no-cache-dir -r requirements.txt

# Run tests with pytest by default.
CMD ["pytest"]
