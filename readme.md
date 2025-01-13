# flask-demo

## 1 介绍

提供一些常见接口，特别是在以下场景特别有用：

1. 在容器化部署时，有多副本，想看一下负载均衡情况是否符合预期
2. 多层反向代理时，先看下业务接收到的请求头比如XFF是否符合预期
3. apisix等作为反向代理，主动注入了一些header，想看下是否符合预期
4. 其他情况

## 2 部署

k8s 部署参考 k8s-deployment.yaml

## 3 测试

### 3.1 http测试

```bash
# 获取header
curl https://****.com/header
{
  "Accept": "*/*",
  "Accept-Encoding": "gzip",
  "Host": "***.com",
  "User-Agent": "curl/8.4.0",
  "X-Forwarded-For": "10.0.102.23",
  "X-Forwarded-Host": "***.com",
  "X-Forwarded-Port": "443",
  "X-Forwarded-Proto": "https",
  "X-Forwarded-Server": "cs-work-02",
  "X-Real-Ip": "10.0.102.23",
  "remote_addr": "10.42.119.192"
}

# 获取ip
curl https://****.com/ip
{
    "ip": "10.42.18.35"
}

# 获取hostname
curl https://****.com/hostname
{
    "hostname": "flask-demo-55b54c576d-55fkb"
}

# 其他测试
比如测试多副本运行的情况下，负载均衡情况
```

### 3.2 HTML测试

浏览器访问：<http://127.0.0.1:8888/index> ， 一个简单页面，可测试json提交和json返回

### 3.3 udp测试

```bash
# 使用python的udp客户端测试，脚本见test/udp-client.py，如下有2个pod在运行，可以看到两个pod都在返回
～ python3 test/udp-client.py
send   : 0
recvice: my ip is 10.42.215.235
send   : 1
recvice: my ip is 10.42.215.235
send   : 2
recvice: my ip is 10.42.215.235
send   : 3
recvice: my ip is 10.42.8.166
send   : 4
recvice: my ip is 10.42.8.166
send   : 5
recvice: my ip is 10.42.215.235
send   : 6
recvice: my ip is 10.42.8.166
```
