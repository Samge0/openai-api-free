## 字体反爬破解的api-docker镜像
一个字体反爬破解的api-docker镜像

### 构建api正式包
```shell
docker build . -t samge/openai-api-free -f docker/Dockerfile
```

### 上传
```shell
docker push samge/openai-api-free
```

### 运行docker镜像
这里的`/home/samge/docker_data/openai-api-free/config.json`需要替换为使用者的本地映射路径。
```shell
docker run -d \
--name openai-api-free \
-v /home/samge/docker_data/openai-api-free/config.json:/app/config.json \
-v /home/samge/docker_data/openai-api-free/logs:/app/logs \
-p 8232:8000 \
--pull=always \
--restart always \
--memory=1.5G \
samge/openai-api-free:latest
```
