import csv
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']='SimHei' #设置字体为黑体
plt.rcParams['axes.unicode_minus']=False #用来正常显示负值
# 从 CSV 文件中读取学生成绩数据
def read_student_info_from_csv(file_name):
 with open(file_name, mode='r', encoding='utf-8') as f:
 reader = csv.DictReader(f)
 students_scores = []
 for row in reader:
 students_scores.append(row)
 return students_scores
# 绘制指定学科成绩分布直方图
def plot_grades_distribution(scores, subject_name):
 # 设置直方图的数据和区间
 x = np.array(scores)
 bins = np.arange(0, 110, 10)
 # 绘制直方图
 plt.hist(x, bins=bins, edgecolor='black', alpha=0.75)
 # 设置 X 轴和 Y 轴标题等信息
 plt.xlabel("分数")
 plt.ylabel("学生人数")
 plt.title(subject_name + ' 等级分布直方图')
 plt.show()
# 生成指定学科的成绩分析报告
def generate_subject_report(students_scores, subject_name):
 # 判断输入的学科是否存在
 if subject_name not in students_scores[0]:
 print("很抱歉，该班级没有这门课程")
 return None
 # 获取所有学生对应学科的成绩
 scores = [int(student_score[subject_name]) for student_score in 
students_scores]
 # 统计不及格学生名单
 failed_students = [student_score['姓名'] for student_score in 
students_scores if
 int(student_score[subject_name]) < 60]
 # 生成成绩分析报告信息
 report = {
 '课程': subject_name,
 '不及格名单': failed_students
 }
 plot_grades_distribution(scores, subject_name)
 return report
if __name__ == '__main__':
 # 学科名称和学分的字典映射
 subject_scores = {'语文': 5, '数学': 4, '英语': 3, '物理': 2, '化学': 
1}
 subject_names = list(subject_scores.keys())
 # 读取学生成绩数据
 students_scores = 
read_student_info_from_csv('students_scores.csv')
 # 获取需要生成报告的学科名称
 input_subject = input("请输入您要生成报告的学科：")
 while input_subject not in subject_names:
 print("输入班级中不存在的学科，请重新输入。可供查询的学科：", 
subject_names)
 input_subject = input("请输入您要生成报告的学科：")
 # 调用函数生成指定学科的成绩分析报告，仅输出该学科，
 # 如果输入的学科不存在，则程序结束。
 report = generate_subject_report(students_scores, input_subject)
 if report is not None:
 # 输出指定学科的成绩分析报告信息
 print(report)
 # 展示成绩
