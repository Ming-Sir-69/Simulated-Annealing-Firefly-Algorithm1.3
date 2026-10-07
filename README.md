# Research on Government Subsidies and Hydrogen Energy Supply Chain Based on Simulated Annealing Firefly Algorithm

## 中文阅读入口

氢能供应链与政府补贴研究代码：使用模拟退火与萤火虫算法，按无补贴对照、成本与运输、成本分担、环境与补贴等不同模型保存实验实现。适合研究供应链优化、启发式算法和 MATLAB / Python 联合实验的读者。

1. 先读下方保留的英文研究背景和版本变化。
2. 查看 [model0](model0/)、[model1](model1/)、[model2](model2/) 与 [model3](model3/)，从每个目录的 `initialize_parameters.py`、适应度函数和 MATLAB 入口了解模型假设。
3. 对照 [文件夹结构.txt](文件夹结构.txt) 和实际目录。`实验数据.zip` 是单独的归档，尚未在此说明中展开核验。

### 运行前需要确认

现有 MATLAB 脚本通过 `py.*` 调用同目录 Python 模块；已核对的修改版入口写有特定 Windows Python 安装路径。仓库没有 `requirements.txt`，因此原先的 `pip install -r requirements.txt` 不能直接照用。Python 代码至少导入 NumPy，完整依赖、MATLAB / Python 兼容版本、模块搜索路径和输出位置仍需确认。这里提供阅读入口，不承诺在新的机器上可直接复现。

算法效果、最优解和补贴结论应结合模型假设与独立复现实验判断。下面的 Results 与版本更新保留原研究叙述，未在本次文档整理中复跑或验证。

### 贡献与许可

