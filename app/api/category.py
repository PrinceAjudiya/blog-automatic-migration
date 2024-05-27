from fastapi import APIRouter, HTTPException
from app.db.schema import connect, Category, Post


router = APIRouter()


@router.get(
    "/category",
    tags="Category",
    response_model=dict,
    description="Get all the categories",
    )
def get_category():
    """
    Get all the categories.

    Each category object has the following attributes:
    - id: The unique identifier of the category.
    - name: The name of the category.
    - post: A dictionary representing the post associated with the category.
      - id: The unique identifier of the post.
      - title: The title of the post.
      - content: The content of the post.
      - user_id: The unique identifier of the user who created the post.
      - created_at: The timestamp when the post was created.

    Returns:
    - A dictionary with the following keys:
      - count: The number of categories retrieved.
      - categories: A list of category objects.

    Raises:
    - HTTPException: If there is an error while retrieving the categories.

    """
    try:
        session = connect.session
        result = session.query(Category).join(Post, Category.post_id == Post.id)
        output = []
        for r in result:
            output.append({
                "id": r.id,
                "name": r.name,
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
            "categories": output
            }
    except Exception as e:
        print("Unable to get the categories. Reason: %s" % str(e))
        raise HTTPException(
            status_code=500,
            detail="Unable to get the categories",
        )
