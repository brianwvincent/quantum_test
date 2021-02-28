import pandas as pd
from sklearn.preprocessing import OneHotEncoder



def perform_one_hot_encoding(df, column_name):
    
    encoder = OneHotEncoder()
    results = encoder.fit_transform(df[[column_name]].compute())
    encoded_df = pd.DataFrame(results.toarray(), columns=encoder.categories_)
    
    return df.join(encoded_df)

def perform_many_hot_hot_encodings(df, column_names):

    temp_df = df

    for column_name in column_names:

        temp_df = perform_one_hot_encoding(temp_df, column_name)

    return temp_df