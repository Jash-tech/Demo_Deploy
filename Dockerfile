# 1. Use an official Python image from Docker Hub
FROM python:3.9-slim

# 2. Set the working directory to /app
WORKDIR /app

# 3. Copy the current directory contents into the container at /app
COPY . /app

# 4. Install any dependencies inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose port 8000 for the FastAPI app
EXPOSE 8000

# 6. Command to run the FastAPI app using Uvicorn inside the container
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
