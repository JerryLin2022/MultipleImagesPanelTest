# Generated by Django 3.2.12 on 2022-03-01 12:36

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='stream_body',
            field=wagtail.core.fields.StreamField([('video', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.CharBlock(label='视频标题', max_length=64, required=True)), ('url', wagtail.core.blocks.URLBlock(label='视频网址', max_length=256, required=True)), ('cover', wagtail.images.blocks.ImageChooserBlock(label='视频封面', required=True)), ('intro', wagtail.core.blocks.CharBlock(label='视频说明', max_length=128, required=False))], label='Video Stream Body'))], blank=True, verbose_name='Video Stream Body'),
        ),
        migrations.CreateModel(
            name='HomePageGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='home.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]