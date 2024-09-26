from myapp.app.models import Post

Post.objects.create(title="5 пост", content="Содержание первого поста")
Post.objects.create(title="6 пост", content="Содержание второго поста")
Post.objects.create(title="7 пост", content="Содержание третьего поста")
