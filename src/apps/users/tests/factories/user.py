import factory
from factory.fuzzy import FuzzyText


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttribute(lambda a: '{}.{}test.com'.format(a.first_name, a.last_name).lower())
    first_name = FuzzyText(length=8)
    last_name = FuzzyText(length=8)

    class Meta:
        model = 'users.User'
