# https://github.com/olusegunajibola/onehot-encoder/blob/main/onehot_encoder.py
import pandas as pd
def onehot_encoding(col, df ):
    """
    This function performs one hot encoding on a column in a dataframe and returns an updated dataframe.

    inputs :
        col = a list of columns names
        df = desired dataframe
    return :
        updated dataframe
    """

    for i in col: # pick desired column(s) to hot encode

        dummy_var = pd.get_dummies(df[i]) # make it into dummies

        rename_cols_dict = {} # empty dictionary to store the elements in the column and the dummy column name

        for cols in dummy_var.columns:
            # for each column name in the dummy variable, attach the original column name to it with an underscore
            rename_cols_dict[cols] = i + '_' + str(cols)

        dummy_var = dummy_var.rename( columns = rename_cols_dict) # rename dummy variable columns with dictionary created

        new_df = pd.concat( [df, dummy_var  ], axis = 1 )  # combine the dummy variable and the dataframe side by side

        new_df = new_df.drop(i, axis = 1) # remove original df from the dataset

        df = new_df # update dateframe

    return new_df