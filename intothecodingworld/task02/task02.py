import pandas as pd

df = pd.read_csv('C:/Users/happyhill24/Desktop/work/intothecodingworld/task02/data.csv', header=None)
df

#0열과 1열 합치기
df['combined']=df.apply(lambda x: '%s#%s' % (x[0],x[1]),axis=1)
df['combined']

df=df[['combined',2]]
df

#index를 칼럼으로 살려두기
company_team=df.combined
company_team=company_team.reset_index()
company_team

#개행 별로 쪼개기
split_df=df[2].str.split('\n')
split_df

split_df=split_df.apply(lambda x:pd.Series(x))
split_df

#칼럼을 행으로 바꾸기
split_df.stack()

split_df=split_df.stack().reset_index(level=1,drop=True)
split_df

#index를 칼럼으로 살려두기
split_df=split_df.reset_index()
split_df

#merge
merge=pd.merge(company_team,split_df)
merge

merge.drop(['index'],axis=1,inplace=True)
merge

# 칼럼 이름 변경
merge.columns=['combined','name']
merge

#추출~!
merge.to_excel('merge.xlsx')