FROM python:3.9

WORKDIR /app

# Copy the controller script and dependencies
COPY widget-controller.py /app/widget-controller.py
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Start the controller automatically
CMD ["python", "/app/widget-controller.py"]

