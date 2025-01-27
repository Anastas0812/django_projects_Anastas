# Generated by Django 5.1.5 on 2025-01-21 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_articleposition_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='scope',
            options={'ordering': ['tag__name']},
        ),
        migrations.AddField(
            model_name='scope',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.Scope', to='articles.tag'),
        ),
        migrations.AddField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
        migrations.AlterUniqueTogether(
            name='scope',
            unique_together={('article', 'tag')},
        ),
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.DeleteModel(
            name='ArticlePosition',
        ),
    ]
