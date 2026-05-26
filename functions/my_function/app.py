from shared_lib import SENTINEL, greet


def lambda_handler(event, _context):
    return {"sentinel": SENTINEL, "msg": greet(event.get("name", "world"))}
