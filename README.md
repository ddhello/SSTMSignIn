# SSTMSignIn
SS同盟论坛自动签到，使用selenium库进行自动操作 
SSTM自动签到 SSTM论坛自动签到
python3.7+

# 使用前配置
1.修改main.py中的“在这里输入邮箱”"在这里输入密码"两处分别为自己的SS同盟论坛邮箱和密码
```txt
username.send_keys("在这里输入邮箱")      #输入SS同盟论坛邮箱
```
```txt
password.send_keys("在这里输入密码")      #输入SS同盟论坛密码
```
2.下载适合自己的webdriver.点击chrome，设置，关于chrome，其中会显示chrome版本号（比较常见的是109）,将chromedriver文件放在文件根目录
  webdriver下载地址：https://chromedriver.chromium.org/downloads  
3.使用pip安装根目录下的requirements.txt  
  ```txt
  pip install -r requirements.txt
  ```
4.运行程序
```txt
python main.py
```


# 无界面Linux系统使用指南
鉴于为了自动签到，一般使用linux无界面系统挂机，因此写了该指南。
以Debian为例。  
1.安装Chrome  
更新apt
```txt
apt update
```
安装chrome
```txt
apt install --fix-broken google-chrome-stable
```
2.安装Xvfb  
由于selenium在无界面linux情况下会报错，因此需要安装虚拟桌面
```txt
sudo apt-get install xvfb
```
以下命令每次重启服务器都需要运行一次
```txt
Xvfb -ac :7 -screen 0 1280x1024x8 -extension RANDR -nolisten inet6 &
export DISPLAY=:7
```
3.运行程序
```txt
python3 main.py
```
