import pandas as pd

def question_one(path):
    df = pd.read_csv(path)
    school_grouped = df.groupby('學校名稱')[['男生計', '女生計']].sum()

    school_grouped['男生比例(%)'] = (school_grouped['男生計'] / (school_grouped['男生計'] + school_grouped['女生計'])) * 100
    school_grouped['女生比例(%)'] = (school_grouped['女生計'] / (school_grouped['男生計'] + school_grouped['女生計'])) * 100
    for index, row in school_grouped.iterrows():
        print(f"{index}:")
        print(f"男生比例 {row['男生比例(%)']:.2f}%")
        print(f"女生比例 {row['女生比例(%)']:.2f}%")
        print("*"*20)
        
def question_two(path):
    df = pd.read_csv(path)
    gender_grouped = df.groupby('等級別')[['男生計', '女生計']].sum()
    gender_grouped['男生比例(%)'] = (gender_grouped['男生計'] / (gender_grouped['男生計'] + gender_grouped['女生計'])) * 100
    gender_grouped['女生比例(%)'] = (gender_grouped['女生計'] / (gender_grouped['男生計'] + gender_grouped['女生計'])) * 100
    for index, row in gender_grouped.iterrows():
        print(f"{index}:")
        print(f"男生比例 {row['男生比例(%)']:.2f}%")
        print(f"女生比例 {row['女生比例(%)']:.2f}%")
        print("*"*20)

def question_three(path):
    df = pd.read_csv(path)

    doctoral_students = df[df['等級別'] == 'D 博士'].groupby('學校名稱')['總計'].sum()
    masters_students = df[df['等級別'] == 'M 碩士'].groupby('學校名稱')['總計'].sum()
    total_people = df.groupby('學校名稱')['總計'].sum()

    doctoral_proportion = (doctoral_students / total_people).fillna(0)
    masters_proportion = (masters_students / total_people).fillna(0)

    proportions_df = pd.DataFrame({
        '博士生比例': doctoral_proportion,
        '碩士生比例': masters_proportion
    }).fillna(0)
    
    # change format(add %)
    proportions_df_formatted = proportions_df.applymap(lambda x: f"{round(x * 100, 2)}%")

    print(proportions_df_formatted)
   
def question_four(path):
    df = pd.read_csv(path)
    """1.哪間大專院校有最多的學士生
        step1: 取出想要查看的欄位，並印出此資料集共有多少筆紀錄 (len)

        step2: 篩選等級別為"B 學士"的DataFrame，並印出有招生學士學制的學校數量

        step3: 依據"總計"從大到小排序並印出結果 (sort_values, by, ascending)
    """

    df1 = df[['等級別']] # 取出想要觀看的欄位
    print("本資料集共有", df1, "筆紀錄")

    df1_1 = df[df1['等級別'] == 'B 學士']
    print("有招生學士學制的學校數量為", len(df1_1))

    df1_1_sorted = df1_1.sort_values(by='總計', ascending=False)
    print("112學年度在籍的學士生最多人數之學校為", df1_1_sorted.head(1)['學校名稱'].values)
    
def question_five(path):
    df = pd.read_csv(path)
    """2. 國立？所；私立？所
        step1: 建立空字串 (lsit=[])

        step2: 建立for迴圈，配合if else條件，取出國立與私立

        step3: 新增「公私立」column在DataFrame中 (df['公私立'])

        step4: 篩選掉重複的學校代碼資料 (drop_duplicates)

        step5: 計算公立與私立學校的筆數，並印出結果 (value_counts)
    """
    type_list = [] # 建立空字串

    for i in df['學校名稱']:
        if ('國立' in i) or ('市立' in i):
            type_list.append('國立')
        else:
            type_list.append('私立')

    df['公私立'] = type_list # 將 Dataframe 新增「公私立」column

    df2 = df.drop_duplicates(subset=['學校代碼']) # 篩選掉重複的學校代碼資料
    count = df2['公私立'].value_counts() # 計算公立與私立學校的筆數，並印出結果

    # print(df2)
    print(f"本資料集共收集了 {count.sum()} 所學校，其中公立：{count.get('國立', 0)} 所；私立：{count.get('私立', 0)} 所。")
    
def question_six(path):
    """3. 各等級別學制共有？所
        step1: 篩選掉重複的學校名稱與等級別 (drop_duplicates, subset)

        step2: 計算出等級別的筆數 (value_counts)

        step3: 建立等級別的字串，並找出其類別 (unique)

        step4: 使用for迴圈，依序列出所有等級別學制的學校數量 (count)
    """
    df = pd.read_csv(path)
    
    df3 = df.drop_duplicates(subset=['學校名稱', '等級別']) 
    count = df3['等級別'].value_counts() 
    degree_list = list(df['等級別'].unique()) 

    print(f"本資料集總共收集了 {len(set(df['學校名稱']))} 所學校，各等級學制當中：")
    for degree in degree_list:
        print(f"一共有{count[degree]} 所學校，有招收{degree}。")




if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    csv_path = 'week2/112_student.csv'

    # 請註解function來呼叫對應的問題
    # print("第一題:各大學的男女分佈？\n")
    # question_one(csv_path)
    # print("第二題:各等級別的性別分佈？\n")
    # question_two(csv_path)
    # print("第三題:各大學的博士、碩士生比例？\n")
    # question_three(csv_path)
    # print("第四題(老師):")
    # question_four(csv_path)
    # print("第五題(老師):")
    # question_five(csv_path)
    print("第六題(老師):")
    question_six(csv_path)