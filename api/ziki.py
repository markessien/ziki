import fastapi, os
from fastapi import FastAPI

app = APIRouter()


@app.get("/api/get_following")
def get_following(name: str, organization_id: str, db: orm.Session = fastapi.Depends(get_db)):
    return "The people xou are following"



#create debt
@app.post("/api/create", response_model= debtSchema.DebtBaseOutput)
def create_newfollow(body: debtSchema.DebtBase, db: orm.Session = fastapi.Depends(get_db)):
    return "This creates a debt"