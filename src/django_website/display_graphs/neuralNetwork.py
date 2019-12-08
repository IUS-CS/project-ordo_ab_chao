import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

class Neural_Network:
    
    def neural_network(self, n_df):
        df = n_df.copy()
        df = df.replace('^\s*$', np.nan, regex=True)
        #df['itemId'] = df['itemId'].astype(int)
        df['listingType'] = pd.get_dummies(df['listingType'])
        df['endPrice'] = df['endPrice'].astype(float)
        df['shippingServiceCost'] = df['shippingServiceCost'].astype(float)
        df['shippingServiceCost'] = df['shippingServiceCost'].interpolate()
        df['bidCount'] = df['bidCount'].astype(np.float)
        df['bidCount'] = df['bidCount'].interpolate()
        df['watchCount'] = df['watchCount'].astype(np.float)
        df['watchCount'] = df['watchCount'].interpolate()
        df['returnsAccepted'] = pd.get_dummies(df['returnsAccepted'])
        df['handlingTime'] = df['handlingTime'].astype(int)
        df['sellerUserName'] = pd.get_dummies(df['sellerUserName'])
        df['feedbackScore'] = df['feedbackScore'].astype(int)
        df['positiveFeedbackPercent'] = df['positiveFeedbackPercent'].astype(float)
        df['topRatedSeller'] = pd.get_dummies(df['topRatedSeller'])
        df['endDate'] = pd.get_dummies(df['endDate'])
        print('\nnull values in dataframe are:\n', df.columns.isnull())
        features_df = df.drop(['itemId','title','endPrice','location','endTime','startTime','endTimeOfDay'], axis=1)
        num_of_cols = len(features_df.columns)
        features = features_df.values
        target = df.endPrice.values
        print('\ntarget values:\n', target)
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=124)
        X_train = MinMaxScaler(feature_range=(-1,1)).fit_transform(X_train)
        X_test = MinMaxScaler(feature_range=(-1,1)).fit_transform(X_test)
        model = keras.Sequential()
        input_layer = keras.layers.Dense(16, input_dim=num_of_cols, activation='relu')
        model.add(input_layer)
        hidden_layer = keras.layers.Dense(num_of_cols, input_dim=16, activation='relu')
        model.add(hidden_layer)
        output_layer = keras.layers.Dense(1, input_dim=num_of_cols, activation='softmax')
        model.add(output_layer)
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        history = model.fit(X_train, y_train, validation_split=0.2, batch_size=32, epochs=100, shuffle=True)
        predictions = model.predict(X_test, verbose=0, steps=1)
        pred_nn_df = pd.DataFrame({'predictions':pd.Series(np.round(predictions.reshape(-1),2)),'actual_sell_prices':pd.Series(y_test)})
        return pred_nn_df, history
    
    
    
    
    
    
    