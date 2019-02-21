import pandas as pd

clickbait_titles = pd.read_csv('/Users/yeezhianliew/Desktop/Clickbait.csv')
non_clickbait_titles = pd.read_csv('/Users/yeezhianliew/Desktop/NonClickbait.csv')

clickbait_features = pd.read_csv('/Users/yeezhianliew/Desktop/clickbait_website_features.csv')
non_clickbait_features = pd.read_csv('/Users/yeezhianliew/Desktop/non_clickbait_website_features.csv')

clickbait_full = pd.concat([clickbait_titles, clickbait_features], axis=1)               
non_clickbait_full = pd.concat([non_clickbait_titles, non_clickbait_features], axis=1)

clickbait_full['label'] = 1
non_clickbait_full['label'] = 0

fulldata = pd.concat([clickbait_full, non_clickbait_full],sort=True)                    
fulldata = fulldata.sample(frac=1).reset_index(drop=True)
fulldata = fulldata[fulldata.html_len != -1]

fulldata.to_csv('/Users/yeezhianliew/Desktop/fulldata.csv', index=False)


df = pd.read_csv('/Users/yeezhianliew/Desktop/fulldata.csv')


train_df, test_df = train_test_split(df, random_state=42, test_size=0.1)

train_df.to_csv('/Users/yeezhianliew/Desktop/train.csv', index=False, encoding='utf-8')
test_df.to_csv('/Users/yeezhianliew/Desktop/test.csv', index=False, encoding='utf-8')
