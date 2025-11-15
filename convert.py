import pandas as pd
import json
import os

# --- 配置区 ---
# 修改：现在我们读取CSV文件

CSV_FILE_PATH = 'websites.csv'
OUTPUT_JS_PATH = 'data.js'


# --- 配置区结束 ---

def create_data_js_from_csv():
    if not os.path.exists(CSV_FILE_PATH):
        print(f"错误：找不到文件 '{CSV_FILE_PATH}'。")
        input("按回车键退出。")
        return

    print(f"正在读取 '{CSV_FILE_PATH}'...")

    try:
        # 修改：使用 pd.read_csv 读取文件
        df = pd.read_csv(CSV_FILE_PATH).fillna('')

        # ... 后续代码与之前完全一样 ...
        required_columns = ['Category', 'Name', 'URL', 'Description', 'Icon']
        if not all(column in df.columns for column in required_columns):
            print(f"错误：CSV文件缺少必要列: {required_columns}")
            input("按回车键退出。")
            return

        all_categories_data = []
        ordered_categories = df['Category'].unique()

        for category_name in ordered_categories:
            category_df = df[df['Category'] == category_name]
            sites_list = []
            for _, row in category_df.iterrows():
                sites_list.append({
                    "name": str(row['Name']), "url": str(row['URL']),
                    "desc": str(row['Description']), "icon": str(row['Icon'])
                })
            all_categories_data.append({"category": category_name, "sites": sites_list})

        js_content = "const webstackData = " + json.dumps(all_categories_data, indent=4, ensure_ascii=False) + ";"

        with open(OUTPUT_JS_PATH, 'w', encoding='utf-8') as f:
            f.write(js_content)

        print(f"\n--- 成功 ---\n'{OUTPUT_JS_PATH}' 文件已成功生成！")

    except Exception as e:
        print(f"--- 发生未知错误 ---\n错误详情: {e}")

    input("\n按回车键退出。")


if __name__ == "__main__":
    create_data_js_from_csv()