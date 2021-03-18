<B>◆、LinearRegression(線性迴歸)</B>：  
波士頓房價預測,讀取sklearn.datasets中Boston的資料集(504筆資料，14個屬性).
計算MAE,MSE,RMSE及房價預測 
MAE: 3.7507  
MSE: 23.3808  
RMSE: 4.83537  
房價預測：[30.06627665]    

PS.
平均絕對誤差(mean absolute error,MAE)  
均方誤差(mean squared error,MSE)  
均方根誤差(root-mean-square error,RMSE)並進行房價預測。


<B>◆、Logistic Regression(邏輯迴歸)</B>：  
鐵達尼號生存預測年齡、性別及準確度.  

截距= [1.99663426]  
迴歸係數= [[-1.1832979   2.3834008  -0.03499218]]  
Confusion Matrix 準確度： 0.8149276 



<B>◆、DBSCAN(群聚演算法)</B>：  
手寫數字資料集讀取sklearn.datasets的(1797筆，每筆資料大小8x8 共64個數值徵欄位)，
針對數值欄位標準、建立k-means模型進行分群、計算輪廓係數及準確率.

K-Mean (k-means++):Silhouette=0.1455  
K-Means (random):Silhouette=0.1448   
K-Means (PCA-based):Silhouette=0.1388  
Accuracy (分類準確率)=0.1085  


 