import json
class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False
    
    def mark_as_done(self):
        self.is_done = True

    def mark_as_undone(self):
        self.is_done = False

    def to_dict(self):
        return{"title":self.title,"is_done":self.is_done}

def save_tasks_to_file(tasks_list,filename="tasks.json"):
    """将任务列表保存到JSON文件。"""
    tasks_as_dicts = [task.to_dict() for task in tasks_list]
    with open(filename,'w',encoding='utf-8') as f:
        json.dump(tasks_as_dicts,f,indent=4,ensure_ascii=False)
    print("提示：任务已自动保存。")

def load_tasks_from_file(filename="tasks.json"):
    """从JSON文件加载任务列表。"""
    try:
        with open(filename,'r',encoding='utf-8') as f:
            tasks_as_dicts = json.load(f)
            tasks_list = []
            for d in tasks_as_dicts:
                task = Task(d['title'])
                if d['is_done']:
                    task.mark_as_done()
                tasks_list.append(task)
            return tasks_list
    except FileNotFoundError:
        return []   

def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. 添加新任务")
    print("2. 查看所有任务")
    print("3. 标记任务为已完成")
    print("4. 删除任务")
    print("5. 退出程序")
    print("===========================")

print("正在从文件加载任务...")
tasks=load_tasks_from_file()

while True:
    display_menu()
    choice = input("请输入您的选择 (1-5): ")
    if choice == '1':
        task_title = input("请输入要添加的任务内容: ")
        new_task = Task(task_title)
        tasks.append(new_task)
        print(f"任务 '{task_title}' 已成功添加!")
    elif choice == '2':
        print("\n--- 所有任务 ---")
        if not tasks:
            print("当前没有任何任务。")
        else:
            for i, task in enumerate(tasks):
                status = "✔" if task.is_done else "✘"
                print(f"{i + 1}. [{status}] {task.title}")    
    elif choice == '3':
        if not tasks:
            print("当前没有任何任务可供标记。")
            continue
        for i, task in enumerate(tasks):
            status = "✔" if task.is_done else "✘"
            print(f"{i + 1}. [{status}] {task.title}")
        try:
            task_num_str = input("请输入要标记为已完成的任务序号: ")
            task_index = int(task_num_str) - 1 
            if 0 <= task_index < len(tasks):
                tasks[task_index].mark_as_done()
                print(f"任务 '{tasks[task_index].title}' 已标记为完成。")
            else:
                print("无效的序号。")
        except ValueError:
            print("输入错误，请输入一个数字。")   
    elif choice == '4':
        if not tasks:
            print("当前没有任何任务可供删除。")
            continue

        for i, task in enumerate(tasks):
            status = "✔" if task.is_done else "✘"
            print(f"{i + 1}. [{status}] {task.title}")

        try:
            task_num_str = input("请输入要删除的任务序号: ")
            task_index = int(task_num_str) - 1

            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"任务 '{removed_task.title}' 已被删除。")
            else:
                print("无效的序号。")
        except ValueError:
            print("输入错误，请输入一个数字。")
    elif choice == '5':
        save_tasks_to_file(tasks)
        print("感谢使用 To-Do List，再见！")
        break
    else:
        print("无效输入，请输入 1 到 5 之间的数字。")             