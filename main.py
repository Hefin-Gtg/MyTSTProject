from fastapi import FastAPI

import uvicorn

# App routers
from auth import routers as AuthRouter
from user import routers as UserRouter
from product import routers as ProductRouter


app = FastAPI(title="Product Monitoring and Demand Prediction")

app.include_router(AuthRouter.router)
app.include_router(UserRouter.router)
app.include_router(ProductRouter.router)

@app.get("/")
def welcome():
        return {"message": "Welcome To Product Demand Prediction"}

if __name__ == '__main__':
	# uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
        uvicorn.run('main:app',reload=True)