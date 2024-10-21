# Generated by Django 5.1.2 on 2024-10-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_auctionlisting_id_alter_category_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auctionlisting',
            options={'ordering': ['item_name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='watchlisted_by', to='auctions.auctionlisting'),
        ),
    ]
