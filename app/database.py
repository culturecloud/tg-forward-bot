from umongo import Document, fields
from umongo.frameworks import PyMongoInstance
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from marshmallow.exceptions import ValidationError

from app.config import Config
DATABASE_URI, DATABASE_NAME, COLLECTION_NAME = Config.DATABASE_URI, Config.DATABASE_NAME, Config.COLLECTION_NAME

client = MongoClient(DATABASE_URI)
instance = PyMongoInstance(client.DATABASE_NAME)

@instance.register
class Data(Document):
    id = fields.StrField(attribute='_id')
    channel = fields.StrField()
    file_type = fields.StrField()
    message_id = fields.IntField()
    use = fields.StrField()
    methord = fields.StrField()
    caption = fields.StrField()

    class Meta:
        collection_name = COLLECTION_NAME

Data.ensure_indexes()

async def save_data(id, channel, message_id, methord, caption, file_type):
    try:
        data = Data(
            id=id,
            use = "forward",
            channel=channel,
            message_id=message_id,
            methord=methord,
            caption=caption,
            file_type=file_type
        )
    except ValidationError:
        print('Error occurred while saving file in database')
    try:
        await data.commit()
    except DuplicateKeyError:
        print("Already saved in Database")
    else:
        try:
            print("Messsage saved in DB")
        except:
            pass

async def get_search_results():
    filter = {'use': "forward"}
    cursor = Data.find(filter)
    cursor.sort('$natural', -1)
    cursor.skip(0).limit(1)
    Messages = await cursor.to_list(length=1)
    return Messages

