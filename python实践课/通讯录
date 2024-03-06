import csv
import os
# 获取当前脚本所在目录
dir_path = os.path.dirname(os.path.realpath(__file__))
# 构造 CSV 文件路径
file_path = os.path.join(dir_path, 'contacts.csv')
# 读取 CSV 文件，并返回保存通讯录信息的列表
def load_contacts():
 with open(file_path, 'r', newline='') as f:
 reader = csv.reader(f)
 contacts = []
 for row in reader:
 contacts.append(row)
 return contacts
# 保存信息到 CSV 文件中
def save_contacts(contacts, file_path):
 with open(file_path, 'w', newline='') as f:
 writer = csv.writer(f)
 writer.writerows(contacts)
# 显示通讯录信息
def show_contacts(contacts, page_size=6):
 print("=" * 20 + "通讯录" + "=" * 20)
 print("姓名\t\t 手机号码\t\t 通讯地址")
 page_num = 1
 length = len(contacts)
 if length == 0:
 print("通讯录为空！")
 return
 page_count = (length // page_size) + 1
 flag = True
 while True:
 start = (page_num - 1) * page_size
 end = min(length, start + page_size)
 for row in contacts[start:end]:
 print("{}\t\t{}\t\t{}".format(row[0], row[1], row[2]))
 choice = input(
 f'共有{page_count}页，当前第{page_num}页，’b‘：返回上一页，’n‘：
跳转到下一页，其他任意键退出分页模式。\n')
 if choice == "n" and page_num < page_count:
 page_num += 1
 elif choice == "b" and page_num > 1:
 page_num -= 1
 else:
 break
# 新增联系人
def add_contact(contacts, file_path):
 while True:
 name = input("请输入联系人姓名：")
 while True:
 phone = input("请输入联系人电话号码：")
 if len(phone)>=11:
 break
 else:
 print("输入电话长度不合法，请重新输入")
 address = input("请输入联系人通讯地址：")
 contacts.append([name, phone, address])
 save_contacts(contacts, file_path)
 print("添加成功！请选择是否继续添加")
 x = str(input("请输入 yes or no:"))
 if x == "no":
 break
# 删除联系人
def remove_contact(contacts, file_path):
 name = input("请输入要删除的联系人姓名：")
 found = False
 for row in contacts:
 if row[0] == name:
 contacts.remove(row)
 found = True
 break
 if found:
 save_contacts(contacts, file_path)
 print("删除成功！")
 else:
 print("该联系人不存在。")
# 修改联系人
def modify_contact(contacts, file_path):
 #修改前先输出一遍列表，方便查看错误进行修改
 show_contacts(contacts)
 name = input("请输入要修改的联系人姓名：")
 found = False
 for row in contacts:
 if row[0] == name:
 phone = input("请输入联系人新的手机号码：")
 address = input("请输入联系人新的通讯地址：")
 row[1] = phone
 row[2] = address
 found = True
 break
 if found:
 save_contacts(contacts, file_path)
 print("修改成功！")
 else:
 print("该联系人不存在。")
# 查询联系人
def search_contact(contacts):
 keyword = input("请输入查询关键词（姓名、手机号码或通讯地址）：")
 results = []
 '''使用一个 for 循环遍历联系人列表中的每一行数据（由三个元素组成）。
 对于每行数据，它会检查关键词是否出现在该行的第一个、第二个或第三个元素中。
 如果是，则将该行数据加入 results 列表中。'''
 for row in contacts:
 if keyword in row[0] or keyword in row[1] or keyword in 
row[2]:
 results.append(row)
 if len(results) > 0:
 show_contacts(results)
 else:
 print("未找到相关联系人。")
def main():
 global file_path
 # 构造 CSV 文件路径
 file_path = os.path.join(dir_path, 'contacts.csv')
 contacts = load_contacts()
 while True:
 print("=" * 20 + "菜单" + "=" * 20)
 print("1. 显示清单")
 print("2. 增加记录")
 print("3. 删除记录")
 print("4. 修改记录")
 print("5. 查询记录")
 print("6. 退出程序")
 choice = input("请输入操作序号：")
 if choice == '1':
 show_contacts(contacts)
 elif choice == '2':
 add_contact(contacts, file_path)
 elif choice == '3':
 remove_contact(contacts, file_path)
 elif choice == '4':
 modify_contact(contacts, file_path)
 elif choice == '5':
 search_contact(contacts)
 elif choice == '6':
 exit()
 else:
 print("无效的操作，请重新输入。")
if __name__ == "__main__":
 main()
