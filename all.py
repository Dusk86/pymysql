import os
import pytest

if __name__ == '__main__':
    pytest.main()
    os.system("allure generate ./reports/tmp -o ./reports/report --clean")

    #        生成测试报告，将json文件生成报告保存在指定目录(report/html)下
    #
    #         allure generate 测试结果数据所在目录 -o 测试报告保存的目录   --clean
    #
    #         --clean 目的是先清空测试报告目录，再生成新的测试报告
