# Subdomain3

Subdomain3是新一代子域名爆破工具,它帮助渗透测试者相比与其他工具更快发现更多的信息,这些信息包括子域名,IP,CDN信息等,开始使用它吧!

##### 特性

1. 更快
三种速度模式. 用户也可以修改配置文件(/lib/config.py) 来获得更高的速度.

2. CDN识别支持
可以判定域名是否使用了CDN.

3. 标准C段支持
可以对未使用CDN的域名IP进行分类.

4. 多级域名支持
可以发现多级域名,无限制.

5. 大字典支持
可以支持百万级字典

6. 更少的资源占用
1个CPU/1GB内存/1Mbps带宽 即可获得很高速度

7. 更智能
支持从其他渠道导入子域名，同时会将部分字段导入字典二次爆破，从而更准确。


##### 使用方法
Short Form	Long Form	Description
-d		--domain	目标域名,例如: baidu.com
-s		--speed		速度模式,三种速度模式:fast,medium,low
-l		--level		例子: 2:w.baidu.com; 3:w.w.baidu.com;
-f		--file		使用文件,每行一个子域名
-c		--cdn		开启CDN搜集,y或者n
-f1		--sub_file	一级域名字典
-f2		--next_sub_file	二级域名字典
-f3		--other_file	外部域名结果


![version](https://img.shields.io/badge/version-2.1-green.svg) ![stars](https://img.shields.io/github/stars/yanxiu0614/subdomain3.svg) ![forks](https://img.shields.io/github/forks/yanxiu0614/subdomain3.svg)  ![language](https://img.shields.io/badge/language-python2%2B-green.svg) ![language](https://img.shields.io/badge/language-python3%2B-green.svg)

**README.md in [Chinese 中文](https://github.com/yanxiu0614/subdomain3/blob/master/README_ZH.md)**

## CDN PLAN
Hello,my friend,I am very happy that the tool can help you. Now ,I need your help, and for this tool can be more efficient and easy to use.I suggest that you set cdn(command) is y when you use the tool ,and send the file(/result/cname.txt) to me(email:yanxiu0614@gmail.com).I promise that the cnames will be used to enrich dict of cdn_servers in this project. . Thank you!


## Description
Subdomain3 is a new generation of tool , It helps penetration testers to discover more information  in a shorter time than other tools.The  information includes subdomains, IP, CDN, and so on. Please enjoy it.

## Screenshot
medium pattern for speed

![](screenshot.png)

## Features

* More quick

Three patterns for speed. User can modify the configuration(/lib/config.py) file to speed-up.
* CDN support

Determines whether the subdomain  uses CDN storage by searching list of CDN severs.
* RFC CIDR

Sorting ip and report CIDR(example 1.1.1.1/24)
* Multi-level subdomain support

Discover more subdomains,example:admin.test.xx.com
* Big dict support

Million of subs support
* Less resource consumption

1 CPU/1GB Memory/1Mbps bandwidth
* More intelligent

The strategy of dynamically adjusting of dic by importing subdomains from other sorces，suppport；


## Getting started

```
git clone https://github.com/yanxiu0614/subdomain3.git

pip install -r requirement.txt

python2/3 brutedns.py -d tagetdomain -s high -l 5
```
## Usage

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-d            | --domain      | target domain,for example: baidu.com
-s            | --speed       | speed,three patterns:fast,medium,low
-l            | --level       | example: 2:baidu.com; 3:world.baidu.com;
-f            | --file        | The list of target domain
-c            | --cdn         | n or y,collect cnames

## Thanks:

- <a href="https://github.com/smarttang" target="view_window">smarttang(Tangyucong)</a>
- <a href="https://security.yirendai.com/" target="view_window">Yirendai security department</a>


## Changelog:

- 2018-10-6: api support,import brutedns_api and you will get the number of results in the end;Optimized the deduplication strategy;

- 2018-2-14: fix issue(TypeError: argument of type 'NoneType' is not iterable)

- 2018-1-9: CDN PLAN； add opthon oc collecting cname (-c --cdn  t/f)

- 2017-11-11: import subdomains from other sources support（You should create a new file of target_domain.log, and put it with 'brutedns.py' in the same directory），it will improve the accuracy；it is more convenient for use API；

- 2017-10-26: optimize the  processes；fix bug;

- 2017-10-11:Rebuild part of the program; api support; result is more readable；update cdn-severs；faster

- 2017-6-17: delete universal parse opthon(-p t/f);add a file of config;optimze strategy for universal parse

- 2017-5-2: add a module(validate the domain),please modify "result_name" in the validate_domain.py if you will use it;fix universal bug;update cdn-servers,etc

- 2017-4-21: optimze strategy for generating subname，improve the speed

- 2017-3-23: add universal parse opthon(-p t/f)

- 2017-3-17: big dict support(for example: two million)

- 2017-3-10: read several domains from file support(-f domains) support;update cdn-servers

- 2017-2-26: multilevel domain support(no upper limit);big dict support;take up about a third to a quarter as much memory; faster

- 2017-2-24: mac support




&copy;<a href="https://github.com/sixtant" target="_blank">Sixtant Security Lab</a> 2016-2017
