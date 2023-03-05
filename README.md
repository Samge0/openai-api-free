## 使用openai账号轮询chatgpt的web端接口
- 参考[https://github.com/acheong08/ChatGPT](https://github.com/acheong08/ChatGPT)
- 代理服务器速率限制：每 10 秒 15 个请求（每个 IP）
- OpenAI 速率限制：免费帐户每小时 50 个请求。你可以通过多账户循环来绕过它
- Plus 帐户每小时有大约 150 个请求的速率限制


### 使用说明
- 复制`config-dev.json`文件为`config.json`并填写自定义的`auth_token`、`account_infos`；
  - auth_token：访问接口的自定义token
  - account_infos：openai的账号信息列表，格式为："登录邮箱|登录密码|代理ip"
    - 例如："samgeapp@gmail.com|xxxpw|http://127.0.0.1:7890"
    - 例如："samgeapp@gmail.com|xxxpw"
- 配置`http-client.env.json`后在`test_main.http`中进行接口调试，其中`auth_token`的值跟config.json中的一致；
- 接口使用请查看`test_main.http`测试文件

### docker方式运行
[点击这里查看docker说明](docker/README.md)


### 本地源码运行

- 安装依赖
```shell
pip install -r requirements.txt
```

- 运行
```shell
uvicorn run main:app --reload --host 0.0.0.0 --port 8000
```

### 有疑问请添加微信（备注: openai-api-free），不定期通过解答
**微信号 SamgeApp **


### 免责声明
该程序仅供技术交流，使用者所有行为与本项目作者无关