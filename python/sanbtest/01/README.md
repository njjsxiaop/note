# 后端上机题

## 问题描述

1. 自动 wrap markdown 文本中的裸链接，例如：将 `https://www.shanbay.com` 转换成 `[https://www.shanbay.com](https://www.shanbay.com)`
2. 抽取 markdown 文本中图片链接

## 要求

- 请补充本项目中的代码，使得测试可以全部通过
- 如果用到第三方库，请添加到 `requirements.txt` 中
- 提交结果的时候，将 `markdown.py` 和 `requirements.txt` 两个文件提交给我们即可

## 提示

1. wrap 链接的时候要注意，只能wrap文本中没有正确标记的链接。所以例如 `[Google](https://www.google.com)` 中的链接是不能被重复 wrap 的
2. markdown支持html标签，所以图片有两种形式: `![img name](http://example.com/img.jpg)`与`<img src=http://example.com/img.jpg></img>`
