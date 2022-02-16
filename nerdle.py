import operator

def _len(n):
    return len(str(n))

operator_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def CheckExpr(num_first, oper_first, num_second, oper_second=None, num_third=None):
    if oper_second in operator_dict:
        if oper_second in ('*', '/') and oper_first in ('+', '-'):
            if num_third * num_second == 0  or (oper_second == '/' and num_second % num_third != 0):
                return None
            else:
                res = operator_dict[oper_first](num_first, operator_dict[oper_second](num_second, num_third))
                if _len(num_first) + _len(num_second) + _len(num_third) + _len(res) == 5:
                    return ''.join([str(num_first), oper_first, str(num_second), oper_second, str(num_third), '=', str(res)])
                else:
                    return None
        else:
            if num_first * num_second * num_third == 0  or (oper_first == '/' and num_first % num_second != 0) or (oper_second == '/' and operator_dict[oper_first](num_first, num_second) % num_third != 0):
                return None
            else:
                res = operator_dict[oper_second](operator_dict[oper_first](num_first, num_second), num_third)
                if _len(num_first) + _len(num_second) + _len(num_third) + _len(res) == 5:
                    return ''.join([str(num_first), oper_first, str(num_second), oper_second, str(num_third), '=', str(res)])
                else:
                    return None
    else:
        if num_first * num_second == 0  or (oper_first == '/' and num_first % num_second != 0):
            return None
        res = operator_dict[oper_first](num_first, num_second)
        if _len(num_first) + _len(num_second) + _len(res) == 6:
            return ''.join([str(num_first), oper_first, str(num_second), '=', str(res)])
        else:
            return None


def GenerateTask(size=8):
    result_list = []
    oper_list = '+-/*='
    for num_first in range(-999, 10000):
        for oper_first in oper_list[:-1]:
            for num_second in range(10 ** (4 - _len(num_first)) * -1, 10 ** (5 - _len(num_first))):
                if _len(num_first) + _len(num_second) <= 4:
                    for oper_second in oper_list:
                        if oper_second != '=' :
                            for num_third in range(int(10 ** (3 - _len(num_first) - _len(num_second)) * -1), 10 ** (4 - _len(num_first) - _len(num_second))):
                                res = CheckExpr(num_first=num_first, oper_first=oper_first, num_second=num_second, oper_second=oper_second, num_third=num_third)
                                if res:
                                    result_list.append(res)
                        else:
                            res = CheckExpr(num_first=num_first, oper_first=oper_first, num_second=num_second)
                            if res:
                                result_list.append(res)
                else:
                    res = CheckExpr(num_first=num_first, oper_first=oper_first, num_second=num_second)
                    if res:
                        result_list.append(res)
    return result_list

variant_list = GenerateTask()
print(len(variant_list))
print(variant_list[::100])

