import pandas as pd



def initial_cleanup(df):

    """performs initial data frame column cleaning
        - user.data because its deprecated
    """

    # combine screen size into a single column
    df["screen_size"] = df.apply(lambda x: (x.screen_width, x.screen_height), axis=1)
    
    # drop columns
    df.drop(columns=['screen_width', 'screen_height'], inplace=True)
    
    
    return df