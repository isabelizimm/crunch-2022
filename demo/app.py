from vetiver import VetiverModel
import vetiver
import pins

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.getenv("API_KEY")
rsc_url = os.getenv("RSC_URL")

b = pins.board_rsconnect(server_url=rsc_url, api_key=api_key, allow_pickle_read=True)
v = VetiverModel.from_pin(b, 'isabel.zimmerman/ridership')

vetiver_api = vetiver.VetiverAPI(v)
api = vetiver_api.app
vetiver_api.run()
