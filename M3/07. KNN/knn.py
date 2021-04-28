import numpy as np
import pandas as pd


class KNN():
    
    def __init__(self, k=3):
        self.k = k
          
    def evaluate(self, y_hat, y_true):
        
        return np.count_nonzero( (y_hat - y_true) == 0) / y_true.shape[0]
    
    
    def euclidian_dist(self,  v1, v2 ):
        
        return np.linalg.norm(v1-v2)
    
    def predict(self, x_train, x_test, y_train ):
        
        y_p = []
        
        for i in range(x_test.shape[0]):
            
            dist_list = []
            
            for j in range(x_train.shape[0]):

                eucl_dist = self.euclidian_dist(x_test[i], x_train[j])
                dist_list.append(  ( eucl_dist, y_train[j]  )   )
               
            dist_list = pd.DataFrame( dist_list, columns= ['dist', 'y_true'] )
            dist_list = dist_list.sort_values(by = 'dist' )
            y_p.append( dist_list['y_true'][:self.k].mode()[0])
        return np.array(y_p)
    
a = KNN(3)