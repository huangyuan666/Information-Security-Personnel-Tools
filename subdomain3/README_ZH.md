# Subdomain3

![version](https://img.shields.io/badge/version-2.1-green.svg) ![stars](https://img.shields.io/github/stars/yanxiu0614/subdomain3.svg) ![forks](https://img.shields.io/github/forks/yanxiu0614/subdomain3.svg)  ![language](https://img.shields.io/badge/language-python2%2B-green.svg) ![language](https://img.shields.io/badge/language-python3%2B-green.svg)

**README.md in [English](https://github.com/yanxiu0614/subdomain3/blob/master/README.md)**

## CDN搜集计划
非常感谢各位小伙伴对subdomian3的肯定,目前由于个人时间有限,cname的搜集一直处于停滞状态,导致程序识别CDN的广度不够,为后期IP的搜集增加了很多困难,所以希望借助大家的力量共同搜集.开启方式很简单,只需要设置-c命令为y,然后把爆破之后result文件下的cname.txt文件发送到邮箱:yanxiu0614@gmail.com.我会在汇总分析对字典进行扩充,并上传到项目之中.如果有啥问题或者建议,也欢迎与我微博互动，微博：<a href="https://weibo.com/yanxiu0" rel="nofollow">彦修</a>

## 描述
Subdomain3是新一代子域名爆破工具,它帮助渗透测试者相比与其他工具更快发现更多的信息,这些信息包括子域名,IP,CDN信息等,开始使用它吧!

## 截图
medium 模式下的截图:

![](screenshot.png)

## 特性

* 更快

三种速度模式. 用户也可以修改配置文件(/lib/config.py) 来获得更高的速度.
* CDN识别支持

可以判定域名是否使用了CDN.
* 标准C段支持

可以对未使用CDN的域名IP进行分类.
* 多级域名支持

可以发现多级域名,无限制.
* 大字典支持

可以支持百万级字典
* 更少的资源占用

1个CPU/1GB内存/1Mbps带宽 即可获得很高速度
* 更智能

支持从其他渠道导入子域名，同时会将部分字段导入字典二次爆破，从而更准确。

## 开始

```
git clone https://github.com/yanxiu0614/subdomain3.git

pip install -r requirement.txt

python2/3 brutedns.py -d tagetdomain -s high -l 5
```
## 使用方法

Short Form    | Long Form     | Description
------------- | ------------- |-------------
-d            | --domain      | 目标域名,例如: baidu.com
-s            | --speed       | 速度模式,三种速度模式:fast,medium,low
-l            | --level       | 例子: 2:baidu.com; 3:world.baidu.com;
-f            | --file        | 使用文件,每行一个子域名
-c            | --cdn         | 开启CDN搜集,y或者n


## 致谢:

- <a href="https://github.com/smarttang" target="view_window">smarttang(Tangyucong)</a>
- <a href="https://security.yirendai.com/" target="view_window">宜人贷安全部</a>


## 日志:

- 2018-10-6: 优化了api的使用，支持模块的复用，从而可以内嵌到其他模块之中。优化了域名的去重策略，避免大量无效域名；

- 2018-2-14: 修复报错问题

- 2018-1-9: CDN搜集计划，增加搜集cname选项。

- 2017-11-11:支持导入其他渠道收集的子域名结果（约定文件名为：target_domain.log，并且与brutedns.py文件在同一目录下），程序会对结果进行字段提取加入字典，更加精确;API调用更加方便;

- 2017-10-26:优化过程;修复BUG

- 2017-10-11:重构了部分代码;支持API调用;结果更加易读;更新了CDN厂商;修改了扫描算法,更快速;删除了验证域名脚本;

- 2017-6-17: 删除了泛解析选项(-p t/f);添加了配置文件;优化了泛解析策略;

- 2017-5-2: 添加了域名验证选项;修复了泛解析bug;更新了CDN列表等;

- 2017-4-21: 优化了子域名的爆破策略;提升了速度;

- 2017-3-23: 添加了泛解析选项(-p t/f)

- 2017-3-17: 大字典支持.支持百万级;

- 2017-3-10: 添加了文件中域名爆破的支持;更新了CDN厂商;

- 2017-2-26: 多级域名支持,没有级数上限;较大字典支持;内存占用为原来四分之一;更快;

- 2017-2-24: 支持mac os等


&copy;<a href="https://github.com/sixtant" target="_blank">Sixtant Security Lab</a> 2016-2017