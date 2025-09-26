import json
class Task:
    """代表一个独立的任务"""
    def __init__(self, title):
        self.title = title
        self.is_done = False
    
    def mark_as_done(self):
        self.is_done = True

    def to_dict(self):
        return{"title":self.title,"is_done":self.is_done}

class TodoList:
    """代表整个事项代办列表应用"""
    def __init__(self,filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """从文件中加载任务（这是一个“内部”方法）"""
        try:
            with open(self.filename,'r',encoding='utf-8') as f:
                tasks_as_dicts = json.load(f)
                tasks_list = []
                for d in tasks_as_dicts:
                    task = Task(d['title'])
                    if d['is_done']:
                        task.mark_as_done()
                    tasks_list.append(task)
                print("任务加载成功。")
                return tasks_list
        except FileNotFoundError:
            print("未找到任务列表，将创建一个新的列表。")
            return []
        
    def _save_tasks(self):
        """将任务保存到文件（这是一个“内部”方法）"""
        tasks_as_dicts = [task.to_dict() for task in self.tasks]
        with open(self.filename,'w',encoding='utf-8') as f:
            json.dump(tasks_as_dicts,f,indent=4,ensure_ascii=False)
        print("提示：任务已自动保存。")

    def display_menu(self):
        """显示主菜单"""
        print("\n===== To-Do List Menu =====")
        print("1. 添加新任务")
        print("2. 查看所有任务")
        print("3. 标记任务为已完成")
        print("4. 删除任务")
        print("5. 退出程序")
        print("===========================")

    def add_task(self):
        """处理添加新任务的逻辑"""
        task_title = input("请输入要添加的任务内容：")
        self.tasks.append(Task(task_title))
        print(f"任务'{task_title}'已成功添加！")

    def view_tasks(self):
        """处理查看所有任务的逻辑"""
        print("/n---所有任务---")
        if not self.tasks:
            print("当前没有任何任务。")
        else:
            for i, task in enumerate(self.tasks):
                status = "✔" if task.is_done else "✘"
                print(f"{i + 1}.[{status}]{task.title}")

    def mark_tasks(self):
        """处理标记所有任务已完成的逻辑"""
        if not self.tasks:
            print("当前没有任何任务可供标记。")
            return
        
        for i, task in enumerate(self.tasks):
            status = "✔" if task.is_done else "✘"
            print(f"{i + 1}. [{status}] {task.title}")

        try:
            task_num_str = input("请输入要标记为已完成的任务序号: ")
            task_index = int(task_num_str) - 1 

            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index].mark_as_done()
                print(f"任务 '{self.tasks[task_index].title}' 已标记为完成。")
            else:
                print("无效的序号。")
        except ValueError:
            print("输入错误，请输入一个数字。")

    def delete_tasks(self):
        """处理删除任务的逻辑"""
        if not self.tasks:
            print("当前没有任何任务可供删除。")
        for i, task in enumerate(self.tasks):
            status = "✔" if task.is_done else "✘"
            print(f"{i + 1}. [{status}] {task.title}")

        try:
            task_num_str = input("请输入要删除的任务序号: ")
            task_index = int(task_num_str) - 1

            if 0 <= task_index < len(self.tasks):
                removed_task = self.tasks.pop(task_index)
                print(f"任务 '{removed_task.title}' 已被删除。")
            else:
                print("无效的序号。")
        except ValueError:
            print("输入错误，请输入一个数字。")

    def exit_procedure(self):
        """处理退出程序的逻辑"""
        print("感谢使用 To-Do List，再见！")
    
    def run(self):
        """运行应用的主程序"""
        while True:
            self.display_menu()
            choice = input("请输入您的选择 (1-5): ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_tasks()
            elif choice == '4':
                self.delete_tasks()
            elif choice == '5':
                self._save_tasks()
                self.exit_procedure()
                break
            else:
                print("无效输入，请输入 1 到 5 之间的数字。")

if __name__ =="__main__":
    my_todo_list = TodoList()
    my_todo_list.run()