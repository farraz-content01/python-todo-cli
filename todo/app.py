task=[]

def add_task(title):
    task.append({"title":title, "done":False})

def get_task():
    return task
