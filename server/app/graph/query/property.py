from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models import Property as PropertyModel

class PropertySchema(SQLAlchemyObjectType):
    class Meta:
        model = PropertyModel
