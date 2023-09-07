FROM ml-base:latest

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir output

WORKDIR .
COPY . .

COPY preprocess.py /preprocess.py

ENTRYPOINT ["python", "preprocess.py"]