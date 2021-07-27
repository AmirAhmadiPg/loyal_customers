import pandas as pd


def load_csv_data(cvs_path):
    ''' load_csv_data:
        this function will return a dataframe of csv file
        
        returns: df
    '''
    df = pd.read_csv(cvs_path)
    return df


def outlier_data_remover(df):
    '''outlier_data_remover:
        this function will remove the outlier data with formula:
        IQR(Q1, Q3) = Q3 - Q1
        uppder_limit = Q3 + 1.5 * IQR
        lower_limit = Q1 - 1.5 * IQR

        if data x is lower or upper than limits it will delete from data frame
        
        returns: df
    '''
    Q1= df['karmozd'].quantile(0.25)
    Q3 = df['karmozd'].quantile(0.75)
    IQR = Q3 - Q1
    upper_limit = Q3 + 1.5 * IQR
    lower_limit = Q1 - 1.5 * IQR
    df = df[(df['karmozd'] < lower_limit) | (df['karmozd'] > upper_limit)]
    return df


def data_train_gen(df, mean_of_tx = True, sum_of_tx = False):
    '''data_train_gen:
        this function will create data for traning the k-means algorithm
        
        this function have 2 metrics: both have count of buys, metric 1- mean of tx,
        metric 2 sum of tx 

        returns: df'''
    
    userid = []
    buyCount = []
    kharid = []

    for i in df['userid']:
        if i not in userid:
            buyCount.append(len(df.loc[df['userid'] == i]))
            if mean_of_tx:
                kharid.append(df.loc[df['userid'] == i].values[:, -1].mean())
            else:
                kharid.append(df.loc[df['userid'] == i].values[:, -1].sum())
            userid.append(i)

    data = {'x': kharid, 'y': buyCount}
    df = pd.DataFrame(data, columns=['x', 'y'])

    return df, userid