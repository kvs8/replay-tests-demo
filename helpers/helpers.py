from vedro_replay import JsonResponse, MultipartResponse, Response, filter_response


def basic_headers_exclude():
    return ['x-nf-request-id', 'date']


def basic_body_exclude():
    return []


def prepare_api_character(response) -> Response:
    exclude_headers = basic_headers_exclude() + []
    exclude_body = basic_body_exclude() + []
    return filter_response(JsonResponse.from_response(response), exclude_headers, exclude_body)
