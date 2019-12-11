import pandas as pd

# instance of 'out of sample'/step forward analysis model to predit future prices
class Oos:
 
    def out_of_sample(self, c_df):
        df = c_df.copy()
        df['endPrice'] = df['endPrice'].astype(float)
        pivot_df = df.pivot_table(index='endDate', columns='listingType', values='endPrice')
        pivot_df = pivot_df.interpolate(method='linear', axis=0).ffill().bfill()
        #print('\npivot_df:\n', pivot_df)
        delta_values = [7,14,21,28]
        delta_dict = {}
        for offset in delta_values:
            delta_dict['delta_{}'.format(offset)] = pivot_df/pivot_df.shift(offset) - 1.0
        #print('delta_7 \'date\' check for null dates:', delta_dict['delta_7'].index.isnull().sum())
        #print('delta_14 \'date\' check for null dates:', delta_dict['delta_14'].index.isnull().sum())
        #print('delta_21 \'date\' check for null dates:', delta_dict['delta_21'].index.isnull().sum())
        #print('delta_28 \'date\' check for null dates:', delta_dict['delta_28'].index.isnull().sum())
        melted_dfs = []
        for key, delta_df in delta_dict.items():
            melted_dfs.append(delta_df.reset_index().melt(id_vars=['endDate'], value_name=key))
        '''
        for i in melted_dfs:
            print(i,'melted_dfs:\n', i.tail())
        '''
        target_variable = pd.merge(melted_dfs[0], melted_dfs[1], on=['endDate','listingType'])
        target_variable = pd.merge(target_variable, melted_dfs[2], on=['endDate','listingType'])
        target_variable = pd.merge(target_variable, melted_dfs[3], on=['endDate', 'listingType'])
        #print('\ntarget_variable:\n', target_variable)
        return target_variable