from fastapi import APIRouter, HTTPException
import requests


router = APIRouter(
    tags=["root"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
@router.get("/{entry}")
def read_entry(entry=None):
    try:
        if entry:
            data = requests.get(
                f"https://botw-compendium.herokuapp.com/api/v3/compendium/entry/{entry}"
            )
        else:
            data = requests.get(
                "https://botw-compendium.herokuapp.com/api/v3/compendium/all"
            )
        return data.json()
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=404, detail=str(e))