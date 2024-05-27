from fastapi import APIRouter, HTTPException
from app.db.schema import connect, Comment, Post, User


router = APIRouter()


@router.get(
    "/comment",
    tags="Comment",
    response_model=dict,
    description="Get all the comments",
    )
def get_comment():
    """
    Get all the comments.

    - id: The unique identifier of the comment.
    - content: The content of the comment.
    - created_at: The timestamp when the comment was created.
    - user: A dictionary representing the user who created the comment. It contains the following keys:
        - id: The unique identifier of the user.
        - name: The username of the user.
        - email: The email of the user.
        - password: The password of the user.
    - post: A dictionary representing the post associated with the comment. It contains the following keys:
        - id: The unique identifier of the post.
        - title: The title of the post.
        - content: The content of the post.
        - user_id: The unique identifier of the user who created the post.
        - created_at: The timestamp when the post was created.

    Returns:
    - A dictionary with the following keys:
      - count: The number of comments retrieved.
      - comments: A list of comment dictionaries.

    Raises:
    - HTTPException: If there is an error while retrieving the comments.

    """
    try:
        session = connect.session
        result = session.query(Comment).join(User, Comment.user_id == User.id).join(Post, Comment.post_id == User.id)
        output = []
        for r in result:
            output.append({
                "id": r.id,
                "content": r.content,
                "created_at": r.created_at,
                "user": {
                    "id": r.user.id,
                    "name": r.user.username,
                    "email": r.user.email,
                    "password": r.user.password
                },
                "post": {
                    "id": r.post.id,
                    "title": r.post.title,
                    "content": r.post.content,
                    "user_id": r.post.user_id,
                    "created_at": r.post.created_at
                }
                })
        return {
            "count": len(output),
            "comments": output
            }
    except Exception as e:
        print("Unable to get the comments. Reason: %s" % str(e))
        raise HTTPException(
            status_code=500,
            detail="Unable to get the comments",
        )
