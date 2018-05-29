def Multi_Regression(index,n,Y,*X):
    """
    index是指返回的系数矩阵中第几个，从0开始，0代表常数项，1代表第一个系数的值
    n是rolling多少天
    Y是因变量矩阵
    *X传入自变量，无论多少个，往后填充就行
    """
    from numpy.linalg import inv,LinAlgError
    import numpy as np
    DF=dict()
    le_th=len(Y)
    columns=Y.columns
    indexes=Y.index
    for column in columns:
        betas=[]
        X_column=list(map(lambda x:x[column].values,X))
        X_column.insert(0,np.ones(le_th))
        X_column=np.array(X_column).T
        Y_column=np.array(Y[column].values).T
        print(column)
        for length in range(n,le_th):
            X_temp=X_column[length-n:length]
            try:
                beta=(inv((X_temp.T).dot(X_temp))).dot(X_temp.T).dot(Y_column[length-n:length])
                betas.append(beta[index])
            except LinAlgError:
                betas.append(np.nan)
        DF[column]=betas
    for key,value in DF.items():
        if len(value)!=le_th-n:
            DF[key]+=[np.nan]*(le_th-n-len(DF[key]))
        if len(value)!=le_th:
            DF[key]=[np.nan]*n+DF[key]
    df=pd.DataFrame(DF,index=indexes)
    return df
if __name__=="main":
    dv.add_formula("test","MultipleRegression(1,3,Return(close_adj),close_adj,open_adj)",register_funcs={"MultipleRegression":Multi_Regression},add_data=True,is_quarterly=False)
        
