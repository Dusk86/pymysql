import pytest
import allure
import logging
from mysql.mysql_client import Mysqldb
from common.assertutil import Assertutil
from log.logger import Log

my_db = Mysqldb()

class Testconnect:
    Log().info('--------------------第一条用例------------------------------')
    @allure.title('新增一条数据')
    def test_add(self):
        with allure.step('新增图书馆'):
            commit_data = my_db.commit_data("insert into bas_building_info_t(id, building_name, building_floors, "
                                            "update_date) "
                                            "values('09d62332ba088e85987c3e3e9e4ef23f', '图书馆(python添加)', 2, '2023-12-15 "
                                            "14:35:55')")
            Log().info('向数据库插入的数据')
            with allure.step('是否添加成功'):
                select = my_db.select_one("select * from bas_building_info_t where building_name = '图书馆(python添加)'")
                Log().info(select)
                # print('控制台打印--------------------------------------', select)
                # Assertutil().assert_in_body(select, commit_data)
                Log().info('数据是否添加成功')
                assert select, '新增数据成功'

    # @allure.title('新增多条数据')
    # def test_adds(self):
    #     values = "(''), (''), ('')"
    #
    # @allure.title('删除一条数据')
    # def test_delete(self):
    #     with allure.step('删除图书馆'):
    #         # 删除后，没有返回值，Python 中，如果在函数中有 return 语句但是没有返回任何值,则函数会返回 None
    #         delete = my_db.commit_data("delete from bas_building_info_t where building_name = '图书馆'")
    #         print('删除数据-------', delete)  # None
    #     with allure.step('验证是否删除成功'):
    #         # sql查不到数据没有返回值，Python 中，如果在函数中有 return 语句但是没有返回任何值,则函数会返回 None
    #         select = my_db.select_one("select * from bas_building_info_t where building_name = '图书馆'")
    #         print('选择数据--------', select)  # None
    #         Assertutil().assert_in_body(select, delete)
