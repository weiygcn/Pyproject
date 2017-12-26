#!/bin/bash/evn python
# coding:utf-8
class Example:
    def echo(self):
        print("In echo()")

    def __enter__(self):
        print('[In __enter__()]')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('[In __exit__()]')
        print('exc_type', exc_type)
        print('exc_val', exc_val)
        print('exc_tb', exc_tb)

    def do_something(self):
        bar = 1 / 0
        return bar + 10


def get_example():
    return Example()


with get_example() as a:
    value = a.do_something()
    print('值是',value)
