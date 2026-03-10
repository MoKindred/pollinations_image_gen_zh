### 核心说明
#### 1. 前提条件（仅需1步）
本程序需要 `requests` 库来处理网络请求。打开电脑的**命令提示符（Windows）** 或**终端（Mac/Linux）**，运行以下命令安装该库：
```bash
pip install requests
```
- 若出现“pip 未被识别”错误：重新安装 Python，并在安装过程中勾选“Add Python to PATH”（将Python添加到系统路径）选项。

#### 2. 程序运行方法（分步操作）
1. 将完整代码复制到文本编辑器中（如记事本、VS Code）。
2. 将文件保存为 `.py` 后缀（例如 `pollinations_image_generator.py`）。
3. 双击该 `.py` 文件运行程序，随后按照屏幕提示操作：
   - 首先，输入你的 API 密钥 → 按下回车键。
   - 接着，输入生成模型（例如 `zimage`）→ 按下回车键。
   - 选择选项 `1` 输入提示词（例如 `a small cat`，即“一只小猫”）→ 程序会自动生成并保存图片。
   - 生成完成后程序不会退出——你可以反复输入新的提示词，或选择 `3` 退出程序。

#### 3. 核心 URL 规则（重要）
程序严格遵循以下 URL 格式调用 Pollinations AI 接口：
```
https://gen.pollinations.ai/image/{prompt}?model={model}&key={API}
```
- `{prompt}`：你的图片描述（程序会自动编码，避免特殊字符导致错误）。
- `{model}`：你输入的 AI 模型（例如 `zimage`）。
- `{API}`：你的 Pollinations API 密钥。

#### 4. 图片保存规则
生成的图片会保存到该 `.py` 文件所在的**同一文件夹**中。文件名格式为：
```
pollinations_{model}_{shortened_prompt}.png
```
- 示例：`pollinations_zimage_a_small_white_cat.png`（对应提示词“一只白色的小猫”）

### 总结
1. 运行程序前需先安装 `requests` 库，安装失败需检查 Python 的 PATH 配置；
2. 程序运行后可重复输入提示词生成图片，无需反复启动；
3. 图片会按固定命名规则保存在代码文件同目录，URL 格式是调用接口的核心规则。
