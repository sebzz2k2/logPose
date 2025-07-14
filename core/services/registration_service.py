from core.utils import get_country
import uuid

class RegisterationService:
    def __init__(self):
        self._uuid = str(uuid.uuid4()) 

    def is_registered():
        # check if i am registered in db
        # if yes > return True
        # if no > return False
        pass

    def register(self):
        # connect to db 
        country_code = get_country()

        unique_identifier = f"{country_code}-{self._uuid}"
        # insert unique_identifier into db
        # if success > continue
        # if fail > raise exception >
        # while True:
            # check if i am still register
            # ask for who is leader
            # if leader follow leader
            # if no leader election > if only one service you are leader > leader election
            # 

        # if not > try to register agaisn > user expoential backoff + random delay + > restart after a config 
        pass            

