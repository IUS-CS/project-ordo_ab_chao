import pandas as pd
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# instance of the neural network to predit future prices
class Neural_Network:
    
    def neural_network(self, n_df):
        df = n_df.copy()
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
        model = keras.Sequential()
        '''
        input_layer = keras.layers.Dense(16, input_dim=num_of_cols, activation='sigmoid')
        model.add(input_layer)
        hidden_layer = keras.layers.Dense(num_of_cols, input_dim=16, activation='sigmoid')
        model.add(hidden_layer)
        output_layer = keras.layers.Dense(1, input_dim=num_of_cols, activation='softmax')
        model.add(output_layer)
        model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
        history = model.fit(X_train, y_train, validation_split=0.2, batch_size=32, epochs=100, shuffle=True)
        '''
        input_layer = keras.layers.Dense(units=16, kernel_initializer='uniform', input_dim=num_of_cols, activation='relu')
        model.add(input_layer)
        hidden_layer1 = keras.layers.Dense(units=18, kernel_initializer='uniform', activation='relu')
        model.add(hidden_layer1)
        model.add(keras.layers.Dropout(rate=0.25))
        hidden_layer2 = keras.layers.Dense(20, kernel_initializer='uniform', activation='relu')
        model.add(hidden_layer2)
        hidden_layer3 = keras.layers.Dense(24, kernel_initializer='uniform', activation='relu')
        model.add(hidden_layer3)
        output_layer = keras.layers.Dense(1, kernel_initializer='uniform', activation='sigmoid')
        model.add(output_layer)
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
        history = model.fit(X_train, y_train, validation_split=0.2, batch_size=15, epochs=10, shuffle=2)
        predictions = model.predict(X_test, verbose=1, steps=1)
        #print('\npredictions shape:\n', predictions.shape)
        #print('\npredictions values:\n', predictions)
        pred_nn_df = pd.DataFrame({'predictions':pd.Series(predictions.reshape(-1)),'actual_sell_prices':pd.Series(y_test)})
        return pred_nn_df, history
    
    
    
    
    
    
    