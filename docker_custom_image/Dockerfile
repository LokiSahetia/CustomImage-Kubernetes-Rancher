# Step 1: Use Python Base Image
FROM python:3.11-slim

# Step 2: Set Working Directory
WORKDIR /app

# Step 3: Copy Files
COPY . .

# Step 4: Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose Port
EXPOSE 5000

# Step 6: Start Application
CMD ["python", "app.py"]
