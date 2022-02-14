# from bigfastapi.db import create_database as create_database_bfa
import bigfastapi
import uvicorn
from bigfastapi.auth import app as authentication
from bigfastapi.auth_api import app as jwt_services
from bigfastapi.banks import router as banks
from bigfastapi.blog import app as blog
from bigfastapi.comments import app as comments
from bigfastapi.contact import app as contact
from bigfastapi.countries import app as countries
from bigfastapi.credit import app as credit
from bigfastapi.customer import app as customer
from bigfastapi.email import app as email
# Import all the functionality that BFA provides
from bigfastapi.faq import app as faq
from bigfastapi.files import app as files
from bigfastapi.google_auth import app as social_auth
from bigfastapi.notification import app as notification
from bigfastapi.organization import app as organization
from bigfastapi.organization import app as organization_router
from bigfastapi.pages import app as pages
from bigfastapi.pdfs import app as pdfs
from bigfastapi.plans import app as plans
from bigfastapi.qrcode import app as qrcode
from bigfastapi.receipts import app as receipts
from bigfastapi.settings import app as settings
from bigfastapi.sms import app as sms
from bigfastapi.users import app as accounts
from bigfastapi.users import app as accounts_router
from bigfastapi.wallet import app as wallet
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware


app = FastAPI()

bigfastapi.db.database.create_database()
create_database()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(authentication, tags=["Auth"])
app.include_router(social_auth)
app.include_router(accounts_router, tags=["User"])
app.include_router(organization_router, tags=["Organization"])
app.include_router(countries, tags=["Countries"])
app.include_router(faq)
app.include_router(contact)
app.include_router(blog, tags=["Blog"])
app.include_router(pages, tags=["Pages"])
app.include_router(plans, tags=['Plans'])
app.include_router(email)
app.include_router(files, tags=["File"])
app.include_router(accounts, tags=["Auth"])
app.include_router(comments, tags=["Comments"])
app.include_router(banks, tags=["Banks"], prefix="/stores/{store_id}")
app.include_router(countries, tags=["Countries"])
app.include_router(organization, tags=["Organization"])
app.include_router(qrcode, tags=["qrcode"])
app.include_router(settings, tags=["Settings"])
app.include_router(wallet, tags=["Wallet"])
app.include_router(notification, tags=["Notification"])
app.include_router(credit)
app.include_router(pdfs)
app.include_router(jwt_services)
app.include_router(receipts)
app.include_router(customer)
app.include_router(customer, tags=['Customers'], prefix="/stores/{store_id}")
app.include_router(sms)


@app.get("/", tags=["Home"])
async def get_root() -> dict:
    return {
        "message": "Welcome to Ziki.",
        "url": "http://127.0.0.1:7001/docs",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=7001, reload=True)