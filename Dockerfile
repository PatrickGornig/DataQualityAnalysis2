# Use an official python runtime as the base image
FROM python:3.9.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that Streamlit will run on
EXPOSE 8501

# Set the command to run when the container starts
CMD ["streamlit", "run", "app.py"]