from AbstractRepository import AbstractRepo
from .schemas import SubscriptionUpdate, SubscriptionResponse, SubscriptionCreate
from .models import Subscriprion


class SubscriptionRepo(AbstractRepo):
    model = Subscriprion
    update_schema = SubscriptionUpdate
    create_schema = SubscriptionCreate
    get_schema = SubscriptionResponse

    @classmethod
    async def validate(cls, obj: Subscriprion):
        return cls.get_schema.model_validate(obj)
