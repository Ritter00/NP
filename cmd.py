py manage.py shell
from myapp.models import *
us1 = User.objects.create_user(username='Vasya')
us2 = User.objects.create_user(username='John')
Author.objects.create(authorUser= us1)
Author.objects.create(authorUser= us2)
Category.objects.create(category = 'Sport')
Category.objects.create(category = 'IT')
Category.objects.create(category = 'CULTURE')
Category.objects.create(category = 'POLITICS')
au1 = Author.objects.get(id=1)
au2 = Author.objects.get(id=2)
Post.objects.create(author= au1, categoryType= 'AR', title= 'Заголовок_1', text= 'Много, много, очень много текста. Прям, просто очень много текста.......')
Post.objects.create(author= au1, title= 'Заголовок_2', text= 'Попытка номер 2, написать: Много, много, очень много текста. Прям, просто очень много текста.......')
Post.objects.create(author= au2,categoryType=Post.NEWS, title= 'Молния', text= 'Попытка номер 32, написать: Много, много, очень много текста. Прям, просто очень много текста.......')
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
Comment.objects.create(commentPost= Post.objects.get(id=1), commentUser= Author.objects.get(id=1).authorUser,text= 'Cool')
Comment.objects.create(commentPost= Post.objects.get(id=1), commentUser= Author.objects.get(id=2).authorUser,text= 'ok')
Comment.objects.create(commentPost= Post.objects.get(id=2), commentUser= Author.objects.get(id=2).authorUser,text= 'oh, no')
Comment.objects.create(commentPost= Post.objects.get(id=3), commentUser= Author.objects.get(id=1).authorUser,text= 'bla-bla-bla')
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).dislike()
Post.objects.get(id=1).like()
Post.objects.get(id=1).like()
Post.objects.get(id=2).like()
Comment.objects.get(id=3).dislike()
Comment.objects.get(id=3).dislike()
Author.objects.get(id=1).update_rating()
Author.objects.get(id=2).update_rating()
Author.objects.order_by('-ratingAuthor')[0].authorUser.username
Author.objects.order_by('-ratingAuthor')[0].ratingAuthor
best= (Post.objects.all().order_by('-rating').filter(categoryType= Post.ARTICLE))[0]
best.dateCreation
best.author.authorUser.username
best.rating
best.title
best.preview()
comm = Comment.objects.filter(commentPost= best)
for i in comm:
    print(i.id,end=' ')
    print(i.rating,end=' ')
    print(i.text,end=' ')
    print(i.commentUser.username)
