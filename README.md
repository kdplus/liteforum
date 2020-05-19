# liteforum
拟V2EX设计的初级DJANGO论坛应用

## 视频上传
* 使用七牛云python-sdk上传
* __需要__在view.py里的add_post部分里的qiniu处将'bucket_src',qiniu.Auth('','')三个位置分别改为自己的七牛空间,ak,sk.详见[七牛云文档](http://developer.qiniu.com/docs/v6/sdk/python-sdk.html)
* 上传后立即执行转码,代码同在qiniu注释下方.详见[七牛运转码](http://developer.qiniu.com/docs/v6/sdk/python-sdk.html#pfop)
* 程序将自动为每一个新视频建立新的.xml文件前缀为文件名.mp4
* __需要__将绝对路径改为自己的路径(相对路径暂时报错)

## 使用到的第三方app
* grappelli(美化admin)[文档](http://django-grappelli.readthedocs.org/en/latest/quickstart.html#installation)
* django_gravatar(使用邮箱头像)[文档](https://pypi.python.org/pypi/django-gravatar2)
* pagedown,markdown_deux(支持markdown)[文档](https://pypi.python.org/pypi/django-pagedown/0.1.0)  [文档2](https://pypi.python.org/pypi/django-markdown-deux)
* django_comments,disqus(评论,暂时搁置)[文档](http://django-contrib-comments.readthedocs.org/en/latest/quickstart.html)  [文档2](http://django-disqus.readthedocs.org/en/latest/installation.html?highlight=api)
* 以上app__需要__下载安装

## 备注
* clone后需要调整setting.py中database项
* 执行python manage.py makemigrations
* 执行python manage.py makemigrate
* 执行python manage.py collectstatic
* 其他自行调整

## TODO
* comments
* like it
* tags
* 关注
* 收藏
* 个人删改权限
* 提醒
* 个人页面
* 个人信息补全

## 目前效果
![image](https://user-images.githubusercontent.com/3047375/82343618-0ddd4700-9a2e-11ea-9563-fa913ba57ad2.png)
![image](https://user-images.githubusercontent.com/3047375/82343646-13d32800-9a2e-11ea-991c-45a9f68f92e7.png)
![image](https://user-images.githubusercontent.com/3047375/82343631-10d83780-9a2e-11ea-826c-6d000b457e08.png)
![image](https://user-images.githubusercontent.com/3047375/82343657-16ce1880-9a2e-11ea-85fb-ff03abadfa1a.png)
![image](https://user-images.githubusercontent.com/3047375/82343672-1a619f80-9a2e-11ea-8c6f-1190bbd5282e.png)
![image](https://user-images.githubusercontent.com/3047375/82343679-1cc3f980-9a2e-11ea-914c-2349aa9ce6b1.png)
![image](https://user-images.githubusercontent.com/3047375/82343689-1fbeea00-9a2e-11ea-823d-4191d2410e99.png)
![image](https://user-images.githubusercontent.com/3047375/82343706-23527100-9a2e-11ea-9072-819e4bc9cb08.png)
![image](https://user-images.githubusercontent.com/3047375/82343718-264d6180-9a2e-11ea-883d-18a9e078d083.png)
![image](https://user-images.githubusercontent.com/3047375/82343731-29e0e880-9a2e-11ea-9f1b-7b504226a7f0.png)
![image](https://user-images.githubusercontent.com/3047375/82343744-2fd6c980-9a2e-11ea-91dd-499bbb4838a7.png)
![image](https://user-images.githubusercontent.com/3047375/82343753-32392380-9a2e-11ea-8c42-4faaa8f8efa8.png)
![image](https://user-images.githubusercontent.com/3047375/82343769-35ccaa80-9a2e-11ea-9556-c077331065ea.png)

