import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from datetime import datetime
from create_pdf import take_pdf

# uvicorn main:app --reload
app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)


class InvoiceData(BaseModel):
    organization: str
    requisites: str
    cards: int | None
    pouchs: int | None


@app.get('/')
def wakeup():
    return True


@app.post('/create-invoice')
def create_invoice(body: InvoiceData):
    invoice_data = jsonable_encoder(body)
    response = take_pdf(invoice_data['organization'], invoice_data['requisites'], invoice_data['cards'], invoice_data['pouchs'])
    return response
