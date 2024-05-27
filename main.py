from fastapi import FastAPI
from app.api import user, post, comment, category, tag

API_PREFIX = "/api"
app = FastAPI(title="Blog Details")


app.include_router(user.router, prefix=API_PREFIX)
app.include_router(post.router, prefix=API_PREFIX)
app.include_router(comment.router, prefix=API_PREFIX)
app.include_router(category.router, prefix=API_PREFIX)
app.include_router(tag.router, prefix=API_PREFIX)
