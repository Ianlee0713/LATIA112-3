import pandas as pd
import matplotlib.pyplot as plt


def question_one(path):
    print(f"\n問題一:各科系的學生人數？")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 計算每個科系的學生人數
    department_counts = df['Department'].value_counts()
    # 打印每個科系的學生人數
    print(department_counts)

    # 繪製條形圖來展示每個科系的學生人數分布
    plt.figure(figsize=(10, 6))
    bars = department_counts.plot(kind='bar')
    plt.title('Question 1: 學生人數按科系分布')
    plt.xlabel('Department')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # 在條形圖上加上數字
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, bar.get_height(), 
                 ha='center', va='bottom')
        
    # 將圖表保存為檔案
    plot_path_q1 = 'answer_pic/question1.png'
    plt.savefig(plot_path_q1)
    plt.show()

def question_two(path):
    print(f"\n問題二:請計算男女學生的平均身高(四捨五入到小數點第一位數)")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 按性別分組，計算每組的平均身高
    average_height_by_gender = df.groupby('Gender')['Height(CM)'].mean()
    # 打印四捨五入後的平均身高
    print(average_height_by_gender.round(1))
    
    # 繪製條形圖展示男女學生的平均身高
    plt.figure(figsize=(6, 4))
    bars = average_height_by_gender.plot(kind='bar', color=['blue', 'pink'])
    plt.title('Question2:請計算男女學生的平均身高(四捨五入到小數點第一位數)')
    plt.xlabel('Gender')
    plt.ylabel('Average Height (CM)')
    plt.xticks(rotation=0)
    plt.tight_layout()

    # 在條形圖上加上數字
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{bar.get_height()} CM', 
                 ha='center', va='bottom')
        
    # 將圖表保存為檔案
    plot_path_q2 = 'answer_pic/question2.png'
    plt.savefig(plot_path_q2)
    plt.show()

def question_three(path):
    print(f"\n問題三:參與認證課程和未參與認證課程學生的平均大學成績(四捨五入到小數點第二位數)")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 按是否參與認證課程分組，計算每組的平均大學成績
    average_grade_by_certification = df.groupby('Certification Course')['college mark'].mean()
    # 打印四捨五入後的平均成績
    print(average_grade_by_certification.round(2))
    
    # 繪製條形圖展示參與認證課程和未參與認證課程學生的平均大學成績
    plt.figure(figsize=(8, 4))
    bars = average_grade_by_certification.plot(kind='bar', color=['green', 'orange'])
    plt.title('Question3:參與認證課程和未參與認證課程學生的平均大學成績(四捨五入到小數點第二位數)')
    plt.xlabel('Certification Course Participation')
    plt.ylabel('Average College Mark')
    plt.xticks(rotation=0)
    plt.tight_layout()

    # 在條形圖上加上數字
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{bar.get_height()}', 
                 ha='center', va='bottom')

    # 將圖表保存為檔案
    plot_path_q3 = 'question3.png'
    plt.savefig(plot_path_q3)
    plt.show()

def question_four(path):
    print(f"\n問題四:每個科系中，喜歡自己學位的學生比例（百分比，四捨五入至小數點後一位）")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 篩選出喜歡自己學位的學生，按科系分組，並計算每個科系的學生數量
    like_degree = df[df['Do you like your degree?'] == 'Yes'].groupby('Department').size()
    # 按科系分組，計算每個科系的總學生數量
    total_students_per_department = df.groupby('Department').size()
    # 計算每個科系中喜歡自己學位的學生比例
    percentage_like_degree = (like_degree / total_students_per_department * 100).round(1)
    # 將比例轉換為百分比格式
    answer = percentage_like_degree.astype(str) + '%'
    # 打印每個科系中喜歡自己學位的學生比例
    print(answer)
    
    # 繪製條形圖展示每個科系中喜歡自己學位的學生比例
    plt.figure(figsize=(10, 6))
    bars = percentage_like_degree.plot(kind='bar', color='purple')
    plt.title('Question4:每個科系中，喜歡自己學位的學生比例（百分比，四捨五入至小數點後一位）')
    plt.xlabel('Department')
    plt.ylabel('Percentage (%)')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # 在條形圖上加上百分比標籤
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{bar.get_height()}%', 
                 ha='center', va='bottom')
        
    # 將圖表保存為檔案
    plot_path_q4 = 'answer_pic/question4.png'
    plt.savefig(plot_path_q4)
    plt.show()

