FROM python:3.6
COPY . /app
WORKDIR /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
RUN pip install -r requirements.txt