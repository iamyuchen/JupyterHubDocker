#Entity Aligned






##使用JuputerHub

###部署
```shell
touch .env
make env ENVFLAG=dev DATADIR=/path/to/your/team/data
make run
```

###使用
open http://127.0.0.1:8889
在界面中输入id, 密码随意即可
!tip:
	因为文件属系统原因, 很有可能无法新建notebook或者进行git操作
	需要修改文件属用户为 jovyan
	```shell
	sudo chown jovyan *.
	sudo chown jovyan *
	```

###注意事项
- 每位用户都会获得一个单独的容器作为运行环境
- 数据是共享的
- 容器中的代码是编译期加入的, 不一定是最新的
- 使用jupyter中的terminal而不是系统terminal
- 新的依赖可以直接在容器中添加, 如: 使用jupyter terminal添加
- 需要工程化的依赖应该在容器编译期固定
- 当前python依赖文件requirements.txt比较混乱, 需要进一步规范
