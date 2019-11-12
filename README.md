# Entity Aligned






## 使用JuputerHub

### 部署


```shell

touch .env
make env ENVFLAG=dev DATADIR=/path/to/your/team/data
make run
```

### 使用
open http://127.0.0.1:8889
在界面中输入id, 密码随意即可
!tip:
	因为文件属系统原因, 很有可能无法新建notebook或者进行git操作
	需要修改文件属用户为 jovyan
	
	```shell
	sudo chown jovyan *.
	sudo chown jovyan *
	```

### 注意事项
- 每位用户都会获得一个单独的容器作为运行环境
- 数据是共享的
- 容器中的代码是编译期加入的, 不一定是最新的
- 使用jupyter中的terminal而不是系统terminal
- 需要工程化的依赖应该在容器编译期固定
- python包pyhanlp的数据未下载, 需要自行下载, 或者去/data/目录里找找
- 建议把自己的代码用github一类的远端库管理起来
- 数据应该放到/data/里面