def question_five(path):
    print(f"\n問題五:每日使用社交媒體和影片時間的學生成績平均")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 定義社交媒體和影片使用時間的排序
    accurate_usage_order = {
        '0 Minute': 0,
        '1 - 30 Minute': 1,
        '30 - 60 Minute': 2,
        '1 - 1.30 hour': 3,
        '1.30 - 2 hour': 4,
        'More than 2 hour': 5
    }
    # 映射使用時間到一個可排序的數值
    df['accurate_social_media_video_usage_order'] = df['social medai & video'].map(accurate_usage_order)
    # 按照映射後的使用時間分組，計算每組的平均大學成績
    average_mark_by_social_media_usage = df.groupby('accurate_social_media_video_usage_order')['college mark'].mean().round(1)
    # 將索引映射回原始的使用時間類別
    average_mark_by_social_media_usage.index = average_mark_by_social_media_usage.index.map({v: k for k, v in accurate_usage_order.items()})
    # 打印每日使用社交媒體和影片時間的學生成績平均
    print(average_mark_by_social_media_usage)
    
    # 繪製條形圖展示每日使用社交媒體和影片時間的學生成績平均
    plt.figure(figsize=(10, 6))
    bars = average_mark_by_social_media_usage.plot(kind='bar', color='cyan')
    plt.title('Question5:每日使用社交媒體和影片時間的學生成績平均')
    plt.xlabel('Daily Social Media and Video Usage')
    plt.ylabel('Average College Mark')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # 在條形圖上加上成績標籤
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{bar.get_height()}', 
                 ha='center', va='bottom')

    # 將圖表保存為檔案
    plot_path_q5 = 'answer_pic/question5.png'
    plt.savefig(plot_path_q5)
    plt.show()
        
def question_six(path):
    print(f"\n問題六:每種「財務狀況」分類下，學生對自己學位喜好（Do you like your degree?）的比例")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 按財務狀況和學位喜好分組，計算每組的學生數量
    degree_like_by_financial_status = df.groupby(['Financial Status', 'Do you like your degree?']).size()

    # 計算每個「財務狀況」分類下的學生總數
    total_students_by_financial_status = df.groupby('Financial Status').size()

    # 計算喜歡自己學位的學生比例
    percentage_like_degree_by_financial_status = (degree_like_by_financial_status / total_students_by_financial_status * 100).unstack().round(1)
    sorted_percentage_like_degree = percentage_like_degree_by_financial_status['Yes'].sort_values(ascending=False)

    # 格式化輸出結果
    formatted_output = ""
    for status in sorted_percentage_like_degree.index:
        yes_percentage = sorted_percentage_like_degree[status]
        no_percentage = 100 - yes_percentage if status in percentage_like_degree_by_financial_status.index and 'No' in percentage_like_degree_by_financial_status.columns else None
        formatted_output += f"{status}\n"
        if not pd.isna(no_percentage):
            formatted_output += f"不喜歡：{no_percentage}%\n"
        formatted_output += f"喜歡：{yes_percentage}%"
        if pd.isna(no_percentage):
            formatted_output += " (沒有學生選擇「不喜歡」)"
        formatted_output += "\n\n"

    # 打印格式化後的輸出結果
    print(formatted_output.strip())
    
    # 將學生的學位喜好轉換為布爾值，計算每種「財務狀況」下的喜好比例
    df['like_degree'] = df['Do you like your degree?'] == 'Yes'
    like_degree_by_financial_status = df.groupby(['Financial Status', 'like_degree']).size().unstack().fillna(0)
    like_degree_percentages = (like_degree_by_financial_status.div(like_degree_by_financial_status.sum(axis=1), axis=0) * 100).round(1)

    # 繪製堆疊條形圖展示結果
    _, ax = plt.subplots(figsize=(10, 6))
    bars = like_degree_percentages.plot(kind='bar', stacked=True, color=['red', 'lightgreen'], ax=ax)
    ax.set_title('Question6:每種「財務狀況」分類下，學生對自己學位喜好（Do you like your degree?）的比例')
    ax.set_xlabel('Financial Status')
    ax.set_ylabel('Percentage')
    ax.tick_params(axis='x', rotation=45)
    ax.legend(['No', 'Yes'], title='Do you like your degree?')
    
    plt.tight_layout()
    
    # 在條形圖上加上百分比標籤
    for rect in bars.patches:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., height + 1, f'{height}%', ha='center', va='bottom')

    # 將圖表保存為檔案
    plot_path_q6 = 'answer_pic/question6.png'
    plt.savefig(plot_path_q6)
    plt.show()

