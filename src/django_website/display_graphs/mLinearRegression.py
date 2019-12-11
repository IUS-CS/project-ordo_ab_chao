import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression

# instance of Regression model for future price predictions
class MultivariateLinearRegression:
    
    def regression(self, r_df):
        df = r_df.copy()
        df = df.replace('^\s*$', np.nan, regex=True)
        #df['itemId'] = df['itemId'].astype(int)
        df['listingType'] = pd.get_dummies(df['listingType'])
        df['endPrice'] = df['endPrice'].astype(np.float)
        df['shippingServiceCost'] = df['shippingServiceCost'].astype(np.float)
        #df['shippingServiceCost'] = df['shippingServiceCost'].interpolate()
        df['shippingServiceCost'] = df['shippingServiceCost'].fillna(df['shippingServiceCost'].mean())
        df['bidCount'] = df['bidCount'].astype(np.float)
        #df['bidCount'] = df['bidCount'].interpolate()
        df['bidCount'] = df['bidCount'].fillna(df['bidCount'].mean())
        df['watchCount'] = df['watchCount'].astype(np.float)
        #df['watchCount'] = df['watchCount'].interpolate()
        df['watchCount'] = df['watchCount'].fillna(df['watchCount'].mean())
        df['returnsAccepted'] = pd.get_dummies(df['returnsAccepted'])
        df['handlingTime'] = df['handlingTime'].astype(np.float)
        df['sellerUserName'] = pd.get_dummies(df['sellerUserName'])
        df['feedbackScore'] = df['feedbackScore'].astype(np.float)
        df['positiveFeedbackPercent'] = df['positiveFeedbackPercent'].astype(np.float)
        df['topRatedSeller'] = pd.get_dummies(df['topRatedSeller'])
        df['endDate'] = pd.get_dummies(df['endDate'])
        #print('\nnull values in dataframe are:\n', df.isnull().any())
        features_df = df.drop(['itemId','title','endPrice','location','endTime','startTime','endTimeOfDay'], axis=1)
        corr = features_df.corr()
        #print('\ncorr:\n', corr)
        num_of_cols = len(features_df.columns)
        #print('\nnumber of feature columns:\n', num_of_cols)
        features = features_df.values
        target = df.endPrice.values
        #print('\ntarget values:\n', target)
        #print('\nfeatures values:\n', features)
        #print('\ntarget shape:\n', target.shape)
        #print('\nfeatures shape:\n', features.shape)
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=124)
        #print('\nTRAIN TEST SPLIT EXECUTED\n')
        X_train = MinMaxScaler(feature_range=(-1,1)).fit_transform(X_train)
        X_test = MinMaxScaler(feature_range=(-1,1)).fit_transform(X_test)
        #print('\nX_train and X_test scaled\n')
        y_train = y_train.reshape(-1,1)
        y_test = y_test.reshape(-1,1)
        y_train = MinMaxScaler(feature_range=(-1,1)).fit_transform(y_train)
        y_test = MinMaxScaler(feature_range=(-1,1)).fit_transform(y_test)
        y_train = y_train.reshape(-1)
        y_test = y_test.reshape(-1)
        #print('\nshape of X_train:\n', X_train.shape)
        #print('\nshape of X_test:\n', X_test.shape)
        #print('\nshape of y_train:\n', y_train.shape)
        #print('\nshape of y_test:\n', y_test.shape)
        model = LinearRegression()
        model = model.fit(X_train, y_train)
        yhat = model.predict(X_test)
        #y_test = y_test.reset_index(drop=True)
        pred_df = pd.DataFrame({'predictions': pd.Series(yhat), 'actual_sell_prices': pd.Series(y_test)})
        return pred_df
        
        
        