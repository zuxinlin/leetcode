# jupyter

## 安装

```shell
# 安装依赖
pip install jupyter jupyter_contrib_nbextensions
jupyter contrib nbextension install

# 生成密码
from notebook.auth import passwd
passwd()

# 在用户目录生成配置文件
jupyter notebook --generate-config

# 修改配置文件
c.NotebookApp.ip='*'
c.NotebookApp.password = ''

# 启动
jupyter notebook --allow-root
```

## 快捷键

### 命令模式 (按键 Esc 开启)

* Enter : 转入编辑模式
* Shift-Enter : 运行本单元，选中下个单元
* Ctrl-Enter : 运行本单元
* Alt-Enter : 运行本单元，在其下插入新单元
* Y : 单元转入代码状态
* M :单元转入markdown状态
* K : 选中上方单元
* J : 选中下方单元
* A : 在上方插入新单元
* B : 在下方插入新单元
* X : 剪切选中的单元
* C : 复制选中的单元
* V : 粘贴到下方单元
* Z : 恢复删除的最后一个单元
* D,D : 删除选中的单元
 
