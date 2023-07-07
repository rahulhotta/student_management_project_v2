from fastapi import FastAPI
from scripts.core.services.student_info_services import student_router
import uvicorn

# import logging
# import scripts.logging.logger
app=FastAPI()


app.include_router(student_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)

