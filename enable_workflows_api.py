import requests
import os

# 配置信息
GITHUB_TOKEN = os.getenv('GH_TOKEN')  # 从环境变量获取
REPO_OWNER = "你的用户名"  # 替换为你的GitHub用户名
REPO_NAME = "Rules"

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def get_workflows():
    """获取所有工作流"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows"
    response = requests.get(url, headers=headers)
    return response.json()['workflows']

def enable_workflow(workflow_id):
    """启用单个工作流"""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/actions/workflows/{workflow_id}/enable"
    response = requests.put(url, headers=headers)
    return response.status_code == 204

def main():
    print("正在获取工作流列表...")
    workflows = get_workflows()
    
    print(f"找到 {len(workflows)} 个工作流")
    
    enabled_count = 0
    for workflow in workflows:
        workflow_id = workflow['id']
        workflow_name = workflow['name']
        
        print(f"正在启用: {workflow_name}")
        if enable_workflow(workflow_id):
            print(f"✅ {workflow_name} 启用成功")
            enabled_count += 1
        else:
            print(f"❌ {workflow_name} 启用失败")
    
    print(f"\n完成！成功启用了 {enabled_count}/{len(workflows)} 个工作流")

if __name__ == "__main__":
    main()