欢迎在 [Issues](https://github.com/Ming-Sir-69/Simulated-Annealing-Firefly-Algorithm1.3/issues) 讨论依赖清单、可复现的小例子和模型假设，或提交文档 Pull Request。请注明模型目录、入口、版本与预期行为，不把原始实验或未获授权的数据直接提交到公开仓库。

仓库维护：[Ming-Sir-69](https://github.com/Ming-Sir-69)。当前未发现 LICENSE/NOTICE；资料来源和复用授权待确认，不在这里新增许可或版权归属声明。

## Introduction

This repository contains the research and implementation of a study on government subsidies and the hydrogen energy supply chain, utilizing the Simulated Annealing Firefly Algorithm. The project aims to optimize the hydrogen energy supply chain by considering various factors such as production costs, transportation costs, environmental costs, and government subsidies.

## Research Background

Hydrogen energy is a promising alternative to fossil fuels due to its high energy density and environmental benefits. However, the production and distribution of hydrogen involve significant costs and logistical challenges. Government subsidies play a crucial role in promoting the adoption of hydrogen energy by offsetting some of these costs.

This research focuses on three key models to analyze and optimize the hydrogen energy supply chain:

1. **Model 1**: Examines the production and transportation costs.
2. **Model 2**: Incorporates cost-sharing ratios.
3. **Model 3**: Integrates environmental costs and government subsidies.

The Simulated Annealing Firefly Algorithm is used to find optimal solutions for these models, balancing cost efficiency and environmental impact.

## Project Structure

The project is organized into the following directories and files:

```

模型函数/
├── model0/  # 模型0专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model0.py  # 适用于模型0的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model0.m  # 适用于模型0的MATLAB脚本
│   ├── matlab_script_model0_modified.m  # 适用于模型0的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model0.py  # 适用于模型0的模拟退火萤火虫算法文件
├── model1/  # 模型1专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model1.py  # 适用于模型1的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model1.m  # 适用于模型1的MATLAB脚本
│   ├── matlab_script_model1_modified.m  # 适用于模型1的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model1.py  # 适用于模型1的模拟退火萤火虫算法文件
├── model2/  # 模型2专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model2.py  # 适用于模型2的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model2.m  # 适用于模型2的MATLAB脚本
│   ├── matlab_script_model2_modified.m  # 适用于模型2的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model2.py  # 适用于模型2的模拟退火萤火虫算法文件
├── model3/  # 模型3专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model3.py  # 适用于模型3的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model3.m  # 适用于模型3的MATLAB脚本
│   ├── matlab_script_model3_modified.m  # 适用于模型3的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model3.py  # 适用于模型3的模拟退火萤火虫算法文件
├── 初始值.md  # 初始值说明文档
├── 清空命令窗口.m  # 清空命令窗口的MATLAB脚本
├── 文件夹结构.txt  # 文件夹结构说明文件
|── README.md  # 项目介绍文档
├── 实验数据/
│   ├──model0/
│       ├── optimal_solutions/
│   ├──model1/
│       ├── optimal_solutions/
│   ├──model2/
│       ├── optimal_solutions/
|   └──model3/
└       └── optimal_solutions/


```

## Files Description

### model1 Directory

- **adaptive_cooling_rate.py**: Adjusts the cooling rate for the simulated annealing algorithm.
- **adaptive_initial_temperature.py**: Adjusts the initial temperature for the simulated annealing algorithm.
- **calculate_fitness_model1.py**: Calculates the fitness value for Model 1.
- **generate_initial_solutions.py**: Generates initial solutions for the optimization algorithm.
- **initialize_parameters.py**: Initializes the parameters required for the simulation, including production and transportation costs, environmental costs, and subsidy coefficients.
- **matlab_script_model1.m**: MATLAB script to run Model 1 with the Simulated Annealing Firefly Algorithm.
- **objective_function_health_check.py**: Checks the health of the objective function to determine if the algorithm has converged.
- **simulated_annealing_firefly_model1.py**: Implements the Simulated Annealing Firefly Algorithm for Model 1.

### model2 Directory

- **adaptive_cooling_rate.py**: Adjusts the cooling rate for the simulated annealing algorithm.
- **adaptive_initial_temperature.py**: Adjusts the initial temperature for the simulated annealing algorithm.
- **calculate_fitness_model2.py**: Calculates the fitness value for Model 2, including cost-sharing ratios.
- **generate_initial_solutions.py**: Generates initial solutions for the optimization algorithm.
- **initialize_parameters.py**: Initializes the parameters required for the simulation, including production and transportation costs, environmental costs, and subsidy coefficients.
- **matlab_script_model2.m**: MATLAB script to run Model 2 with the Simulated Annealing Firefly Algorithm.
- **objective_function_health_check.py**: Checks the health of the objective function to determine if the algorithm has converged.
- **simulated_annealing_firefly_model2.py**: Implements the Simulated Annealing Firefly Algorithm for Model 2.

### model3 Directory

- **adaptive_cooling_rate.py**: Adjusts the cooling rate for the simulated annealing algorithm.
- **adaptive_initial_temperature.py**: Adjusts the initial temperature for the simulated annealing algorithm.
- **calculate_fitness_model3.py**: Calculates the fitness value for Model 3, integrating environmental costs and government subsidies.
- **generate_initial_solutions.py**: Generates initial solutions for the optimization algorithm.
- **initialize_parameters.py**: Initializes the parameters required for the simulation, including production and transportation costs, environmental costs, and subsidy coefficients.
- **matlab_script_model3.m**: MATLAB script to run Model 3 with the Simulated Annealing Firefly Algorithm.
- **objective_function_health_check.py**: Checks the health of the objective function to determine if the algorithm has converged.
- **simulated_annealing_firefly_model3.py**: Implements the Simulated Annealing Firefly Algorithm for Model 3.

### Other Files

- **初始值.md**: Documentation of initial values.
- **清空命令窗口.m**: MATLAB script to clear the command window.
- **文件夹结构.txt**: Description of the directory structure.
- **README.md**: Introduction and overview of the project.

## Reproduction status / 复现状态

The original project uses MATLAB scripts with Python modules. Begin with the actual `model0/`–`model3/` directories. The checked modified MATLAB scripts set a machine-specific Python path, and the repository does not include `requirements.txt`. Configure the MATLAB/Python bridge and confirm dependencies before attempting reproduction; no turnkey setup is claimed here.

## Results

The results of the simulations will provide insights into the optimal strategies for hydrogen production and transportation under various subsidy policies. The project demonstrates the effectiveness of the Simulated Annealing Firefly Algorithm in optimizing complex supply chain problems.

## PS

**Note**: When running the MATLAB scripts, you may encounter an issue where running one script causes another to fail due to conflicts in the Python environment setup. To resolve this:
- After running a MATLAB script, close the current MATLAB session.
- Open a new MATLAB session and run the next script.

This ensures that each script runs with a fresh Python environment setup.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions and suggestions, use this repository’s GitHub Issues or Pull Requests. Repository maintenance: [Ming-Sir-69](https://github.com/Ming-Sir-69).


### Update Version 1.1

#### Update Content
- Corrected and updated the calculation formula for Model 1, adding the `subsidy_amount` parameter for calculating direct financial subsidies. 🚀
- Data modification process:
  1. Added the `subsidy_amount` parameter in `initialize_parameters.py`. 📝
  2. Used the `subsidy_amount` parameter in `calculate_fitness_model1.py` to calculate subsidies and updated the fitness calculation function. 🔄
- Usage:
  1. Ensure all parameters are initialized in `initialize_parameters.py`. 📂
  2. When performing fitness calculations in `calculate_fitness_model1.py`, ensure the subsidy parameter is used correctly. ✅
  3. Run `matlab_script_model1.m` to conduct the experiment. 🔍

### Update Version 1.2

#### Update Content
- Added a control group model without subsidies (Model 0). 🎉
- Reasons and functions of adding Model 0:
  1. The control group model provides a baseline comparison without subsidies to evaluate the effects of different subsidy policies. 📊
  2. By comparing with the subsidy models, analyze the impact of subsidies on the cost of the hydrogen supply chain to identify the optimal subsidy policies and plans. 🔬
- Usage:
  1. Initialize all parameters in `initialize_parameters.py`. 📂
  2. Use `calculate_fitness_model0.py` for fitness calculation, which does not consider any subsidies, only calculating the total production and transportation costs. 🔄
  3. Run `matlab_script_model0.m` to conduct the experiment and obtain baseline data without subsidies. 🔍

### Update Version 1.3

#### Update Content
- Corrected and updated the calculation formulas for Models 0, 1, and 2 to ensure correct extraction of `production_quantity` and `distance_pipeline` parameters from `params`. 🔧
- Optimized the result saving paths and file naming formats to ensure correct saving of experimental data and optimal solution tables. 📁
- Data modification process:
  1. Defined initial production quantity and pipeline transportation distance in `initialize_parameters.py` and calculated other related parameters based on proportions. 📝
  2. Ensured consistent parameter sources in the fitness calculation files for each model (`calculate_fitness_model0.py`, `calculate_fitness_model1.py`, `calculate_fitness_model2.py`). 🔄
  3. Modified the relevant MATLAB script files (`matlab_script_model0_modified.m`, `matlab_script_model1_modified.m`, `matlab_script_model2_modified.m`) to ensure correct extraction and use of parameters, and optimized the result saving paths and file naming formats. 🔍
  4. Updated the file structure.

- Usage:
  1. Ensure all parameters are initialized in `initialize_parameters.py`. 📂
  2. When performing fitness calculations in the fitness calculation files for each model, ensure the parameters are used correctly. ✅
  3. Run the corresponding MATLAB script files to conduct experiments and obtain experimental data and optimal solution tables for each model. 📊
