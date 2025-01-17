FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    curl \
    nano \
    cron
RUN rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy application files
COPY checker.py /app/
COPY requirements.txt /app/

# Install dependencies using pip as root (default user)
RUN pip install -r /app/requirements.txt

# Copy crontab and set permissions
COPY crontab /etc/cron.d/crontab
RUN chmod 644 /etc/cron.d/crontab

# Run cron in the foreground
ENTRYPOINT ["cron", "-f"]
