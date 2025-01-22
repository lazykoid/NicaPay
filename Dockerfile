# Use the official Python 3.12.8 Alpine image
FROM python:3.12.8-alpine

# Set the working directory
WORKDIR /app

# Copy your bot files into the container
COPY . /app

# Install dependencies
RUN pip install mercadopago discord.py

# Command to run the script
CMD ["python3", "src/bot.py"]
