import fastapi
import fastapi.middleware.cors as cors

app = fastapi.FastAPI()

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)


@app.get('/')
def wakeup():
    return True
