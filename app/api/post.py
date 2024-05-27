from fastapi import APIRouter, HTTPException
from app.db.schema import connect, Post, User


router = APIRouter()


@router.get(
    "/post",
    tags="Post",
    response_model=dict,
    description="Get all the posts",
    )
def get_post():
    """
    Get all the posts.

    Each post dictionary has the following keys:
    - id: The unique identifier of the post.
    - title: The title of the post.
    - content: The content of the post.
    - created_at: The timestamp when the post was created.
    - user: A dictionary representing the user who created the post. It contains the following keys:
        - id: The unique identifier of the user.
        - name: The username of the user.
        - email: The email of the user.
        - password: The password of the user.

    Returns:
    - A dictionary with the following keys:
      - count: The number of posts retrieved.
      - posts: A list of post dictionaries.

    Raises:
    - HTTPException: If there is an error while retrieving the posts.
    """
    try:
        session = connect.session
        result = session.query(Post).join(User, Post.user_id == User.id)
        output = []
        for r in result:
            output.append({
                "id": r.id,
                "title": r.title,
                "content": r.content,
                "created_at": r.created_at,
                "user": {
                    "id": r.user.id,
                    "name": r.user.username,
                    "email": r.user.email,
                    "password": r.user.password
                }
                })
        return {
            "count": len(output),
            "posts": output
            }
    except Exception as e:
        print("Unable to get the posts. Reason: %s" % str(e))
        raise HTTPException(
            status_code=500,
            detail="Unable to get the posts",
        )
