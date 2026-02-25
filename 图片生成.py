import requests
import os
from urllib.parse import quote

def generate_image(api_key, model, prompt):
    """
    核心生成图片函数：接收API、模型、提示词，生成并保存图片
    """
    # 拼接符合规则的完整URL（提示词URL编码）
    encoded_prompt = quote(prompt)
    full_url = f"https://gen.pollinations.ai/image/{encoded_prompt}?model={model}&key={api_key}"
    
    print(f"\n🔗 拼接后的完整请求链接：\n{full_url}")
    print("\n🔄 正在调用API生成图像（请等待10-30秒）...")

    try:
        # 发送请求获取图像数据
        response = requests.get(full_url, timeout=60)
        response.raise_for_status()

        # 保存图像到本地
        safe_prompt = prompt.replace(" ", "_").replace("/", "_").replace("\\", "_")[:15]
        filename = f"pollinations_{model}_{safe_prompt}.png"
        with open(filename, "wb") as f:
            f.write(response.content)

        # 提示成功信息
        print(f"\n✅ 图像生成并保存成功！")
        print(f"📂 保存路径：{os.path.abspath(filename)}")
        print(f"💡 也可直接在浏览器打开：{full_url}")
    except requests.exceptions.Timeout:
        print("\n❌ 错误：生成图像超时（超过60秒），请重试！")
    except requests.exceptions.HTTPError as e:
        print(f"\n❌ HTTP错误（API/模型可能错误）：{e}")
    except requests.exceptions.ConnectionError:
        print("\n❌ 错误：网络连接失败，请检查网络！")
    except Exception as e:
        print(f"\n❌ 未知错误：{e}")

def main():
    """
    主程序：首次输入API和模型，之后循环输入提示词生成图片，支持退出/修改API/模型
    """
    print("===== Pollinations AI 持续图像生成工具 =====\n")
    # 1. 首次输入API密钥和生成模型（只需输入一次）
    api_key = input("请输入你的API密钥：").strip()
    while not api_key:
        print("❌ API密钥不能为空！")
        api_key = input("请重新输入API密钥：").strip()
    
    model = input("请输入要使用的生成模型：").strip()
    while not model:
        print("❌ 生成模型不能为空！")
        model = input("请重新输入生成模型：").strip()

    # 2. 循环生成图片，直到用户选择退出
    while True:
        print("\n" + "-"*40)
        # 提供操作选项
        choice = input("请选择操作：\n1. 输入新提示词生成图片\n2. 修改API密钥/生成模型\n3. 退出程序\n请输入数字（1/2/3）：").strip()
        
        if choice == "1":
            # 输入提示词生成图片
            prompt = input("\n请输入图像提示词：").strip()
            if not prompt:
                print("❌ 提示词不能为空！跳过本次生成。")
                continue
            generate_image(api_key, model, prompt)
        
        elif choice == "2":
            # 修改API或模型
            print("\n📝 开始修改配置：")
            new_api = input(f"当前API密钥：{api_key}\n输入新API密钥（直接回车则保留原密钥）：").strip()
            if new_api:
                api_key = new_api
            
            new_model = input(f"当前生成模型：{model}\n输入新生成模型（直接回车则保留原模型）：").strip()
            if new_model:
                model = new_model
            print("✅ 配置修改完成！")
        
        elif choice == "3":
            # 退出程序
            print("\n👋 程序已退出，感谢使用！")
            break
        
        else:
            # 无效选项提示
            print("❌ 无效选项，请输入1、2或3！")

if __name__ == "__main__":
    main()