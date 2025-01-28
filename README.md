


# 绅士漫画 图片下载器

## 项目概述
这个 Python 脚本 `ImageCrawler.py` 是一个下载 绅士漫画网站漫画的下载工具，它能够从指定的网页中下载图片。脚本使用了 Selenium 和 BeautifulSoup 库，通过多线程的方式进行图片下载，提高了下载效率。

## 功能特性
- **多线程下载**：利用 Python 的 `concurrent.futures` 模块中的 `ThreadPoolExecutor` 实现多线程下载，加快图片下载速度。
- **网页解析**：使用 BeautifulSoup 解析网页 HTML 内容，提取图片链接和相关信息。
- **Selenium 驱动**：使用 Selenium 的 Edge 浏览器驱动来加载网页，处理 JavaScript 渲染的页面。

## 安装与依赖
在运行此脚本之前，你需要确保以下依赖库已经安装：
- `selenium`：用于自动化浏览器操作。
- `beautifulsoup4`：用于解析 HTML 内容。
- `requests`：用于发送 HTTP 请求下载图片。
- `urllib3`：用于处理 HTTP 请求相关操作。

你可以使用以下命令安装这些依赖库：
```sh
pip install selenium beautifulsoup4 requests urllib3
```

此外，你还需要下载并配置 Edge 浏览器驱动（`msedgedriver.exe`），确保驱动的路径与脚本中配置的路径一致。

## 使用方法

### 1. 克隆仓库
首先，你需要将本仓库克隆到本地计算机。打开终端（命令行工具），执行以下命令：
```sh
git clone <仓库地址>
cd <仓库目录>
```
`<仓库地址>` 是本项目在 GitHub 上的仓库地址，`<仓库目录>` 是克隆后本地仓库的目录名。

### 2. 配置脚本
打开 `ImageCrawler.py` 文件，使用文本编辑器（如 Notepad++、VS Code 等）进行以下配置：

#### 2.1 配置图片保存路径
找到以下代码行：
```python
base_folder = r"D:\\Download"
```
将 `D:\\Download` 修改为你希望保存图片的文件夹路径。例如，如果你想将图片保存到 `E:\\Pictures` 文件夹下，可以修改为：
```python
base_folder = r"E:\\Pictures"
```

#### 2.2 配置 Edge 浏览器驱动路径
找到以下代码行：
```python
driver_path = r"C:\\Users\\lihua\\AppData\\Local\\edgedriver_win64\\msedgedriver.exe"
```
将 `C:\\Users\\lihua\\AppData\\Local\\edgedriver_win64\\msedgedriver.exe` 修改为你本地 Edge 浏览器驱动的实际路径。

### 3. 运行脚本
在终端中，执行以下命令来运行脚本：
```sh
python ImageCrawler.py
```

### 4. 输入网址
脚本运行后，会提示你输入要下载图片的网页 URL。输入你想要下载图片的网页地址，然后按回车键。例如：
```
请输入网址: https://wnacg.com
```

### 5. 等待下载完成
脚本会自动打开 Edge 浏览器（无头模式），访问你输入的网页，解析网页内容，提取图片链接，并开始下载图片。下载过程中，脚本会输出详细的日志信息，包括正在处理的网页、找到的图片数量、下载进度等。

### 6. 查看下载结果
下载完成后，你可以在之前配置的图片保存路径下找到下载的图片。图片会按照网页的标题或者网页序号进行分类保存。

## 注意事项
- 脚本在运行过程中会忽略 SSL 证书验证（`verify=False`），请确保你在安全的环境中使用。
- 脚本使用了 `time.sleep()` 来等待网页和图片加载，可能会导致运行时间较长，你可以根据实际情况调整等待时间。

## 贡献指南
如果你发现了任何问题或者有改进的建议，欢迎提交 Issue 或者 Pull Request。

## 许可证
本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)，你可以自由使用、修改和分发本项目。
