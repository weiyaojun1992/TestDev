#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from pycode.calculator import Calculator


class TestCalc():
    def setup_class(self):
        print("计算开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,exp',[[1,2,3],[1.1,2.2,3.3],[-1,-1,0]],ids=['inttest','floattest','zerotest'])
    def test_add(self,a,b,exp):
        # c = Calculator()
        rst = self.calc.add(a,b)
        assert rst == exp

    def test_sub(self):
        rst = self.calc.sub(2,1)
        assert rst == 2

    def test_mul(self):
        rst = self.calc.mul(2,3)
        assert rst == 6