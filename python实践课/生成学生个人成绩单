import csv
# 定义学科名称和学分信息
subject_names = ['语文', '数学', '英语', '物理', '化学']
subject_scores = {'语文': 5, '数学': 4, '英语': 3, '物理': 2, '化学': 1}
# 从 CSV 文件中读取学生成绩数据
def read_student_info_from_csv(file_name):
 with open(file_name, mode='r', encoding='utf-8') as f:
 reader = csv.DictReader(f)
 students_scores = []
 for row in reader:
 students_scores.append(row)
 return students_scores
# 根据输入的学生学号或名字查找对应的学生记录
def find_student_record(students_scores):
 query_info = input('请输入要查询成绩报告的学生学号或姓名：')
 for student_score in students_scores:
 if query_info == student_score['学号'] or query_info == 
student_score['姓名']:
 return student_score
 print('未找到该学生记录！')
# 生成学生个人成绩报告单
def generate_student_report(student_score):
 # 计算每个学科的等级
 scores = [int(score) for score in 
list(student_score.values())[2:7]]
 # 计算学生的学分绩点和总学分
 score_points = [(score-60)//10+1 for score in scores]
 total_score = sum([score*subject_scores[subject_names[i]] for i, 
score in enumerate(scores)])
 grade_point = sum([score_point*score for (score_point, score) in 
zip(score_points, 
subject_scores.values())])/sum(subject_scores.values())
 # 生成成绩报告信息
 report = {
 '学号': student_score['学号'],
 '姓名': student_score['姓名'],
 '成绩': dict(zip(subject_names, scores)),
 '学分绩点': grade_point,
 '总学分': total_score
 }
 return report
if __name__ == '__main__':
 # 读取学生成绩数据
 students_scores = 
read_student_info_from_csv('students_scores.csv')
 # 根据输入查询学生记录并生成成绩报告单
 student_record = find_student_record(students_scores)
 if student_record:
 report = generate_student_report(student_record)
 print(report)
