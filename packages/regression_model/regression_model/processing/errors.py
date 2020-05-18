class BaseError(Exception):
	"""Base package error"""


class InvalidModelInputError(BaseError):
	"""Model Input contains an error"""