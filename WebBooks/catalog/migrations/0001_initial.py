# Generated by Django 4.2.4 on 2023-08-31 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=200, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=200, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дaтa рождения')),
                ('about', models.TextField(help_text='Bвeдитe сведения об авторе', verbose_name='Сведения об авторе')),
                ('photo', models.ImageField(blank=True, help_text='Введите фото автора', null=True, upload_to='images', verbose_name='Фoтo автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Haзвaниe книги')),
                ('year', models.CharField(help_text='Введите год издания', max_length=4, verbose_name='Год издания')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1000, verbose_name='Аннотация книги')),
                ('isbn', models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену книги', max_digits=7, verbose_name='Цeнa (руб.)')),
                ('photo', models.ImageField(help_text='Введите изображение обложки', upload_to='images', verbose_name='Изображение обложки')),
                ('author', models.ManyToManyField(help_text='Выберите автора (авторов) книги', to='catalog.author', verbose_name='Aвтop (авторы) книги')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=200, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите наименование издательства', max_length=20, verbose_name='Издательство')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Cтaтyc экземпляра книги')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер экземпляра', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дaтa окончания статуса')),
                ('book', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Cтaтyc экземпляра книги')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Cтaтyc экземпляра книги')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите жанр для книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(help_text='Выберите издательство', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.publisher', verbose_name='Издательство'),
        ),
    ]
