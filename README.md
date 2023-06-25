
<p align="center">
  <img width="18%" align="center" src="https://raw.githubusercontent.com/Seattle-233/Melody-Insights/main/PyQt_UI/main/gallery/app/resource/images/logo_red.png" alt="logo">
</p>
  <h1 align="center">
  Melody Insights
</h1>
<p align="center">
  A music preference analysis system based on Netease Cloud Music based on PyQt5
</p>

<p align="center">
  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Platform-Windows-blue?color=#4ec820" alt="Platform Windows"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/Author-Seattle-blue?color=#4ec820.svg " alt="Download"/>
  </a>

  <a style="text-decoration:none">
    <img src="https://img.shields.io/badge/License-MIT-blue?color=#4ec820" alt="MIT"/>
  </a>
</p>


![Interface](https://raw.githubusercontent.com/Seattle-233/Melody-Insights/main/PyQt_UI/docs/source/_static/interface.png)



❗叠甲环节 | 该项目为作者大一下 Python 大作业，因此非常粗糙，仅供参考，烦请各位嘴下留情。若有任何问题，欢迎提出 issue 或者联系作者。如若侵权，请立刻联系作者删除！！！
:---: | :---


## 项目简介

该项目为基于**网易云音乐**的歌曲偏好分析系统，可以爬取用户的相关数据，进行清洗分析，并利用 PyQt5 构建应用，结合 HTML, JS 实现数据可视化。


## 环境要求

- NodeJS 12+
- Python 3.0+
- Python package: `requests`， `pyqt5`， `flask`, `stylecloud`, `jieba`

## 项目依赖的安装📥

安装PyQt-Fluent-Widgets：
```shell
pip install "PyQt-Fluent-Widgets[full]" -i https://pypi.org/simple/
```

安装 `requests`， `pyqt5`， `flask`
```shell
pip install requests
pip install pyqt5
pip install flask
```

Tips: 如果你的网络环境不佳，可以使用清华源进行加速，例如：

```shell
pip install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 项目部署及运行

### 1. 创建虚拟环境

这里使用 conda 作为例子
    
    ```shell
    conda create -n melody python = 3.8
    conda activate melody
    ```


### 2. 启动网易云 Local Server

进入 ncm 文件夹，运行 `app.js`, 启动 Local Server
```shell
cd ncm
node app.js
```

若出现以下提示，则说明运行成功

```shell
Server running at http://localhost:3000
```

服务器启动默认端口为 3000,若不想使用 3000 端口,可使用以下命令: 
```shell
$ set PORT=4000 && node app.js
```

### 2. 启动 flask 的 Local Server

```shell
cd PyQt_UI/main/gallery
python flsk.py
```

出现以下内容则说明运行成功

```shell
* Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
```

### 3. 启动 Melody Insights 的 PyQt UI
```shell
cd PyQt_UI/main/gallery
python main.py
```
### 4. Enjoy it! ✌️

### PyQt UI 特点

- 优秀的自适应，能够适配不同分辨率的屏幕
- 拥有浅色/深色两种主题，用户可以随心切换
- 优秀的美观性，拥有丰富的动画效果
- 支持多国语言，适应不同用户群体
- 仿照 Windows Fluent 风格，呈现简洁美观的界面
- 优秀的交互体验，完全接轨 Windows 用户的操作逻辑
- 功能完善的设置界面，能够满足用户的基本个性化需求

## 功能

- 支持使用网易云用户 ID 登录
- 支持展示用户最喜欢的100首歌曲
- 支持展示用户曲风标签统计
- 支持展示用户曲风标签的数据分析
- 支持通过用户爱听的曲风进行歌曲推荐
- 支持获取用户常听的歌的评论区内容，并以词云图展示内容


## TODO
- [ ] 二维码登录
- [ ] 歌曲搜索页面
- [ ] 获取每日推荐
- [ ] 实现应用内播放歌曲



## 参考说明与鸣谢

本项目在实现的的过程中参考了以下内容：

- [网易云音乐 API](https://github.com/Binaryify/NeteaseCloudMusicApi): 该项目的部分用户数据通过该项目获取
- [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets): 为 PyQt5 提供 Fluent 风格的 UI 组件，帮助了该项目的 UI 实现
- [网易云音乐]( https://music.163.com/): 该项目的所有用户数据来源于网易云音乐
- [ECharts](https://echarts.apache.org/zh/index.html): 该项目的数据可视化部分使用了 ECharts 辅助实现
- [miHoYo]( https://www.mihoyo.com/): 该项目的私货部分来源于米哈游的游戏作品《崩坏：星穹铁道》





