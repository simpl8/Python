from python.calc import Calc
import pytest
class TestCalc():
    test_add1 = [(1, 1)]
    test_add2 = [(-5, 5.5)]
    test_add3 = [(0, 0)]
    test_add4 = [(-1, 1)]
    test_add5 = [(complex(3, 4), complex(-3, -4))]
    test_add6 = [('hello', 'world')]
    test_add7 = [('', None)]
    #test_add8 = [('x', 'y'), ('m', 'n')]//会当成两组数据
    test_div1 = [(1, 3)]
    test_div2 = [(3, 2)]
    test_div3 = [(3, 0)]
    test_div4 = [(-3, 2)]
    test_div5 = [('hello', 'world')]
    test_div6 = [(0, 145)]
    test_div7 = [(complex(4, 3), complex(3, 4))]
    #test_div8 = [(1, 2), (1, 2)]//会当成两组数据
#测试add方法case：
    @pytest.mark.parametrize('a, b', test_add1)
    def test_add1(self, a, b):
        result = Calc().add(a, b)
        pytest.assume(result == 2)

    @pytest.mark.parametrize('a, b', test_add2)
    def test_add2(self, a, b):
        result = Calc().add(a, b)
        pytest.assume(result == 0.5)

    @pytest.mark.parametrize('a, b', test_add3)
    def test_add3(self, a, b):
        result = Calc().add(a, b)
        pytest.assume(result == 0)

    @pytest.mark.parametrize('a, b', test_add4)
    def test_add4(self, a, b):
        result = Calc().add(a, b)
        pytest.assume(result == 0)

    @pytest.mark.parametrize('a, b', test_add5)
    def test_add5(self, a, b):
        result = Calc().add(a, b)
        pytest.assume(result == 0)

    @pytest.mark.parametrize('a, b', test_add6)
    def test_add6(self, a, b):
        result = Calc().add(a, b)
        pytest.assume(result == "helloworld")

    @pytest.mark.parametrize('a, b', test_add7)
    def test_add7(self, a, b):
        with pytest.raises(TypeError) as e:
            result = Calc().add(a, b)
            assert  str(e.value) == 'can only concatenate str (not "NoneType") to str'

    @pytest.mark.parametrize('a, b', test_add8)

#测试div方法case：
    @pytest.mark.parametrize('a, b',test_div1)
    def test_div1(self,a,b):
        result = Calc().div(a, b)
        pytest.assume(result == 0.3333333333333333)
    @pytest.mark.parametrize('a, b',test_div2)
    def test_div2(self,a,b):
        result = Calc().div(a,b)
        pytest.assume(result == 1.5)

    @pytest.mark.parametrize('a, b', test_div3)
    def test_div3(self, a, b):
        with pytest.raises(ZeroDivisionError) as e:
            result = Calc().div(a, b)
        assert str(e.value) == 'division by zero'

    @pytest.mark.parametrize('a, b', test_div4)
    def test_div4(self, a, b):
        result = Calc().div(a, b)
        pytest.assume(result == -1.5)

    @pytest.mark.parametrize('a, b', test_div5)
    def test_div5(self, a, b):
        with pytest.raises(TypeError) as e:
            result = Calc().div(a, b)
        assert str(e.value) == "unsupported operand type(s) for /: 'str' and 'str'"

    @pytest.mark.parametrize('a, b', test_div6)
    def test_div6(self, a, b):
        result = Calc().div(a, b)
        pytest.assume(result == 0)

    @pytest.mark.parametrize('a, b', test_div7)
    def test_div7(self, a, b):
        result = Calc().div(a, b)
        pytest.assume(result == 0.96-0.28j)

if __name__ == '__main__':
    pytest.main(['-s','calculatetest.py'])