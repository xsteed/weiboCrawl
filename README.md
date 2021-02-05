<!--
 * @Descripttion: 
 * @Author: LJZ
 * @Date: 2021-02-05 16:53:14
 * @LastEditTime: 2021-02-05 17:48:39
-->

### 微博热搜实时平台

### 结果展示
![weibo.gif](https://csgduanzhou-pic.oss-cn-shenzhen.aliyuncs.com/my_self/weibo.gif?versionId=CAEQHBiBgIDEraXGuxciIDA1ZTNjY2Y2ZDY0ZTQ5NWJhYWVmODkxNzAwY2U1OWVm)

具体详情可以查看我CSDN博文

#### 版本说明：
  - mysql可以使用5.0或以上版本
  - python是3.6版本或以上
  
  
#### 配置Mysql数据库：
  - html文件中需要将发送ajax请求的url改成是自己服务器的
  - 修改py和php文件中的数据库配置，改成自己的
  - 最重要是，记得自己的mysql要创建好相应的表
  
```sql
CREATE TABLE `hot_list` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `scores` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=13970 DEFAULT CHARSET=utf8;
```

#### 将这些文件部署在服务器端，并运行weibo.py脚本，前端网页就可以使用了