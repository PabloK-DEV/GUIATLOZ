from fastapi import APIRouter, HTTPException
import requests

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{category_name}")
def read_item(category_name: str):
    try:
        data = requests.get(
            f"https://botw-compendium.herokuapp.com/api/v3/compendium/category/{category_name}"
        )
        return data.json()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail=str(e))
