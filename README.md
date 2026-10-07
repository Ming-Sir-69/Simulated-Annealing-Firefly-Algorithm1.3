<picture>
  <source media="(prefers-color-scheme: dark)" srcset="readme-assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="readme-assets/header-light.svg">
  <img alt="氢能供应链模拟退火萤火虫研究 · ✦ EricMingle69" src="readme-assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="PERSONAL-NOTICE.md">✦ EricMingle69</a>
</p>

# 氢能供应链模拟退火萤火虫研究

## 项目定位

利用模拟退火与萤火虫算法探索政府补贴和氢能供应链，保存无补贴对照、成本、成本分担及环境/补贴模型的 MATLAB 与 Python 实现。

## 阅读入口

| 入口 | 内容 |
| --- | --- |
| [Model 0](model0/) | 无补贴对照 |
| [Model 1](model1/) | 生产与运输成本 |
| [Model 2](model2/) | 成本分担 |
| [Model 3](model3/) | 环境成本与补贴 |
| [结构说明](文件夹结构.txt) | 与实际目录对照阅读 |
| [实验归档](实验数据.zip) | 单独压缩保存的研究材料 |

## 从哪里开始

1. 在对应 model 目录查看参数初始化、适应度函数和 MATLAB 入口。
2. MATLAB 脚本通过 `py.*` 调用 Python 模块；修改版入口包含特定机器的 Windows Python 路径。
3. 复现前核对 MATLAB/Python 兼容版本、模块搜索路径、完整依赖与结果输出位置。

## 使用边界

- 当前没有 `requirements.txt`，不能照用旧的 requirements 安装命令；代码至少依赖 NumPy。
- 实验压缩归档的内容与研究结果没有在此提供独立复现证明。
- 补贴结论和最优解需结合假设、参数来源和独立实验判断，不作为通用性能或政策结论。
- 旧版本说明可在[原研究 README](https://github.com/Ming-Sir-69/Simulated-Annealing-Firefly-Algorithm1.3/blob/56a4ed11d0deabb0c9fcfadcb019781dd5230ef0/README.md) 查阅。

## 来源与原有许可

原仓库未提供 LICENSE/NOTICE。研究材料、代码、协作成果和数据应保留原有来源；具体复用与再分发权限需确认。

---

文档维护：**✦ EricMingle69** · [Ming-Sir-69](https://github.com/Ming-Sir-69)  
[个人标识、许可与权限说明](PERSONAL-NOTICE.md) · 明暗页眉随 GitHub 主题自动切换。
