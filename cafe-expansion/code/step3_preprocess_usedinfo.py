import numpy as np
import pandas as pd
import seaborn as sns
import os, sys

# cafe-expansion 경로
PRJCT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PRJCT_PATH, 'data')
RSLT_DIR = DATA_DIR

sys.path.append(PRJCT_PATH)
from module_aladin.util import train_test_split_strat
from module_aladin.file_io import save_pkl
from sklearn.model_selection import train_test_split

quality_dict= {
    '최상':4,
    '상':3,
    '중':2,
    '균일가':1,
    '하':1
}

if __name__=='__main__':
    # 파일명 및 경로 수정
    base_file = 'bestseller_cleaned_240718'
    file_name = f'usedproduct_{base_file}_concatted.csv'
    file_path = os.path.join(DATA_DIR, file_name)
    usedinfo = pd.read_csv(file_path)
    usedinfo['quality'] = usedinfo['quality'].map(quality_dict)
    assert len(usedinfo['delivery_fee'].unique()) == 1
    usedbook_data = usedinfo [['ItemId','quality','store','price']]

    file_name = 'usedinfo_ver0.csv'
    save_path = os.path.join(DATA_DIR, file_name)
    usedinfo.to_csv(save_path, index=False)
    
    y_col = 'price'
    x_cols = list(filter(lambda x : x != y_col,list(usedinfo.columns)))
    X, y = usedinfo[x_cols], usedinfo[y_col]
    
    strat = False 
    if strat :
        #split strat by ItemId
        X_dev,X_test,y_dev,y_test = train_test_split_strat(X,y,strat=X['ItemId'],test_size=0.2,random_state=329)
        X_train,X_val,y_train,y_val = train_test_split_strat(X_dev,y_dev,strat=X_dev['ItemId'],test_size=0.2,random_state=329)
    else : 
        #not stratified
        X_dev,X_test,y_dev,y_test = train_test_split(X,y,test_size=0.2,random_state=801)
        X_train,X_val,y_train,y_val = train_test_split(X_dev,y_dev,test_size=0.2,random_state=801)

    data_dict= {
        'train':{'X': X_train, 'y': y_train},
        'val':{'X': X_val, 'y': y_val},
        'test':{'X': X_test, 'y': y_test},
    }
    ver = 1.0
    file_name = f'data_splitted_ver{ver}_strat-{strat}.pkl'
    save_pkl(RSLT_DIR, file_name, data_dict)
