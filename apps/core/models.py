"""
Core models for Loan Service DRF Backend
Contains abstract base models that other apps inherit from
"""

from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model with common fields
    """

    id = models.BigAutoField(primary_key=True, editable=False, help_text="Unique identifier")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the record was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when the record was last updated")

    class Meta:
        abstract = True
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.__class__.__name__}({self.id})"
