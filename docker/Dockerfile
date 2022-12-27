FROM python:3.10.9-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

RUN useradd --user-group --shell /bin/false otus  
USER otus

EXPOSE 8000

CMD ["uvicorn", "service.main:app", "--host=0.0.0.0", "--port=8000"]
