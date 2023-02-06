# SSTMSignIn
SS同盟论坛自动签到，使用selenium库进行自动操作  
python3.10.4

# 使用前配置
1.修改main.py中的“在这里输入邮箱”"在这里输入密码"两处分别为自己的SS同盟论坛邮箱和密码  
2.下载适合自己的webdriver.点击chrome，设置，关于chrome，其中会显示chrome版本号（比较常见的是109）,将chromedriver文件放在文件根目录（如果不是Windows，需要自行更改    driver = webdriver.Chrome(executable_path= "chromedriver.exe",options= option)）  
  webdriver下载地址：https://chromedriver.chromium.org/downloads  
3.使用pip安装根目录下的requirements.txt  
4.`python main.py`
