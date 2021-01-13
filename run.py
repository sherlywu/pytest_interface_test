"""
运行整个项目的入口文件
"""
import pytest
import time

def run_all_cases():
    current_day = time.strftime("%Y-%m-%d")
    pytest.main(['testcases', '-v', '-s', f'--html=reports/report_{current_day}.html'])

def run_case():
    current_day = time.strftime("%Y-%m-%d")
    pytest.main(['testcases', '-v', '-s', '-m tmp', f'--html=reports/report_{current_day}.html'])


if __name__ == "__main__":
    run_all_cases()