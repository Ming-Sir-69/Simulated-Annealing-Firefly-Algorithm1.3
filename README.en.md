<picture>
  <source media="(prefers-color-scheme: dark)" srcset="readme-assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="readme-assets/header-light.svg">
  <img alt="Hydrogen Supply Chain SA–Firefly Research · ✦ EricMingle69" src="readme-assets/header-light.svg" width="100%">
</picture>

<p align="center">
  <a href="README.md">简体中文</a> · <a href="README.en.md">English</a> · <a href="PERSONAL-NOTICE.md">✦ EricMingle69</a>
</p>

# Hydrogen Supply Chain SA–Firefly Research

## Purpose

MATLAB and Python research implementations exploring government subsidies and hydrogen supply chains with simulated annealing and firefly algorithms, including a no-subsidy control, costs, cost sharing and environment/subsidy models.

## Repository guide

| Entry | Contents |
| --- | --- |
| [Model 0](model0/) | No-subsidy control |
| [Model 1](model1/) | Production and transportation costs |
| [Model 2](model2/) | Cost sharing |
| [Model 3](model3/) | Environmental costs and subsidies |
| [Structure notes](文件夹结构.txt) | Read alongside the actual tree |
| [Experiment archive](实验数据.zip) | Separately compressed research material |

## Getting started

1. Inspect parameter initialization, fitness functions and MATLAB entries in the corresponding model directory.
2. MATLAB scripts call Python modules through `py.*`; modified entries contain a machine-specific Windows Python path.
3. Before reproduction, establish compatible MATLAB/Python versions, module paths, complete dependencies and output locations.

## Scope and limitations

- There is no `requirements.txt`; the historical requirements-install command is inapplicable. The code imports at least NumPy.
- The compressed experiment archive and research outcomes are not supported here by independent reproduction evidence.
- Assess subsidy conclusions and optimal solutions against assumptions, parameter provenance and independent experiments; they are not general performance or policy conclusions.
- Historical version notes are available in the [original research README](https://github.com/Ming-Sir-69/Simulated-Annealing-Firefly-Algorithm1.3/blob/56a4ed11d0deabb0c9fcfadcb019781dd5230ef0/README.md).

## Sources and existing licenses

The original repository provides no LICENSE/NOTICE. Retain the original sources of research material, code, collaborative contributions and data; confirm reuse and redistribution rights.

---

Documentation maintained by **✦ EricMingle69** · [Ming-Sir-69](https://github.com/Ming-Sir-69)  
[Personal identity, licensing and permissions](PERSONAL-NOTICE.md) · The header follows your GitHub theme.
