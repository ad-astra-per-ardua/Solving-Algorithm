from fastapi import FastAPI

app = FastAPI()

items = ['Macbook','Apple Watch', 'iPhone', 'Air Pods']
# @app.get('/items')
# async def read_items():
#     return items

@app.get('/items/{id}')
async def read_id_item(id):
    return items[int(id)]

@app.get('/items/')
async def read_item(skip:int=0, limit:int=10):
    return items[skip:skip+limit]