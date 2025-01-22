# Official Python 3.12.8 Alpine image
FROM python:3.12.8-alpine

# Set the working directory
WORKDIR /app

# Install git to clone the repository
RUN apk add --no-cache git

# Install dependencies
RUN pip install mercadopago discord.py

# Clone the repository
RUN git clone https://github.com/lazykoid/NicaPay.git

# Copy your bot files into the container
COPY . /app

# Command to run the script
CMD ["python3", "src/bot.py"]
