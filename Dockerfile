FROM --platform=linux/amd64 python:3.6.13-buster

WORKDIR /app
ADD . .
RUN pip install --upgrade pip \
	&& pip install -r requirements.txt -i https://pip.nie.netease.com/simple

CMD ["python3", "run.py"]