import csv
import random
# 定义学科名称和学分信息
subject_names = ['语文', '数学', '英语', '物理', '化学']
subject_scores = {'语文': 5, '数学': 4, '英语': 3, '物理': 2, '化学': 1}
# 将学生成绩列表写入 CSV 文件中
def write_student_info_to_csv(file_name, students):
 with open(file_name, mode='w', encoding='utf-8', newline='') as f:
 writer = csv.writer(f)
 # 写入表头
 headers = ['学号', '姓名'] + subject_names + 
[subject_names[i]+'学分' for i in range(5)] + ['学分绩点', '总学分']
 writer.writerow(headers)
 # 写入学生成绩数据
 for student in students:
 writer.writerow(student)
# 生成学生信息和成绩数据
def generate_student_info(n):
 students = []
 for i in range(1, n+1):
 # 随机生成学号
 student_id = 'stu' + str(i).zfill(4) #.zfill(4) 是一个字符串方法，
用于将字符串在左边填充 0，使其总长度为 4
 # 随机生成姓名
 first_name = random.choice(['张', '王', '李', '赵', '钱', '孙', 
'周', '吴', '郑'])
 last_name = random.choice(['一', '二', '三', '四', '五', '六', 
'七', '八', '九'])
 student_name = first_name + last_name
 # 随机生成五门学科的成绩
 scores = [random.randint(20, 100) for _ in range(5)] #这里生成类
似[56,48,80,76,99]的列表
 # 计算学分绩点和总学分
 score_points = [(score-60)//10+1 for score in scores] 
#[1.5,2,3,0.7,0.5]
 '''该行代码先使用 zip() 函数将 score_points 和
subject_scores.values() 中的元素一一对应起来，
 构造 (score_point, score) 的二元组。然后通过列表推导式，
 计算第 i 门科目的得分情况 score_points[i] 与其对应的成绩
subject_scores.values()[i] 相乘所得到的分数，
 并将这些分数相加，得到总分。最后将总分除以每门课程的学分之和，即可得到加权
平均分。'''
 grade_point = sum([score_point*score for (score_point, score) 
in zip(score_points, subject_scores.values())])\
 /sum(subject_scores.values())
 total_score = sum([score*subject_scores[subject_names[i]] for 
i, score in enumerate(scores)])
 # 将学生信息和成绩存储到 students 列表中
 students.append([student_id, student_name] + scores + 
score_points + [grade_point, total_score])
 return students
if __name__ == '__main__':
 # 生成 40 名学生的成绩数据
 students = generate_student_info(40)
 # 将学生成绩数据写入 CSV 文件中
 write_student_info_to_csv('students_scores.csv', students)
