import random
workers = 20
total_salary = 10000
basic_salary = 1000
for i in range(workers+1):
    num = random.randint(1, 10)

    if num<5:
        print("员工 %d ，绩效分 %d ，低于5，不发工资"%(i,num))
        continue


    if total_salary<=0 :
        print("工资发完了，下个月再来吧")
        break
    else:
        if total_salary < 0:
            print("向员工 %d 发放工资 %d ，账户余额不足" % (i, basic_salary))
            total_salary += basic_salary  # 把扣除的工资加回去，因为余额不足
        else:
            total_salary = total_salary-basic_salary
            print("向员工 %d 发放工资 %d ，账户余额 %d 元"%(i,basic_salary,total_salary))
