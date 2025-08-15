FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "app.py"]
