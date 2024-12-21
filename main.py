from enum import Enum
from typing import Annotated, Literal
from pydantic import BaseModel, Field

from fastapi import Body, FastAPI, Path, Query

app = FastAPI()


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query

# Multiple body params and query



# Singular values in body
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
    # results = {"item_id": item_id, "item": item, "user": user}
    # return results


# @app.put("/items/{item_id}")
# async def update_item(
    # item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=100)],
    # q: str | None = None,
    # item: Item | None = None
# ):
    # results = {"item_id": item_id}
    # if q:
        # results.update({"q": q})
    # if item:
        # results.update({"item": item})
    # return results



# class Item(BaseModel):
    # name: str
    # description: str | None = None
    # price: float
    # tax: float | None = None


# class ModelName(str, Enum):
    # alexnet = "alexnet"
    # resnet = "resnet"
    # lenet = "lenet"


# @app.get("/items/{item_id}")
# async def read_items(item_id: Annotated[int, Path(title="The ID of the item to get", ge=1)], q: Annotated[str | None, Query(alias="item-query")] = None):
    # results = {"item_id": item_id}
    # if q:
        # results.update({"q": q})
    # return results


# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.model_dump()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({
#             "price_with_tax": price_with_tax
#         })  
#     return item_dict


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.model_dump()}
#     if q:
#         result.update({"q": q})
#     return result


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(min_length=3, max_length=50,)] = "fixedquery"):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[list[str] | None, Query()] = ["foo", "bar"]):
#     query_items = {"q": q}
#     return query_items


# @app.get("/items/")
# async def read_items(q: Annotated[str | None, Query(alias="item-query", title="Query string", description="Query string for the items to search in the database that have a good match", min_length=3, deprecated=True, include_in_schema=False)] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


# fake_items_db = [
#     {"item_name": "Foo"},
#     {"item_name": "Bar"},
#     {"item_name": "Baz"}
# ]

# @app.get("/")
# async def root():
    # return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


# @app.get("/users/me")
# async def read_user_me():
    # return {"user_id": "the_current user"}


# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
    # return {"user_id": user_id}


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
    # if model_name is ModelName.alexnet:
        # return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # 
    # if model_name.value == "lenet":
        # return {"model_name": model_name, "message": "LeCNN all the images"}
# 
    # return {"model_name": model_name, "message": "Have some residuals"}


# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
    # return {"file_path": file_path}
        

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: str | None = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"itemI_id": item_id, "q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# @app.get("/users/{user_id}/items/{item_id}")
# async def read_user_item(
    # user_id: int, item_id: str, q: str | None = None, short: bool = False
# ):
    # item = {"item_id": item_id, "owner_id": user_id}
    # if q:
        # item.update({"q": q})
    # if not short:
        # item.update({
            # "description": "This is an amazing item that has a long description"
        # })
    # return item