def question_seven(path):
    print(f"\n問題七:每個科系學生的平均薪資期望值")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 按科系分組，計算每個科系學生的平均薪資期望值
    average_salary_expectation_by_department = df.groupby('Department')['salary expectation'].mean().round(2)
    # 打印每個科系學生的平均薪資期望值
    print(average_salary_expectation_by_department)
    
    # 繪製條形圖展示每個科系學生的平均薪資期望值
    plt.figure(figsize=(10, 6))
    average_salary_expectation_by_department.plot(kind='bar', color='skyblue')
    plt.title('Question7:每個科系學生的平均薪資期望值')
    plt.xlabel('Department')
    plt.ylabel('Average Salary Expectation')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    # 在條形圖上加上數字
    for i, value in enumerate(average_salary_expectation_by_department):
        plt.text(i, value + 0.05, round(value, 2), ha='center')
    
    # 將圖表保存為檔案
    plot_path_q7 = 'answer_pic/question7.png'
    plt.savefig(plot_path_q7)
    plt.show()

def question_eight(path):
    print(f"\n問題八:統計有多少學生參與了認證課程，並按科系分類")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 計算參與了認證課程的學生數，並按科系分類
    students_with_certification_by_department = df[df['Certification Course'] == 'Yes'].groupby('Department').size()
    # 打印參與了認證課程的學生數，按科系分類
    print(students_with_certification_by_department)

    # 繪製條形圖展示參與了認證課程的學生數，按科系分類
    plt.figure(figsize=(10, 6))
    bars = students_with_certification_by_department.plot(kind='bar', color='lightgreen')
    plt.title('Question8:統計有多少學生參與了認證課程，並按科系分類')
    plt.xlabel('Department')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    # 在條形圖上加上數字
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, bar.get_height(), ha='center', va='bottom')
    
    # 將圖表保存為檔案
    plot_path_q8 = 'answer_pic/question8.png'
    plt.savefig(plot_path_q8)
    plt.show()

def question_nine(path):
    print(f"\n問題九:不同的通勤時間學生的成績平均")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 定義通勤時間的排序規則，以便正確排序並分析
    travelling_time_sort_order = {
        '0 - 30 minutes': 1,
        '30 - 60 minutes': 2,
        '1 - 1.30 hour': 3,
        '1.30 - 2 hour': 4,
        '2 - 2.30 hour': 5,
        '2.30 - 3 hour': 6,
        'more than 3 hour': 7
    }

    # 將通勤時間映射到排序規則，以便進行排序
    df['Travelling Time Sort Order'] = df['Travelling Time '].map(travelling_time_sort_order)

    # 根據排序後的通勤時間分組，計算每組的平均大學成績
    average_college_mark_sorted_by_travelling_time = df.groupby('Travelling Time Sort Order')['college mark'].mean().round(2)
    # 將排序後的索引映射回原始的通勤時間標籤，以便閱讀
    average_college_mark_sorted_by_travelling_time.index = average_college_mark_sorted_by_travelling_time.index.map({v: k for k, v in travelling_time_sort_order.items()})

    # 打印不同通勤時間下學生的平均成績
    print(average_college_mark_sorted_by_travelling_time)
    
    # 繪製條形圖來展示不同通勤時間下學生的平均成績
    plt.figure(figsize=(10, 6))
    bars = average_college_mark_sorted_by_travelling_time.plot(kind='bar', color='salmon')
    plt.title('Question 9: Average College Mark by Travelling Time')
    plt.xlabel('Travelling Time')
    plt.ylabel('Average College Mark')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    
    # 在條形圖上方加上數值標籤，顯示平均成績
    for i, (index, value) in enumerate(average_college_mark_sorted_by_travelling_time.items()):
        plt.text(i, value + 0.02, round(value, 2), ha='center', va='bottom')
    
    # 將圖表保存為檔案
    plot_path_q9 = 'answer_pic/question9.png'
    plt.savefig(plot_path_q9)
    plt.show()

