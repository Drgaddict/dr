#理解pytest的框架结构setup和teardown
import pytest
#pytest中一个模块就是一个文件，setup_
#这是类外的测试用例
def setup_module():
    print("\n￥￥￥￥￥teardwown module:整个模块结束只执行一次￥￥￥￥￥");
def teardown_module():
    print("\n￥￥￥￥￥setup module:整个模块结束只执行一次￥￥￥￥￥");
def setup_function():
    print("\nsetup function: 每个不在类中的用例开始前执行！");
def teardown_function():
    print("\nteardown function: 每个不在类中的用例结束后执行！");
def test_one():
    print("\n正在执行模块： test one ")
def test_tow():
    print("\n正在执行模块： test tow")
#测试类
class TestCase():
    def stup_class(self):
        print("**setup class:class类里面所有用例执行前执行")
    def teardown_class(self):
        print("**teardown class:class类里面所有用例执行后执行")
    def setup(self):
        print("setup: 每个用例开始前都会执行")
    def  teardown(self):
        print("teardown: 每个用例结束后都会执行")
    def test_three(self):
        print("正在执行模块： test three")
    def test_four(self):
        print("正在执行模块： test four")