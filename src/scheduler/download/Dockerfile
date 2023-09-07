FROM ml-base:latest

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir output

WORKDIR .
COPY . .

ENV aws_access_key_id="kLm4VFPo52x58AHL8Qao6D"
ENV aws_secret_access_key="f594SW6t8zc6Ysx7pjmofaFUcNPni2dmb4Zhm6waCmHS"

ENTRYPOINT ["python", "download.py"]