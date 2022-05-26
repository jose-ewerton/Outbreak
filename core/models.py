from django.db import models

# Create your models here.



class Base(models.Model):
    create = models.DateField('data de criação', auto_now_add=True)
    modificed = models.DateField('data de atualização', auto_now= True)
    active = models.BooleanField('ativo?', default= True)
    
    class Meta:
        abstract = True
        
class Story(Base):
    CATEGORY = (
        ('1', 'action'),
        ('2', 'adventure'),
    )
    TARGET_AUDIENCE = (
        ('1', '8-13 anos de idade'),
        ('2', '13-18 anos de idade'),
    )
    image = models.ImageField('imagem', null = False, blank = False)
    title = models.CharField('título', max_length = 100, null = False, blank = False)
    description = models.CharField('descrição', max_length = 500, null = False, blank = False)
    category = models.CharField('categoria', max_length = 100, choices= CATEGORY)
    target_audience = models.CharField('público-alvo', max_length = 100, choices= TARGET_AUDIENCE)
    language = models.CharField('idioma', max_length = 100, choices=())
    copyright = models.CharField('direitos autorais', max_length = 100, choices=())
    rating = models.CharField('avaliação', max_length = 100, choices=())    
    story_status = models.CharField('história completa?', max_length = 100, choices=())
    permission = models.CharField('permissão para publicar',max_length = 100, choices=())
    


class MainCharacter(models.Model):
    name = models.CharField('personagem', max_length= 100, null = False, blank = False)
    story = models.ForeignKey(Story, on_delete = models.CASCADE)

class Tags(models.Model):
    title = models.CharField('tag', max_length= 50, null = False, blank = False)
    story = models.ForeignKey(Story, on_delete = models.CASCADE)
    
class Chapter(models.Model):
    title_chapter = models.CharField('título do capítulo', max_length= 100, null= False, blank= False)
    content = models.TextField('conteúdo', null= False, blank= False)
    story = models.ForeignKey(Story, on_delete = models.CASCADE)


class Profile(models.Model):
    pass

