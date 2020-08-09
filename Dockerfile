# Use an official Python runtime as a parent image
FROM python:3.6

COPY requirements/prod.txt requirements.txt
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

WORKDIR ./src
ADD src ./
COPY .myenv.example .myenv

EXPOSE 8080
