# 从零开始的搭建~~视奸~~网站全流程保姆教程
- 成果展示，站点[点击预览](https://smallsinger629.site/)
![预览1](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%A2%84%E8%A7%881.png?raw=true "预览1")
> [!IMPORTANT]
> 
> 本仓库基于是[@wyf9](https://github.com/wyf9)的[sleepy](https://github.com/wyf9/sleepy)项目的commit[6a277a0](https://github.com/wyf9/sleepy/commit/6a277a0c5b751bdc4ded2efc1c4c92d6995bb569)的保存快照，附加了搭建教程，更新的功能和修复请去查看[@wyf9](https://github.com/wyf9)的[sleepy](https://github.com/wyf9/sleepy)项目

**目录**
> 
> 一、[**搭建服务器**](#一搭建服务器以微软azure云服务器为例)
> 
> 二、[购买域名并解析服务器IP（可选）](#二可选购买域名并解析服务器ip)
> 
> 三、[搭建网站后端（可选）](#三可选搭建网站后端)
> 
> 四、[**部署项目**](#四部署sleepy项目)

> [!TIP]
> 如有疑问，可以在[讨论区](https://github.com/univers629/sleepy/issues)查看他人遇到的问题，或[点击](https://github.com/univers629/sleepy/issues/new?template=Blank+issue)提出新的问题。


***

## 一、搭建服务器（以微软Azure云服务器为例）
[**白嫖**](#一开通azure账号) / [**创建**](#二创建b1s虚拟机) / [**设置**](#三开机设置)
> [!TIP]
> 
> 使用Azure免费服务器需要学生邮箱（*.edu*）或外币信用卡

### （一）开通Azure账号

#### 1、[**学生注册链接**](https://azure.microsoft.com/zh-cn/free/students/)（需要学生邮箱验证资格，无需信用卡）
- [x] 12个月免费服务使用资格，学生邮箱资格有效期内可以免费续订
- [x] 12个月有效期的100美金额度

#### 2、[**普通注册链接**](https://azure.microsoft.com/zh-cn/free/)（需要绑定Visa或万事达等外币信用卡，卡里需要有1美元用于验证）
- [x] 仅适用于新的 Azure 客户
- [x] 12 个月内每月免费使用超过 20 项热门服务（仅限新 Azure 客户）
- [x] 每月免费提供超过 65 项始终免费服务
- [x] 访问免费金额和 200 美元额度范围内服务的完整目录
- [x] 支出保护 - 不会向信用卡收费*
- [x] 无前期承诺 - 可随时取消
- [x] 转到即用即付定价，可在超过 30 天或信用额度用尽后继续使用
> 普通注册申请免费试用的30天内，需要把订阅升级到即用即付，才能继续免费用一年。但是在升级过程中，有一个Dev Support Plan是默认勾选的，需要去掉，否则会直接从卡中扣费
> 普通注册的200美金额度只有1个月有效期

> [**余额、资费查询**](https://www.microsoftazuresponsorships.com/Balance)(可查看账单或知晓是否因错误设置而造成收费)

### （二）创建B1s虚拟机

> Azure提供的免费机型为B1s，可分别开一台windows和一台Linux。
> 两台虚拟机服务器每月各自有750小时的免费使用时长，每月共用15GB流量。

#### 1、开通Azure账户后，自动跳转到[Azure门户首页](https://portal.azure.com/#home)，点击创建资源，跳转后创建虚拟机。
![创建1](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%901.png?raw=true "创建资源1") ![创建2](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%902.png?raw=true "创建资源2")
#### 2、创建流程
(1).基本

![创建3](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%903.png?raw=true "创建资源3")

> [!TIP]
> 
> 资源组：可以新建一个用户名为资源组
> 
> 虚拟机名称：随意
> 
> 区域：建议韩国中部，地理距离近且后续配置动态IP时不用删除再新建网络组
> 
> 映像：可选择“查看所有映像”，然后搜索想要的映像，这里我选择Debian12
> 
> VM体系结构：x64
> 
> 使用Azure现成虚拟机折扣运行：保持默认不勾选

> [!IMPORTANT]
> 
> 可用性选项：选择无需基础结构冗余（否则无法配置动态IP）
> 
> 安全类型：如果选择的系统映像结尾为Gen2则可选择“受信任启动虚拟机”，为Gen1则只能选择“标准”

![创建4](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%904.png?raw=true "创建资源4")

> [!TIP]
> 
> 启用休眠：保持默认不勾选
> 
> 身份验证类型：SSH公钥
> 
> 用户名：保持默认即可
> 
> SHH公钥源：保持默认生成新密钥对
> 
> SHH密钥类型：选择更短的Ed25519格式
> 
> 密钥对名称：保持默认或自己设置（之后下载的密钥文件就是这个名称）
> 
> 入站端口规则：保持默认

> [!IMPORTANT]
> 
> 大小：必须选择“B1s(有资格免费试用服务)”，否则会收费！！！可以进入“查看所有大小里搜索选择”

(2).磁盘

![创建5](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%905.png?raw=true "创建资源5")

> [!TIP]
> 
> 全部保持默认，只需要设置磁盘大小

> [!IMPORTANT]
> 
> OS磁盘大小：必须选择“64GiB(P6，符合免费层条件)”，只有这个选项是免费的

(3).网络

![创建6](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%906.png?raw=true "创建资源6")

> [!TIP]
> 
> 全部保持默认，只需要设置公共IP

> [!IMPORTANT]
> 
> 点击新建公共IP，并按如图设置为动态IP并确定，静态IP会收取费用！！！

(4).管理、监视、高级、标记、查看+创建

![创建7](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%907.png?raw=true "创建资源7")

> [!TIP]
> 
> 全部保持默认，点击下一步，直到显示验证已通过，点击下方创建即可获得一台搭载Debian12的虚拟机云服务器
> 
> 创建时会弹出下载SSH密钥的弹窗，点击下载即可
> 
> 等待几分钟，虚拟机服务器就创建完毕了

### （三）开机设置

#### 1、获取服务器公网IP

- 点击网页左上角的`Microsoft Azure`字样回到首页，点击`Debian12`进入虚拟机概述页，将鼠标移至右侧的`公共IP地址`，点击右侧出现的复制图标复制IP地址
![创建8](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%908.png?raw=true "创建资源8")
![创建9](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%88%9B%E5%BB%BA%E8%B5%84%E6%BA%909.png?raw=true "创建资源9")


#### 2、使用SSH终端连接服务器（以WindTerm为例）
[**点击下载Windows最新版**](https://github.com/kingToolbox/WindTerm/releases/download/2.6.0/WindTerm_2.6.1_Windows_Portable_x86_64.zip)

- 下载完成后解压，将文件夹放置到自己想要放置的目录
- 点击进入文件夹，双击`WindTerm.exe`
- 在弹出的窗口中选择`使用应用程序目录`，然后点击`OK`自动打开终端
![SSH1](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH1.png?raw=true "SSH1")
- 关闭下方窗口，然后点击上方`工具`选项卡，点击弹出菜单中的`Onekeys`,点击右下角黄色字体解除锁定，然后点击黄色字体上方的`+`创建新的key，命名后填入创建虚拟机时设置的用户名（默认为`azureuser`），双击下方的`Linux`，在弹出的窗口中选择刚才下载的`Debian12_key.pem`，点击OK，然后点击右下方`确定`完成创建Key
![SSH2](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH2.png?raw=true "SSH2")
![SSH3](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH3.png?raw=true "SSH3")
![SSH4](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH4.png?raw=true "SSH4")

- 选择左上角`会话`选项卡，点击`新建会话`，主机填入`azureusr@你刚刚复制的虚拟机公网IP`，OneKey下拉选择刚才创建的`Debian12`,然后点击连接。
![SSH5](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH5.png?raw=true "SSH5")

- 在弹出的窗口中选择`是（Y）`,再选择一次`Debian12_key.pem`，然后点击连接，出现下图中的字样`azureuser@Debian12:~$`即代表连接成功
![SSH6](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH6.png?raw=true "SSH6")
![SSH7](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH7.png?raw=true "SSH7")
![SSH8](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH8.png?raw=true "SSH8")


> [!TIP]
> 
> Windterm的30分钟自动锁定屏幕功能可能导致密码错误软件需要重新打开
> 
> 可以进入软件目录的`/global`下，右键用记事本打开`wind.config`文件
> 
> 查找并修改`"application.lockScreenTimeout": 30`将`30`改为`0`并保存即可关闭自动锁定屏幕

#### 3、（可选）配置Debian系统的中文环境

![SSH9](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH9.png?raw=true "SSH9")


(输入命令回车即可运行)
- 更新软件包
  ```shell
  sudo apt update && sudo apt upgrade -y
  ```

- 安装`locales`软件包
  ```shell
  sudo apt install locales -y
  ```

- 执行下列命令配置语言环境：
  ```shell
  sudo dpkg-reconfigure locales
  ```
![SSH10](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH10.png?raw=true "SSH10")
语言项非常多，通过`鼠标滚轮`或`上下方向键`逐个移动光标，翻到最下面可以找到中文语言环境,**按下`空格`即可选择，前面带星号(*)即被选中**，选择如图的`zh_CN.UTF-8 UTF-8`即可，最后按下回车确定。
![SSH11](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH11.png?raw=true "SSH11")
在新页面中通过`鼠标滚轮`或`上下方向键`逐个移动光标，选择`zh_CN.UTF-8`，按下回车确定，完成中文环境设置（如下图所示）
![SSH12](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH12.png?raw=true "SSH12")

> [!TIP]
> 
> 检测方法：我们可以关闭WindTerm并重新打开，并输入`sudo apt update`运行，就可以看到输出了中文提示
> 
> ![SSH13](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/SSH13.png?raw=true "SSH13")

- 将系统时区调整为北京时间
  运行
  ```shell
  sudo timedatectl set-timezone Asia/Shanghai
  ```
  即可更改，可以用`timedatectl`命令检测更改是否成功：
  ```shell
  azureuser@Debian12:~$ sudo timedatectl set-timezone Asia/Shanghai
  azureuser@Debian12:~$ timedatectl
                Local time: 五 2025-01-24 19:49:27 CST
            Universal time: 五 2025-01-24 11:49:27 UTC
                  RTC time: 五 2025-01-24 11:49:27
                  Time zone: Asia/Shanghai (CST, +0800)
  System clock synchronized: yes
                NTP service: active
            RTC in local TZ: no
  azureuser@Debian12:~$ 
  ```
  出现`Time zone: Asia/Shanghai (CST, +0800)`代表配置成功

***

## 二、（可选）购买域名并解析服务器IP

> [!IMPORTANT]
> 
> 不绑定域名的话只能通过IP地址访问网站，且在大多数浏览器上会提示不安全，需要选择`继续访问`之类的选项。

### （一）购买域名
[百度智能云·域名服务](https://cloud.baidu.com/product/bcd.html)
![域名1](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D1.png?raw=true "域名1")

- 输入你想要的域名并查询
![域名2](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D2.png?raw=true "域名2")

- 按照流程购买并实名，上传身份证，填写信息，等待审核通过（一天之内就能通过）

- 获得域名后，进入[域名管理页](https://console.bce.baidu.com/bcd/#/bcd/manage/list)，点击右侧的`解析`
![域名3](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D3.png?raw=true "域名3")

### （二）添加解析示例

#### 1、添加CNAME记录解析（推荐）
- 回到服务器概览页，点击右侧`DNS名称：未配置`，进入页面后随便填写一个允许的名称保存即可
![域名4](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D4.png?raw=true "域名4")
![域名5](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D5.png?raw=true "域名5")

- 保存完毕后，点击左上角`Debian12`回到概览页，刷新网页，复制右侧出现的`DNS名称`
![域名6](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D6.png?raw=true "域名6")

- 在域名解析页`添加解析`，主机记录填写`@`，选择`CNAME记录`，并在`记录值`处填写之前复制的`DNS名称`，点击`确定`，等待几分钟即可将域名解析到服务器，并通过域名访问服务器
![域名7](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D7.png?raw=true "域名7")

#### 2、添加A记录解析
在域名解析页`添加解析`，主机记录填写`www`，选择`A记录`，并在`记录值`处填写之前复制的`公共IP地址`，点击`确定`，等待几分钟即可将域名解析到服务器，并通过域名访问服务器
![域名8](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D8.png?raw=true "域名8")

#### 3、更改SSH终端登录地址为域名地址

- 打开SSH终端应用，单击右键点击右侧添加的会话`azureuser@你的公共IP地址`，点击删除
![域名9](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D9.png?raw=true "域名9")

- 像之前一样点击左上角`会话`→`新建会话`，将主机值改为`azureuser@你的域名地址`，即可实现之后用域名连接服务器。
![域名10](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%9F%9F%E5%90%8D10.png?raw=true "域名10")

> [!TIP]
> 
> 主机记录即域名前缀，常用如下：
> 
> 1.www：解析后域名为www.baidubceyun.cn
> 
> 2.@：直接解析主域名baidubceyun.cn
> 
> 3.*：泛解析，匹配其他所有域名baidubceyun.cn


> CNAME解析可以记录服务器的动态IP，不需要服务器每次重启时都来域名解析这里修改IP地址
> 
> 通过`http`或`https`协议访问服务器需要在服务器上打开`80`和`443`端口，详细教程见下方

***

## 三、（可选）搭建网站后端
### （一）开启防火墙端口
- 在服务器概览页点击左侧的`网络设置`
![后端1](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF1.png?raw=true "后端1")
- 在右侧选择`创建端口规则`→`入站端口规则`
![后端2](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF2.png?raw=true "后端2")
- 放行80端口：在服务里选择`HTTP`，点击`添加`
![后端3](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF3.png?raw=true "后端3")
- 放行443端口：以同样的方式添加`HTTPS`
![后端4](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF4.png?raw=true "后端4")
- （自定义）放行9010端口用于测试：在`目标端口范围`处填写`9010`
![后端5](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF5.png?raw=true "后端5")
- 最终开放的端口：
![后端6](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF6.png?raw=true "后端6")
> [!TIP]
> 
> 可以自定义开放端口，`80`端口和`443`端口是`http`或`https`所协议必须的，`9010`端口是`sleepy`项目默认使用的端口，可选择是否开启

### (二)Nginx后端搭建
- 安装nginx
  ```shell
  sudo apt install nginx -y
  ```
- 启动nginx
  ```shell
  sudo systemctl start nginx
  ```
- 设置nginx为开机自启
  ```shell
  sudo systemctl enable nginx
  ```
- 示例
![后端7](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF7.png?raw=true "后端7")
> [!TIP]
> 
> 测试：现在，在浏览器的新标签页地址栏输入你的服务器的`公共IP地址`，即可看到nginx的欢迎页！！！
> 
> ![后端8](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF8.png?raw=true "后端8")

### (三)配置网站安全证书（使用`certbot`项目）

#### 1、安装证书
- 安装certbot和nginx插件
  ```shell
  sudo apt install certbot python3-certbot-nginx -y
  ```
- 使用certbot自动获取网站网站安全证书并配置nginx
  ```shell
  sudo certbot --nginx -d 你的域名地址
  ```
> [!TIP]
> 
> 如果有多个域名，可以继续添加`-d`参数来添加。
> 
> 这里的域名需要都在[域名管理页](https://console.bce.baidu.com/bcd/#/bcd/manage/list)里配置了解析，否则获取证书会失败，需要重新运行命令获取。

- 以下是运行的示例和注释：
  ```shell
  azureuser@Debian12:~$ sudo certbot --nginx -d 你的域名地址
  Saving debug log to /var/log/letsencrypt/letsencrypt.log # 日志存放路径
  Enter email address (used for urgent renewal and security notices)
    (Enter 'c' to cancel): 填写你的邮箱地址或输入“C”取消程序

  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Please read the Terms of Service at
  https://letsencrypt.org/documents/LE-SA-v1.4-April-3-2024.pdf. You must agree in
  order to register with the ACME server. Do you agree?
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  (Y)es/(N)o: y # 这里输入y，表示同意他们的服务政策

  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  Would you be willing, once your first certificate is successfully issued, to
  share your email address with the Electronic Frontier Foundation, a founding
  partner of the Let's Encrypt project and the non-profit organization that
  develops Certbot? We'd like to send you email about our work encrypting the web,
  EFF news, campaigns, and ways to support digital freedom.
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  (Y)es/(N)o: y # 这里输入有y或n，这个选项是询问您是否愿意在成功申请到第一个证书后，将您的电子邮箱地址共享给 Electronic Frontier Foundation (EFF)。EFF 是 Let's Encrypt 项目的创始合作伙伴之一，也是 Certbot 的开发组织。他们希望向您发送有关加密网络、EFF 新闻、活动以及支持数字自由的相关邮件。如果您不想接收这些邮件，可以选择填写 n，拒绝共享您的邮箱地址。这不会影响您的证书申请或续签过程。
  Account registered.
  Requesting a certificate for 这里是你的域名地址

  Successfully received certificate.
  Certificate is saved at: /etc/letsencrypt/live/这里是你的域名地址/fullchain.pem # 证书链存放路径
  Key is saved at:         /etc/letsencrypt/live/这里是你的域名地址/privkey.pem # 密钥
  This certificate expires on 2025-04-24. # 证书的过期时间
  These files will be updated when the certificate renews.
  Certbot has set up a scheduled task to automatically renew this certificate in the background. #设置了自动续签的任务

  Deploying certificate
  Successfully deployed certificate for 这里是你的域名 to /etc/nginx/sites-enabled/default
  Congratulations! You have successfully enabled HTTPS on 这里是你的域名1的HTTPS协议的网址 and 这里是你的域名2的HTTPS协议的网址 # 表示成功签发了证书，可以用HTTPS协议访问域名

  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  If you like Certbot, please consider supporting our work by: # 下面是为Certbot项目提供支持和赞助的方式
  * Donating to ISRG / Let's Encrypt:   https://letsencrypt.org/donate
  * Donating to EFF:                    https://eff.org/donate-le
  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  azureuser@Debian12:~$ 
  ```
> [!TIP]
> 
> 证书安装完成后，在浏览器新建标签页，再地址栏中输入你的域名
> 
> 你就可以看到网站已经可以安全访问，显示`连接安全`，并且`此网站具有由受信任的机构颁发的有效证书`
> 
> ![后端9](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF9.png?raw=true "后端9")
> 
> ![后端10](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E5%90%8E%E7%AB%AF10.png?raw=true "后端10")

#### 2、站点配置

- 禁用默认配置文件
  ```shell
  sudo rm -f /etc/nginx/sites-enabled/default
  ```
- 新建配置文件
  ```shell
  sudo nano /etc/nginx/sites-available/sleepy.conf
  ```
  复制下面内容后右键粘贴到终端中并使用`方向键`和`鼠标滚轮`修改为自己的域名，修改完成后按`Ctrl+X`后按`Y`确认修改，最后按`回车键`退出
  ```nginx
  # Default server configuration
  server {
          listen 80 default_server;
          listen [::]:80 default_server;

          root /var/www/html;

          index index.html index.htm index.nginx-debian.html;

          server_name _;

          location / {
              try_files $uri $uri/ =404;
          }
  }

  # SSL configuration for 你的域名地址
  server {
          listen [::]:443 ssl ipv6only=on; # managed by Certbot
          listen 443 ssl; # managed by Certbot

          ssl_certificate /etc/letsencrypt/live/你的域名地址/fullchain.pem; # managed by Certbot
          ssl_certificate_key /etc/letsencrypt/live/你的域名地址/privkey.pem; # managed by Certbot

          include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
          ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

          server_name 你的域名地址; # 仅处理你的域名地址

          location / {
              proxy_pass http://127.0.0.1:9010;  # 将请求转发到本地的 127.0.0.1:9010
              proxy_set_header Host $host;       # 传递原始请求的 Host 头
              proxy_set_header X-Real-IP $remote_addr;  # 传递客户端的真实 IP
              proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;  # 传递转发信息
              proxy_set_header X-Forwarded-Proto $scheme;  # 传递原始请求的协议（HTTP/HTTPS）
          }
  }

  # HTTP to HTTPS redirection
  server {
      listen 80;
      listen [::]:80;

      server_name 你的域名地址

      return 301 https://$host$request_uri; # 重定向到 HTTPS
  }
  ```
- 启用新的配置文件
  ```shell
  sudo ln -s /etc/nginx/sites-available/sleepy.conf /etc/nginx/sites-enabled/
  ```




***

## 四、部署sleepy项目

### （一）克隆并启动sleepy项目
- 安装`python3`、`pip`、`git`软件包
  ```shell
  sudo apt install python3 python3-pip git -y
  ```
- 克隆`sleepy`项目储存库
  ```shell
  git clone --depth 1 https://github.com/univers629/sleepy.git
  ```
- 切换到`sleepy`目录
  ```shell
  cd sleepy
  ```
- 安装依赖

  ```shell
  pip install flask pytz --break-system-packages
  ```

- 先启动一遍程序:
  ```shell
  python3 server.py
  ```

- 如果不出意外，会提示类似于下方内容，同时目录下出现`config.json` 文件
  ```python
  [Warning] [2025-01-25 21:39:00] config.json not exist, creating
  [Error] [2025-01-25 21:39:00] Create config.json failed: Generated new config file (config.json), please edit it and re-run this program.
  [Warning] [2025-01-25 21:39:00] ==========
  Generated new config file (config.json), please edit it and re-run this program. 
  ```
- 打开`config.json` 文件
  ```shell
  nano config.json
  ```
  会出现按照下面的说明编辑`config.json`文件，编辑完成后按`Ctrl+X`后按`Y`确认修改，最后按`回车键`退出
  ```python
  {
    "version": "2025.1.18.1",
    "debug": false,
    "host": "0.0.0.0",
    "port": 9010,
    "timezone": "Asia/Shanghai",
    "metrics": true,
    "secret": "", # 这里填写你要设置的密码
    "status_list": [
        {
            "id": 0,
            "name": "活着", # 可以更改成自己想要的状态
            "desc": "目前在线，可以通过任何可用的联系方式联系本人。", # 可以更改成自己想要的描述
            "color": "awake"
        },
        {
            "id": 1,
            "name": "似了", # 可以更改成自己想要的状态
            "desc": "睡似了或其他原因不在线，紧急情况请使用电话联系。", # 可以更改成自己想要的描述
            "color": "sleeping"
        }
    ],
    "refresh": 20000, # 填写你要的网页自动刷新时间间隔，20000ms=20秒
    "data_check_interval": 30,
    "other": {
              "user": "User", # 填写你想在网页上显示的昵称
              "background": "https://imgapi.siiway.top/image",
              "alpha": 0.85,
              "learn_more": "搭建教程",
              "repo": "https://github.com/univers629/sleepy",
              "more_text": "＞﹏＜<br/>已被视奸 <span id='finicount_views'>(未知)</span> 次<script async src='https://finicounter.eu.org/finicounter.js'></script>", #这里还可以填你的联系方式
              "device_status_slice": 50 # 设备状态从开头截取多少文字显示 (防止窗口标题过长, 设置为 0 禁用)
    }
  }
  ```
- 再次输入命令启动`sleepy`项目
  ```shell
  python3 server.py
  ```
  你会看到以下类似结果，代表`sleepy`项目已成功启动
  ```python
  [Info] [2025-01-25 22:01:03] Could not find data.json, creating.
  [Info] [2025-01-25 22:01:03] [timer_check] started, interval: 30 seconds.
  [Info] [2025-01-25 22:01:03] Note: metrics enabled, open /metrics to see your count.
  [Info] [2025-01-25 22:01:03] Metrics data init
  * Serving Flask app 'server'
  * Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  * Running on all addresses (0.0.0.0)
  * Running on http://127.0.0.1:9010
  * Running on http://10.0.0.4:9010
  Press CTRL+C to quit
  ```
- 此时，在浏览器的新标签页地址栏输入你的域名地址，就可以看到网站页面已启动
> [!IMPORTANT]
> 
> 没有购买域名和部署网站后端的，需要点击跳转到[开启防火墙端口教程](#一开启防火墙端口)，并开启9010端口，在浏览器的新标签页地址栏输入`你的服务器公共IP地址:9010`来打开网站，类似于`192.168.1.1:9010`这样

![部署1](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B21.png?raw=true "部署1")

### (二)将`sleepy`添加到系统级服务放止后台进程被杀
#### 1、新建systemd服务
- 在SSH终端中输入Ctrl+C键结束进程，会看到以下信息
  ```python
  [Info] [2025-01-26 15:42:25] - Request: 127.0.0.1 / 5.34.220.34 : /device/set
  127.0.0.1 - - [26/Jan/2025 15:42:25] "POST /device/set HTTP/1.0" 200 -
  ^CServer exited, saving data...
  Bye.
  ```
- 输入命令新建sleepy服务
  ```shell
  sudo nano /etc/systemd/system/sleepy.service
  ```
  在其中填入以下内容
  ```ini
  [Unit]
  Description=Sleepy Flask Application
  After=network.target

  [Service]
  User=azureuser
  Group=azureuser
  WorkingDirectory=/home/azureuser/sleepy
  ExecStart=/usr/bin/python3 server.py
  Restart=always
  RestartSec=5
  Environment="FLASK_APP=server.py"
  Environment="FLASK_RUN_HOST=127.0.0.1"
  Environment="FLASK_RUN_PORT=9010"

  [Install]
  WantedBy=multi-user.target
  ```
  编辑完成后按`Ctrl+X`后按`Y`确认修改，最后按`回车键`退出
- 重新加载`systemd`配置运行以下命令，让`systemd`重新加载配置文件
  ```shell
  sudo systemctl daemon-reload
  ```
#### 2、启用并启动服务
- 启用服务，使其在开机时自动启动
  ```shell
  sudo systemctl enable sleepy.service
  ```
- 启动服务
  ```shell
  sudo systemctl start sleepy.service
  ```

#### 3、检查服务是否正常运行
- 运行命令
  ```shell
  sudo systemctl status sleepy.service
  ```
  会看到以下类似结果
  ```shell
  azureuser@Debian12:~$ sudo systemctl status sleepy.service
  ● sleepy.service - Sleepy Flask Application
      Loaded: loaded (/etc/systemd/system/sleepy.service; enabled; preset: enabled)
      Active: active (running) since Sun 2025-01-26 15:43:16 CST; 26s ago
    Main PID: 38049 (python3)
        Tasks: 2 (limit: 1003)
      Memory: 22.8M
          CPU: 212ms
      CGroup: /system.slice/sleepy.service
              └─38049 /usr/bin/python3 server.py

  1月 26 15:43:17 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:17] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:19 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:19] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:22 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:22] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:25 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:25] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:27 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:27] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:29 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:29] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:32 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:32] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:34 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:34] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:37 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:37] "POST /device/set HTTP/1.0" 2>
  1月 26 15:43:39 Debian12 python3[38049]: 127.0.0.1 - - [26/Jan/2025 15:43:39] "POST /device/set HTTP/1.0" 2>
  ```
> [!TIP]
>
> 以后需要开启或关闭网站服务时用下列命令即可
> 
> 关闭服务
> 
> ```shell
> sudo systemctl stop sleepy.service
> ```
> 
> 开启服务
> 
> ```shell
> sudo systemctl start sleepy.service
> ```
>
> 重启服务
> 
> ```shell
> sudo systemctl restart sleepy.service
> ```

### (三)添加客户端状态
#### 1、添加windows电脑客户端状态
- 点击安装[python](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe)，全部选择默认选项安装即可
> [!TIP]
> 
> 在安装时需要勾选这个选项
> 
> ![部署2](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B22.png?raw=true "部署2")
- 安装`pywin32`，`requests`依赖，按`win`+`R`键打开运行窗口，输入`cmd`后按`回车键`打开命令行工具，一次输入下面命令并按`回车键`确认
  ```shell
  pip install pywin32
  ```
  ```shell
  pip install requests
  ```
- 完成安装后，点击查看[windows客户端程序](https://github.com/univers629/sleepy/blob/main/client/win_device.py)，点击下载按钮下载到电脑上
![部署3](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B23.png?raw=true "部署3")
- 右键点击刚才下载的客户端程序，右键用记事本打开，修改里面的基础配置
![部署4](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B24.png?raw=true "部署4")
> [!TIP]
> 
> 菜单里没有记事本的点击`选择其他应用`找到记事本打开，翻到下面这一段按照说明更改自己的配置
  ```python
  # --- config start
  # 服务地址, 末尾同样不带 /
  SERVER = 'https://你的域名地址  或者  http://你的服务器公共IP:9010'
  # 密钥
  SECRET = '填入自己之前设置的密码'
  # 设备标识符，唯一 (它也会被包含在 api 返回中, 不要包含敏感数据)
  DEVICE_ID = 'device-1'
  # 前台显示名称
  DEVICE_SHOW_NAME = '取一个自己想要在网页上现实的设备名称'
  ```
- 更改完成后关闭并保存，双击`win_device.py`程序打开，回到网站等待一会或者手动刷新即可看到增加了一个设备状态
![部署5](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B25.png?raw=true "部署5")

#### 2、添加安卓移动客户端状态
- 点击下载[Autojs6](https://github.com/SuperMonster003/AutoJs6/releases/download/v6.6.1/autojs6-v6.6.1-universal-7b5e4685.apk)
- 安装软件后授予`无障碍服务权限`并打开`忽略电池优化`
- 像电脑端一样点击查看[安卓客户端程序](https://github.com/univers629/sleepy/blob/main/client/autoxjs_device.js)，点击![部署6](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B26.png?raw=true "部署6")按钮下载`autoxjs_device.js`并传输到手机上
- 在软件首页点击`+`并选择`导入`，将刚才下载的程序导入，点击铅笔图标像刚才配置电脑端一样编辑你的网站地址和密码，最后点击右上角`保存`然后`运行`，就可以到网站上查看到你的安卓客户端信息了
![部署7](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B27.jpg?raw=true "部署7")![部署8](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B28.jpg?raw=true "部署8")![部署9](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B29.jpg?raw=true "部署9")
![部署10](https://github.com/univers629/MacrodownNoteAssets/blob/main/dev/sleepy/asset/images/%E9%83%A8%E7%BD%B210.png?raw=true "部署10")
> [!TIP]
> 
> 可以用同样的方法为平板电脑等设备添加客户端状态，注意不要使用一样的ID导致冲突。

***

## 本教程到此结束，修改时间2025年1月26日
