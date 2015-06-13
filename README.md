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
![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:26:04屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:26:08屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:26:12屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:23:51屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:24:52屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:24:38屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:25:55屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:25:08屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-124 03:25:17屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:33:51屏幕截图.png)

![](http://7xj463.com1.z0.glb.clouddn.com/2015-06-14 03:34:29屏幕截图.png)
