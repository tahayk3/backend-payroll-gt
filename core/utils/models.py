from django.db import models

class BaseModel(models.Model):
    """ Abstract Class, BaseModel
      """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on  was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on  was last modified'
    )

    class Meta:
        """Meta options."""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
