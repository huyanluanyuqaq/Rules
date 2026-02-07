#!/bin/bash

# 批量启用GitHub Actions工作流脚本
# 使用前需要安装GitHub CLI: https://cli.github.com/

REPO_OWNER="你的用户名"
REPO_NAME="Rules"

echo "正在启用 $REPO_OWNER/$REPO_NAME 的所有工作流..."

# 登录GitHub CLI（如果尚未登录）
gh auth status || gh auth login

# 启用所有工作流
gh workflow enable --all -R "$REPO_OWNER/$REPO_NAME"

echo "所有工作流已启用！"
echo "验证工作流状态："
gh workflow list -R "$REPO_OWNER/$REPO_NAME"