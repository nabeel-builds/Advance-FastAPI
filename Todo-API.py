from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

# create todo
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "TODO Added", "data": todo}



# get all todos
@app.get("/todos")
def get_todos():
    return todos



# get single todos
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}



# update Todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, update_todo:Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = update_todo
            return{
                "message": "data Updated",
                "data": update_todo
            }
        return{
            "error": "Todo not found"
        }




# delete todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return{
                "message": "Data deleted successfully",
            }
        return{
            "error": "Error for deleteing the data"
        }