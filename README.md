# Remix Tiny Port Mapper

一个用于端口转发的软件，基于TinyPortMapper.exe，并弥补其不能进行DNS解析的不足。

## 使用方法

1. 下载Release文件后解压，修改`conf/settings.json`文件：

```json
{
    // 主机启动，只需修改server即可
  "server": {
    "address": "此处填写用作主机的地址", // 主机地址（公网）
    "port": 1234, // 主机原端口号
    "isIPv6": true, // 是否是ipv6地址 true/false
    "needDNS": true // 是否需要DNS解析 true/false
  },
    // 客户机启动，需同时修改server和client
  "client": {
    "address": "localhost", // 客户机地址，一般填写localhost即可
    "port": 8888, // 客户机端口号
    "isIPv6": false, // 是否是ipv6地址 true/false
    "needDNS": true// 是否需要DNS解析 true/false
  }
}
```

2. 主机：运行`bin/Server.exe`文件
3. 客户机：运行`bin/Client.exe`文件

## 补充说明

- 程序运行后，`conf`文件夹下自动生成`DNS_setting.json`文件，即域名解析后配置文件。
- `TinyPortMapper.exe`文件在`resources/tinymapper`文件夹下，支持命令行启动，更多高级用法请参看原作。[tinyPortMapper](https://github.com/wangyu-/tinyPortMapper)