def question_ten(path):
    print(f"\n問題十:參與認證課程的學生中，每種「財務狀況」分類的學生數量")
    # 使用pandas讀取CSV檔案
    df = pd.read_csv(path)
    # 篩選出參與了認證課程的學生，按財務狀況分組，計算每組的學生數量
    certification_students_by_financial_status = df[df['Certification Course'] == 'Yes'].groupby('Financial Status').size()
    # 將結果按學生數量降序排序
    certification_students_by_financial_status_sorted = certification_students_by_financial_status.sort_values(ascending=False)

    # 格式化輸出每種「財務狀況」分類下參與認證課程的學生數量
    sorted_financial_status_output = "\n".join([f"{status}: {count}人" for status, count in certification_students_by_financial_status_sorted.items()])
    print(sorted_financial_status_output)
    
    # 繪製條形圖展示每種「財務狀況」分類下參與認證課程的學生數量
    plt.figure(figsize=(10, 6))
    bars = certification_students_by_financial_status.plot(kind='bar', color='teal')
    plt.title('Question10:參與認證課程的學生中，每種「財務狀況」分類的學生數量')
    plt.xlabel('Financial Status')
    plt.ylabel('Number of Students')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # 在條形圖上加上學生數量
    for bar in bars.patches:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1, f'{bar.get_height()}', 
                 ha='center', va='bottom')

    # 將圖表保存為檔案
    plot_path_q10 = 'answer_pic/question10.png'
    plt.savefig(plot_path_q10)
    plt.show()
    
    
def main():
    """csv文件說明
    這是一個有關學生行為的csv數據,出自Kaggle開放式平台的數據
    網頁:https://www.kaggle.com/datasets/gunapro/student-behavior/
    下面為csv各欄位的說明
    
    Certification Course->指示學生是否完成了任何認證課程
    Gender->學生的性別
    Department->學生所就讀的學科或領域
    Height (CM)->學生的身高（以公分計）
    Weight (KG)->學生的體重（以公斤計）
    10th Mark->學生在10年級所獲得的成績
    12th Mark->學生在12年級所獲得的成績
    College Mark->學生在大學或學院所獲得的成績
    Hobbies->學生的嗜好或興趣
    Daily Studying Time->學生每天花在學習上的時間
    Prefer to Study in->學生偏好的學習環境或地點
    Salary Expectation->學生對未來薪資的期望
    Do you like your degree?->學生是否喜歡他們的學位
    Willingness to pursue a career based on their degree->學生是否願意從事與其學位相關的職業
    Social Media & Video->學生如何參與社交媒體和視頻平台
    Traveling Time->學生到學校或教育機構的通勤時間
    Stress Level->學生自覺的壓力水平
    Financial Status->學生的財務狀況或經濟背景
    Part-time Job->學生是否有兼職工作

    """
    #傳入csv檔案path
    path = 'student-behavior.csv'
    
    from matplotlib.font_manager import fontManager
    import matplotlib as mpl
    fontManager.addfont('TaipeiSansTCBeta-Regular.ttf')
    mpl.rc('font', family='Taipei Sans TC Beta')
    
    # 問題一解答
    question_one(path)
    # 問題二解答
    question_two(path)
    # 問題三解答
    question_three(path)
    # 問題四解答
    question_four(path)
    # 問題五回答
    question_five(path)
    # 問題六回答
    question_six(path)
    # 問題七回答
    question_seven(path)
    # 問題八回答
    question_eight(path)
    # 問題九回答
    question_nine(path)
    # 問題十回答
    question_ten(path)


if __name__ == '__main__':
    main()