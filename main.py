import sys

from data_transfer_object import DTO

global_number = 7


def show_global_vs_local() -> None:
    global_number = 1
    print(f'inside method that shadowed it, {global_number=}')


def pass_in_global_variable(n: int) -> int:
    print(f'inside method, {n=}')
    n += 2
    return n


def modify_global_in_list(lst: list[int]) -> None:
    print(f'inside method, before changing it, {lst=}')
    lst[0] = 9
    print(f'inside method, after changing it, {lst=}')


def manipulate_global_variable_using_object() -> None:
    payload = DTO(global_number)
    print(f'before changing, {payload.number=:.2f}')
    payload.number = 6.5
    print(f'after changing, {payload.number=:.2f}')

def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def print_separator() -> None:
    print('=' * 80)

if __name__ == '__main__':
    print(f'Python version {get_python_version()}')

    print_separator()

    print(f'before shadowing it, {global_number=}')
    show_global_vs_local()
    print(f'after leaving method that shadowed it, {global_number=}')

    print_separator()

    pass_in_global_variable(pass_in_global_variable(global_number))
    print(f'after leaving method that changed it, {global_number=}')

    print_separator()

    global_in_list: list[int] = [global_number]
    print(f'before calling method with list, {global_in_list=}')
    modify_global_in_list(global_in_list)
    print(f'after leaving method that changed it, {global_in_list=}')
    global_number = global_in_list[0]
    print(f'after leaving method that changed it, {global_number=}')

    print_separator()

    manipulate_global_variable_using_object()
