# Pull official base image
FROM python:3.8.10

# Set work directory
WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

#
COPY . .

# Подумать нужен ли --reload, если контейнер и так перезагружается:
CMD ["python", "create_db.py"]
#CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
#CMD ["uvicorn", "main:app"]
# CMD ["python", "test.py"]

# Copy project
#COPY . .

#FROM python:3.8.10

#WORKDIR /usr/src/app

#RUN python -m pip install requests
#COPY headlines.py .
#CMD ["python", "test.py"]