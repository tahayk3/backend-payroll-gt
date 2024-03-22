""" Serializers for the services app. """

from rest_framework import serializers


class CMSSerializer(serializers.Serializer):
    """CMS Serializer."""

    content = serializers.JSONField()


class CMSResponseSerializer(serializers.Serializer):
    """CMS Response Serializer."""

    stories = CMSSerializer(many=True)

    def validate_stories(self, value):
        """Validate content."""
        transformed_data = {}
        for item in value:
            component = item["content"]["component"]
            if component not in transformed_data:
                transformed_data[component] = []
            del item["content"]["component"]
            transformed_data[component].append(item["content"])
        return transformed_data
