class DomainException(Exception):
    """Base exception for domain errors."""


class TenantNotFound(DomainException):
    """Raised when a tenant cannot be found."""
