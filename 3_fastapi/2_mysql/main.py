import router
import uvicorn
from fastapi import FastAPI


def main():
    app = FastAPI()
    app.include_router(router.demo_router())
    return app


if __name__ == "__main__":
    uvicorn.run(main(), host="0.0.0.0", port=8000)
