# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	def __unicode__(self):
		return self.username


class UserList(admin.ModelAdmin):
	list_display = ('id', 'username')


# 专辑
class Item(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	uid = models.IntegerField()

	def __unicode__(self):
		return self.name


# 图片
class Photo(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='./photo/')
	iid = models.IntegerField()
	#uid = models.IntegerField()

	def __unicode__(self):
		return self.title


admin.site.register(User, UserList)
