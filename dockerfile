# Use the official Python 3.12.8 Alpine image
FROM python:3.12.8-alpine

# Set the working directory
WORKDIR /app

# Install git to clone the repository
RUN apk add --no-cache git

# Clone the repository
RUN git clone https://github.com/lazykoid/Niczx.git .

# Create a requirements.txt file with the necessary packages
RUN echo "discord.py\nmercadopago" > requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the run.sh script is executable
RUN chmod +x run.sh

# Command to run the script
CMD ["./run.sh"]
