FROM --platform=linux/amd64 python:3.13.0

WORKDIR /app
ADD . .
RUN pip install --upgrade pip \
	&& pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
#	&& pip install -r requirements.txt -i https://pip.nie.netease.com/simple

CMD ["python3", "run.py"]
# CMD ["sleep", "360000000"]

# docker build --platform=linux/amd64 -t ncr.nie.netease.com/ccbaseimage/flask-demo-mengzi:v0.6 .
# docker build --platform=linux/amd64 -t flask-demo:v0.1 .