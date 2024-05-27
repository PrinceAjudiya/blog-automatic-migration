from fastapi import APIRouter, HTTPException
from app.db.schema import connect, User


router = APIRouter()


@router.get(
    "/user",
    tags="User",
    response_model=dict,
    description="Get all the users",
    )
def get_user():
    """
    Get all the users.

    - "id" (int): The unique identifier of the user.
    - "name" (str): The username of the user.
    - "email" (str): The email of the user.
    - "password" (str): The password of the user.

    Returns:
        dict: A dictionary with two keys: "count" and "users".
        - "count" (int): The number of tags retrieved.
        - "users" (list): A list of users, where each dictionary represents a users.

    Raises:
    - HTTPException: If there is an error while retrieving the users.
    """
    try:
        session = connect.session
        result = session.query(User)
        output = []
        for r in result:
            output.append({
                "id": r.id,
                "name": r.username,
                "email": r.email,
                "password": r.password
                })
        return {
            "count": len(output),
            "users": output
            }
    except Exception as e:
        print("Unable to get the users. Reason: %s" % str(e))
        raise HTTPException(
            status_code=500,
            detail="Unable to get the users",
        )
