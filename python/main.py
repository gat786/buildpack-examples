import os

import uvicorn
from fastapi import FastAPI

app = FastAPI()
port = os.getenv("PORT", "8080")
port = int(port)
run_env = os.getenv("ENVIRONMENT", "dev")


@app.get("/")
def read_root():
    return {"Hello": "World"}


def main():
    uvicorn.run("main:app", port=port, reload=(run_env == "dev"))


if __name__ == "__main__":
    main()
