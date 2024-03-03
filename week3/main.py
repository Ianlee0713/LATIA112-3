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
   

if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    csv_path = 'week2/112_student.csv'

    # 請註解function來呼叫對應的問題
    print("第一題:各大學的男女分佈？\n")
    question_one(csv_path)
    print("第二題:各等級別的性別分佈？\n")
    question_two(csv_path)
    print("第三題:各大學的博士、碩士生比例？\n")
    question_three(csv_path)