# Just for everyday
Upload code everyday.建个目录督促自己每天往上边传点东西。

**希望能够多多坚持吧，努力争取坚持三位数天数**


_1、搭建物联网_

  https://github.com/phodal/designiot
  这个原项目的GitHub地址，原本想直接fork，但是感觉还是要有自己的东西会比较好就自己创建个玩玩

现在是做到了api写出来了，然后正在纠结前后端交互的事情，COAP我觉得可以放到最后，现在也不在乎连接的速度。

然后之后要做的东西有：

1) Django 前后端交互 Ajax方法

（现在是已经能访问了，之后只要看传感器就行了。）

传感器的事情先放一放，数据库的作业要跟上了，所以到4月12日之前不要求每日上传了。

2）Arduino 串口通信，以及传感器的连接方法


_2、额，现在还不知道，可能在树莓派里头放个挖矿机吧_

_3、还是不知道，可能玩玩apt攻击？_

_4、安卓内核相关知识学习——这个应该主要是笔记，放在博客里吧。 http://drpride.github.io_





## Problems：

1）hjc还是有一些问题.比如

```
<style type="text/css" href="style.css"></style>
```

好像起不到链接css文件的作用。只有换成

```
<link href="./style.css" rel="stylesheet" type="text/css" />
```

才行。

而且

```
<p class="para2 para_bg">
```

使用para_bg类并不能对这个p产生影响

```
p{
    text_align = left;
}
```

也没能实现左对齐




现在这个Arduino_python只是用pyserial这个包在实现一些简单的串口通信，之后的更新详情会记录在那个目录里头的readme.md
目前是能将Arduino里头的信息在python里直接读出来
然后为啥GitHub上python对Arduino的支持这么少？？作为控制器来说python难道不会上层逻辑上更有优势吗？？还是说面向底层的语言会更加有优势吗？？
