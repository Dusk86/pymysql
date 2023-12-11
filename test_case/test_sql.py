import pytest
import allure
from mysql.mysql_client import Mysqldb
from common.assertutil import Assertutil
from log.logger import log

my_db = Mysqldb()

class Testconnect:
    @allure.title('新增一条数据')
    log()
    def test_add(self):
        value = ('09d62332ba088e85987c3e3e9e4ef23f', '图书馆', '2023-12-04 10:41:11')
        with allure.step(f'新增数据为：{value}'):
            add_one = f"insert into bas_building_info_t(id, building_name, update_date) " \
                     "values {value}"
            commit_data = my_db.commit_data(add_one)

    @allure.title('新增多条数据')
    def test_adds(self):
        values = "(''), (''), ('')"

    @allure.title('删除一条数据')
    def test_delete(self):
        with allure.step('删除图书馆'):
            # 删除后，没有返回值，Python 中，如果在函数中有 return 语句但是没有返回任何值,则函数会返回 None
            delete = my_db.commit_data("delete from bas_building_info_t where building_name = '图书馆'")
            print('删除数据-------', delete)  # None
        with allure.step('验证是否删除成功'):
            # sql查不到数据没有返回值，Python 中，如果在函数中有 return 语句但是没有返回任何值,则函数会返回 None
            select = my_db.select_one("select * from bas_building_info_t where building_name = '图书馆'")
            print('选择数据--------', select)  # None
            Assertutil().assert_in_body(select, delete)







