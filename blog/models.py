# Create your models here.

from django.conf import settings	# 'from' e 'import' adicionam pedaços de outros arquivos
from django.db import models
from django.utils import timezone

class Post(models.Model):		# linha que define o nosso modelo (é um objeto)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)	# link para outro modelo
    title = models.CharField(max_length=200)			# define texto (título) com nº limitado de caracteres
    text = models.TextField()					# para textos sem limite fixo
    created_date = models.DateTimeField(default=timezone.now)	# data e hora
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def _str_(self):	# 2 '_' é denominado dunder (double-underscore = sublinhado duplo)
        return self.title
        
    # linha 7 => 'class' indica que estamos definindo um objeto; 'Post' é o nome do nosso modelo ...
    #			... o nome de uma classe é sempre iniciado em maiúscula
    #		'models.Model' sgnfik que o Post é um modelo de Django => será salvo no banco de dados
