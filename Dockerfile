# 1. Base Image
# Use a specific slim version of Python for a smaller image size
FROM python:3.11-slim

# 2. Environment Variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing .pyc files to disk (keeps image clean)
# PYTHONUNBUFFERED: Ensures logs print immediately to the console (essential for debugging)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Working Directory
WORKDIR /app

# 4. Install Dependencies (Cached Layer)
# We only copy requirements.txt first. If your code changes but requirements stay 
# the same, Docker will use the cache instead of reinstalling everything.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 5. Copy Application Code
# Copy only the necessary files to keep the container clean
COPY app.py agent.py tools.py ./

# 6. Expose Port
# Tell Docker that the container listens on port 8501 (Streamlit's default)
EXPOSE 8501

# 7. Healthcheck (Optional but impressive)
# Tells Docker how to check if the app is actually running healthily
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# 8. Run Command
# We bind to 0.0.0.0 so the container accepts external traffic
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]