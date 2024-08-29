import os
import json

def generate_json_config(png_folder, output_file):
    # 基础配置
    config = {
        "name": "Yaphet Icon",
        "description": "@YaphetLee2002的自用Quantumult X 图标集",
        "icons": []
    }

    # 遍历PNG文件夹
    for filename in os.listdir(png_folder):
        if filename.lower().endswith('.png'):
            name = os.path.splitext(filename)[0]
            url = f"https://raw.githubusercontent.com/YaphetLee2002/QuantumultRules/main/Icon/Flag-icon/{filename}"
            
            icon = {
                "name": name,
                "url": url
            }
            
            config["icons"].append(icon)

    # 将配置写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)

    print(f"JSON配置文件已生成: {output_file}")

# 使用示例
png_folder = 'Flag-icon'
output_file = 'icon_config.json'
generate_json_config(png_folder, output_file)
