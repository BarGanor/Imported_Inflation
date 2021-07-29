import pandas as pd


def get_eurozone_drop_members(df):
    eurozone_states_lst = pd.read_html('eurozone_members.html')[0].State.values.tolist()[:-1]  # Get eurozone members
    df.loc['Euro area '] = df.loc[eurozone_states_lst].sum()  # Define eurozone by sum of member countries
    df = df.drop(eurozone_states_lst)  # Drop Eurozone members
    return df


def get_largest_import_partners(df, top_n_partners):
    result_df = pd.DataFrame()
    for column in df.columns:
        temp = pd.DataFrame({column: df.nlargest(top_n_partners,[column])[column]})
        result_df = pd.concat([result_df, temp], axis=1, sort=True)

    return result_df



