# Generated by Django 4.1 on 2023-05-02 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("word_e_back", "0006_alter_유저_닉네임_alter_유저_아이디_alter_태그_태그이름"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="데이터셋",
            name="모델",
        ),
    ]
