import pandas as pd
from sys import argv
import re
import subprocess
parser_path,excel_name=argv
model_path=parser_path.replace("parser.py","model.py")
author_model="--author--"
description_model="--factor_description--"
params_description_model="--params_description--"
factor_model="--factor--"
default_params ="--params--"
formula_model="--formula--"
format_model="--format--"
author=input("please input your name")
compiler=re.compile("([0-9]+)")
with open(model_path,encoding="utf-8") as f:
	df=pd.read_excel(excel_name)
	content=f.read()
	factors=df.index
	formulas=df["Formula"]
	params=df["parameter"].values
	descriptions=df["description"].values
	formulas=formulas.map(lambda x:x.replace("{}","%s")).values
	for factor,formula,description,param in zip(factors,formulas,descriptions,params):
		temp=content.replace(author_model,"'"+author+"'")
		temp=temp.replace(factor_model,factor)
		temp=temp.replace(description_model,description)
		temp=temp.replace(formula_model,formula)
		temp=temp.replace("value",factor)
		parameters=dict()
		params_description=dict()
		param=compiler.findall(param)
		format_content=[]
		for i in range(1,len(param)+1):
			parameters['t%d'%i]=int(param[i-1])
			format_content.append("params['t%d']"%i)
			params_description['t%d'%i]="暂无"
		temp=temp.replace(params_description_model,str(params_description))
		format_content=",".join(format_content)
		temp=temp.replace(format_model,format_content)
		temp=temp.replace(default_params,str(parameters))
		with open(factor+".py","w",encoding="utf-8") as g:
			g.write(temp)
		try:
			ret=subprocess.call('dyfactor parse %s.py' %factor ,shell=True)
		except:
			print("检测到没有装大鱼的helper的库！！！%s无法检验，但不影响.py生成"%factor)