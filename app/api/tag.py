from fastapi import APIRouter, HTTPException
from app.db.schema import connect, Tag, Post


router = APIRouter()

@router.get(
    "/tag",
    tags="Tag",
    response_model=dict,
    description="Get all the tags",
    )
def get_tag():
    """
    Get all the tags.

    - "id": The unique identifier of the tag.
    - "name": The name of the tag.
    - "post": A dictionary representing the post associated with the tag. It contains the following keys:
        - "id": The unique identifier of the post.
        - "title": The title of the post.
        - "content": The content of the post.
        - "user_id": The unique identifier of the user who created the post.
        - "created_at": The timestamp when the post was created.

    Returns:
        dict: A dictionary with two keys: "count" and "tags".
            - "count" (int): The number of tags retrieved.
            - "tags" (list): A list of dictionaries, where each dictionary represents a tag.

    Raises:
        HTTPException: If there is an error while retrieving the tags.
    """
    try:
        session = connect.session
        result = session.query(Tag).join(Post, Tag.post_id == Post.id)
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
            "tags": output
            }
    except Exception as e:
        print("Unable to get the tags. Reason: %s" % str(e))
        raise HTTPException(
            status_code=500,
            detail="Unable to get the tags",
        )
