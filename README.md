# Weibo_Spider

1、开发环境
---------
* python3.6
* pycharm
* 所需依赖：re datetime requests BeautifulSoup webdriver  

2、项目结构
---------
* search_spider --根据关键字和时间进行爬取的模块  
----hour_fenge.py 时间分隔函数：对要搜索的时间期限进行以每小时为单位的划分，返回包含所有时间单位的列表  
----search_start.py 根据关键字和时间条件进行爬取的主要函数：其中包括爬取某页全部微博、微博所有页数的计算、保存为csv文件等功能  
* tools --工具模块  
----Cookie_Process.py cookie处理函数：其中包括获取文件中存储的cookie、更新文件中存储的cookie等功能  
----Date_Process.py 时间处理函数：其中包括对爬取到微博的不同时间格式进行统一  
----Emoji_Process.py 表情处理函数：清除掉包含的utf8bm4编码格式的表情  
----Weibo_Driver.py 获取全文微博处理函数：展开需要获取全文的微博并提取  
----Number_Process.py 转发、评论数处理函数:对爬取到的微博的转发、评论数进行统一  

3、使用介绍  
--------
* 需要获取Cookie，Cookie存于目录下的cookie.file中  
* 手动获取Cookie的操作如下：使用谷歌浏览器登录https://weibo.cn/， 登陆成功后打开浏览器开发工具，选择network,点击weibo.cn，查看Request Headers中的Cookie  
* 运行search_start即可使用，运行时输入要爬取的微博关键字和时间范围，时间格式为年-月-日-时(eg. 2020-5-1-0)。运行时会提示是否更新Cookie，如不更新，输入n/N即可  
* 运行过程中报错基本都可通过更新Cookie解决  
