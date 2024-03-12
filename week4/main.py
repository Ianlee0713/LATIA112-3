import pandas as pd


def question_one(path):
    # 創建DataFrame
    df = pd.read_csv(path)

    # 計算每個年級的平均讀書時間
    average_reading_time_by_grade = df.groupby("2. 年級")["13. 每周總讀書時間(請輸入數字，單位為小時)"].mean()

    # 四捨五入到小數點第二位，並為每個數值後面加上"小時"
    average_reading_time_by_grade_with_hours = average_reading_time_by_grade.round(2).apply(lambda x: f"{x} 小時")

    # 將調整後的數據轉換為字符串格式，準備輸出
    average_reading_time_by_grade_with_hours_str = average_reading_time_by_grade_with_hours.to_string(index=True, header=False)

    print(average_reading_time_by_grade_with_hours_str) 


def question_two(path):
    df = pd.read_csv(path)
    time_usage_counts = df['5. 每天使用3C時間多寡，以小時計(是指看影片、社群、打Game等等)'].value_counts().reset_index()
    time_usage_counts.columns = ['每天使用3C時間範圍', '人數']
    print(time_usage_counts)
    
def question_three(path):
    df = pd.read_csv(path)
    average_credits_by_grade = df.groupby('2. 年級')['4. 這學期學分數(請輸入數字，單位為學分)'].mean().reset_index()
    average_credits_by_grade.columns = ['年級', '平均學分數']

    ordered_grades = ['大一', '大二', '大三', '大四']
    average_credits_by_grade['年級'] = pd.Categorical(average_credits_by_grade['年級'], categories=ordered_grades, ordered=True)
    average_credits_by_grade_sorted = average_credits_by_grade.sort_values('年級')
    average_credits_by_grade_sorted['平均學分數'] = average_credits_by_grade_sorted['平均學分數'].round(2)

    print(average_credits_by_grade_sorted)

    
if __name__ == "__main__":
    
    # std_each_week_study_tf.csv
    path = "week4/std_each_week_study_tf.csv"
    print(f"問題一：大一、大二、大三、大四學生的讀書平均時間？")
    question_one(path)
    
    print(f"問題二：平均3C的使用時間？")
    question_two(path)
    
    print(f"問題三：每個年級的平均學分數")
    question_three(path)