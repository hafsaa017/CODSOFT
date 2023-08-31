# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:17:44 2023

@author: Shafeeq
"""

class ToDoList:
    def __init__(self):
        self.tasks = []

#to add a task in list named as tasks
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added:", task)

#to remove a task from the list
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed:", task)
        else:
            print("Task not found.")  
            
#to see the list that show what names of tasks are added and removed
    def list_tasks(self):
        print("Tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")
            
#to update the list
    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print("Task updated.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Update Task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task name: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task name to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.list_tasks()  #list having tasks 
        elif choice == "4":
            index = int(input("Enter the task index to update: "))
            new_task = input("Enter the new task: ")
            todo_list.update_task(index, new_task)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
