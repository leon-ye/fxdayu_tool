# encoding: utf-8 
# 文件需要以utf-8格式编码
# 文件名代表因子名称，需满足命名规范
__author__ = --author-- # 这里填下你的名字
default_params = --params-- # 这里填写因子参数默认值，比如: {"t1": 10}
params_description = --params_description-- # 这里填写因子参数描述信息，比如: {"t1": "并没有用上的参数"}

def run_formula(dv, params=default_params):
    """
    --factor_description--
    """
    value = dv.add_formula('--factor--', "--formula--"%(--format--),
        is_quarterly=False, add_data=True)
    return value
