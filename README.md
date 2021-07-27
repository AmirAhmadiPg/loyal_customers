# Welcome to the loyal_customers wiki!

## this was a project for ict6 challenge

this project will **cluster** 4 classes of customers: **Legendary/Epic/Rare/Common customer**

These clusters are trained on the **ict6 challenge dataset** and you can download it from the repository (trade.csv).

we choose to use **karmozd(or tx)** and the **number of trades** for features to train the model

**normilization:**
    **upper limit = Q3 + 1.5 * IQR**
    **lower limit = Q3 - 1.5 * IQR**
    **every data upper or lower than this threshold value have to remove from dataset**
    **lowerlimit < data < upperlimit**


**hyperparameters for clustering:**
    **number of clusters = 4**
