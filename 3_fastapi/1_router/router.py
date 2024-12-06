from typing import Union

from fastapi import APIRouter


def demo_router():
    router = APIRouter()

    @router.get("/containers")
    def read_root():
        return {"Hello": "World"}

    @router.get("/mac/items/{item_id}")
    def read_item(
        item_id: str,
        q: Union[str, None] = None,
    ):
        return {"id": item_id, "q": f"{q} + mac"}

    @router.get("/win/items/{item_id}")
    def read_item(
        item_id: str,
        q: Union[str, None] = None,
    ):
        return {"id": item_id, "q": f"{q} + win"}

    # @router.post("/item")
    # def insert_item(item: Item):
    #     pass
    #
    # @router.put("/item/{item_id}"):
    # def update_item():

    return router
