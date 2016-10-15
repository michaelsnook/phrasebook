from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import capfirst


class Language(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Card(models.Model):
    # nuggets of the languages people are trying to learn
    text = models.TextField()
    language = models.ForeignKey(Language)
    see_also = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.language.name + ' - ' + self.text


class CardTranslation(models.Model):
    # translations of target cards into other languages people already know
    text = models.TextField()
    literal = models.TextField(blank=True)
    card = models.ForeignKey(Card)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.language.name + ' learning ' + self.card.language.name + ': ' + self.card.text


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_name = models.CharField(max_length=200, blank=True)
    studying_languages = models.ManyToManyField(Language, related_name='students')
    speaks_languages = models.ManyToManyField(Language, related_name='speakers')

    def salutation(self):
        return self.user.first_name or self.user.username

    def username(self):
        return self.user.username

    def name(self):
        return self.user.first_name + ' ' + self.user.last_name if self.user.first_name else self.username()

    def email(self):
        return self.user.email

    def __str__(self):
        return self.name() or self.username()


class Deck(models.Model):
    # one person owns one or more decks
    person = models.ForeignKey(Person)
    language = models.ForeignKey(Language)
    cards = models.ManyToManyField(Card, blank=True)

    def translation_languages(self):
        return self.person.knows

    def __str__(self):
        return capfirst(self.person.name()) + ', ' + self.language.code

"""
class SuggestionStatus(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Suggestion(models.Model):
    card = models.ForeignKey(Card)
    deck = models.ForeignKey(Deck)
    status = models.ForeignKey(SuggestionStatus)
    suggested_by = models.ForeignKey(Person)
    def __str__(self):
        return self.suggested_by.name + ' suggests a ' + self.deck.language.name + ' for ' + self.deck.person.name
"""
