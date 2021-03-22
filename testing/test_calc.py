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

    @pytest.mark.parametrize('a,b,exp',[[1,2,3],[1.1,2.2,3.3],[-1,1,0]],ids=['inttest','floattest','zerotest'])
    def test_add(self,a,b,exp):
        # c = Calculator()
        rst = self.calc.add(a,b)
        assert round(rst,2) == exp

    @pytest.mark.parametrize('a,b,exp',[[2,3,-1],[4,4,0],[0.3,0.2,0.1]])
    def test_sub(self,a,b,exp):
        rst = self.calc.sub(a,b)
        assert round(rst,2) == exp

    def test_mul(self):
        rst = self.calc.mul(2,3)
        assert rst == 6

    @pytest.mark.parametrize('a,b,exp',[[3,3,1],[3,0,2],[5,4,1.25]])
    def test_div(self,a,b,exp):
        if b == 0:
            with pytest.raises(ZeroDivisionError):
                self.calc.div(a,b)
        else:
            rst = self.calc.div(a,b)
            assert round(rst,3) == exp

