from datetime import  datetime as dt

def convertStrDateToDate(_date):
    if (isinstance(_date, basestring)):
        return dt.strptime(_date, "%Y-%m-%d").date()
    else :
        return _date


def save_df_json(df_data):
    json_str = []
    try:
        json_str = df_data.to_json(orient="records")
    except AttributeError as err:
        print err
    return json_str