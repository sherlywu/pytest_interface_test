"""
运行整个项目的入口文件
"""
import pytest
import time

if __name__ == "__main__":
    current_day = time.strftime("%Y-%m-%d")
    pytest.main(['testcases', '-v', f'--html=reports/report_{current_day}.html'])