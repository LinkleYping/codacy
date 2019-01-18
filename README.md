# 手动录入漏洞信息使用说明

## 文件列表

+ codacy.py: 核心文件
+ demo.docx: 模板文件
+ README.md：rt

## 文件具体说明

### codacy.py

#### url
raw_url = raw_url_p1+str(step)+raw_url_p3
url有三部分组成，因为step是翻页的变量，相同漏洞的p1和p3是一样的，换个漏洞，也就是那个Pattern换了,p3也要换的
step我观察的是20为间隔，如果不对你可以自己调整一下，代码63行

#### def writerror(content,numbers,save_name,demoname='demo.docx')
把信息写到docx文件里，传入参数分别是要写入的list列表，数量，保存的数量名，默认的demo文件名

#### def get_error_info(url='')
这个简单，给url然后得到content

### demo.docx
这是一个很诡异的文件，里面全部是空的表格，因为python-docx操作表格很垃圾！！！所以没法拷贝格式，只能画空空的表格然后填数据，空余的个数你自个把握一下哈，比如我试的这个漏洞，一共77个，所以我就大概复制了这么多个，有点蠢，我脑子不够用啦啦啦QAQ

## 使用方法

自己安装需要的库；
第一步，拼接出url

第二步，writerror(content,len(content),'test.docx')为你的数据找一个名字，xx.docx

基本上，一个漏洞类型一个文件

你还可以自己改进

【比心】