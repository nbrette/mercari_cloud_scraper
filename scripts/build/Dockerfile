FROM python:3.10-slim

RUN useradd -ms /bin/bash scraper
USER scraper

WORKDIR /scraper

COPY ./requirements.txt /scraper/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /scraper/requirements.txt

COPY . /scraper

EXPOSE 8080
CMD ["python3", "./src/main.py"]
