import vedro
from contexts.api import golden_response, testing_response
from d42 import from_native
from helpers.helpers import prepare_api_character

from vedro_replay import Request, replay


class Scenario(vedro.Scenario):
    subject = "do request: /api/character (comment='{comment}')"

    @replay("requests/character.http")
    def __init__(self, comment: str, request: Request):
        self.comment = comment
        self.request = request

    async def given_golden_response(self):
        self.golden_response = await golden_response(self.request, prepare_api_character)

    async def when_user_sends_request(self):
        self.testing_response = await testing_response(self.request, prepare_api_character)

    def then_it_should_return_same_status(self):
        assert self.testing_response.status == self.golden_response.status

    def and_it_should_return_same_headers(self):
        assert self.testing_response.headers == from_native(self.golden_response.headers)

    def and_it_should_return_same_body(self):
        assert self.testing_response.body == from_native(self.golden_response.body)
