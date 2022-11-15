from django import forms
from .models import PostTag

POST_TAGS = PostTag.objects.all()


class PostTagsForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for tag in POST_TAGS:
            self.fields[tag.slug] = forms.IntegerField(
                label=str(tag),
                widget=forms.NumberInput(attrs={"class": "tags-list__checkbox three-pos-inp", "value": 0}),
            )
            self.fields[tag.slug].required = False



