class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False
    def mark_as_done(self):
        self.is_done = True
tasks = []
def display_menu():
    print("\n===== To-Do List Menu =====")
    print("1. 添加新任务")
    print("2. 查看所有任务")
    print("3. 标记任务为已完成")
    print("4. 删除任务")
    print("5. 退出程序")
    print("===========================")
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
        print("感谢使用 To-Do List，再见！")
        break
    else:
        print("无效输入，请输入 1 到 5 之间的数字。")             