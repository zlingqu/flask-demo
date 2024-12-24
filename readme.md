
提供一些常见接口，特别是在以下场景特别有用：
- 1. 在容器化部署时，有多副本，想看一下负载均衡情况是否符合预期
- 2. 多层反向代理时，先看下业务接收到的请求头比如XFF是否符合预期
- 3. apisix等作为反向代理，主动注入了一些header，想看下是否符合预期
- 4. 其他情况
```bash
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

curl https://****.com/ip
{
    "ip": "10.42.18.35"
}
➜  ~
➜  ~ curl https://****.com/hostname
{
    "hostname": "flask-demo-55b54c576d-55fkb"
}

```