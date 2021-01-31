#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml
from pythoncode.Calculator import Calculator


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
    # return (datas['add']['datas'], datas['add']['ids'])
    return datas


# yaml json excel csv xml
# 测试类
class TestCalc:
    datas: list = get_datas()

    # 前置条件
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件
    def teardown_class(self):
        print("结束计算")

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', get_datas()['add']['datas'], ids=get_datas()['add']['ids'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a,b)
        assert expect == result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect', get_datas()['subtract']['datas'], ids=get_datas()['subtract']['ids'])
    def test_subtract(self, a, b, expect):
        result = self.calc.subtract(a,b)
        assert expect == result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect', get_datas()['multiply']['datas'], ids=get_datas()['multiply']['ids'])
    def test_multiply(self, a, b, expect):
        result = self.calc.multiply(a,b)
        assert expect == result

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect', get_datas()['div']['datas'], ids=get_datas()['div']['ids'])
    def test_div(self, a, b, expect):
        if b == 0:
            try:
                self.calc.div(a, b)
            except ZeroDivisionError as e:
                print("除数不能为0")
        else:
            result = self.calc.div(a, b)
            assert result == expect


if __name__ == '__main__':
    pytest.main(["-v","-s"])