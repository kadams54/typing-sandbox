from typing import Any

from pydantic import BaseModel, ValidationError
from rich import print


# const User = t.type({
#     userId: t.number,
#     name: t.string,
# });
class User(BaseModel):
    user_id: int
    name: str


def run(data: Any) -> None:
    # const decoded = User.decode(data); // Either<Errors, User>
    try:
        decodedUser = User(**data)
    # if (isLeft(decoded)) {
    #   throw Error(
    #     `Could not validate data: ${PathReporter.report(decoded).join("\n")}`
    #   );
    #   // e.g.: Could not validate data: Invalid value "foo" supplied to : { userId: number, name: string }/userId: number
    #
    except ValidationError as error:
        raise Exception(f"Could not validate data: {error}")
    print(f"User: {decodedUser}")
    print(f"User type: {type(decodedUser)}")
